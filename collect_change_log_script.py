#!/usr/bin/python3
# Authors : Bob Chang

import re
import argparse
import subprocess

def parse_git_log(log_list):

    format_log = ""

    log_list = list(dict.fromkeys(log_list))

    for log in log_list:
        if re.match("^\\[\\S+\\].*|^https:.*|^http:.*", log):
            format_log += "* " + log + "\n"

    return format_log


def main():
    subprocess.run(["git", "checkout", "main"])
    sha_value_head = subprocess.run(["git", "rev-parse", "HEAD"], stdout=subprocess.PIPE)
    sha_value_head = sha_value_head.stdout.decode('utf-8').split("\n")[0]
    sha_value_head_prop = subprocess.run(["git", "rev-parse", "HEAD~"], stdout=subprocess.PIPE)
    sha_value_head_prop = sha_value_head_prop.stdout.decode('utf-8').split("\n")[0]
    argumentForTwoCommitsHash = str(sha_value_head)+"..."+str(sha_value_head_prop)
    log = subprocess.run(["git", "log", "--oneline", "--pretty=%B", argumentForTwoCommitsHash], stdout=subprocess.PIPE)
    log = log.stdout.decode('utf-8').split("\n")[0]
    # log_list = parse_git_log(log)   
    # save text into a file
    with open('CHANGELOG.txt', 'w') as f:
        f.write(log)


if __name__ == '__main__':
    main()
