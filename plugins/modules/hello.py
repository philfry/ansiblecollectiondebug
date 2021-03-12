#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    module = AnsibleModule(argument_spec=dict())
    module.warn("this is a warning")
    module.exit_json(changed = True, msg="Hello world")


######################################################################
from ansible.module_utils.basic import AnsibleModule
main()
