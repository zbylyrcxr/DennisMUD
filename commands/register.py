#####################
# Dennis MUD        #
# register.py       #
# Copyright 2018    #
# Michael D. Reiley #
#####################

# **********
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# **********

import hashlib

NAME = "register"
CATEGORIES = ["users"]
USAGE = "register <username> <password>"
DESCRIPTION = "Register a new user with <username> and <password>."


def COMMAND(console, database, args):
    # args = [username, password]
    if len(args) != 2:
        console.msg("Usage: " + USAGE)
        return False

    if console.user:
        console.msg(NAME + ": logout first to register a user")
        return False

    # Register a new user.
    check = database.users.find_one(
        {
            "name": args[0]
        }
    )
    if check:  # User already exists.
        console.msg(NAME + ": user already exists")
        return False

    # Create new user.
    newuser = {
        "name": args[0].lower(),
        "nick": args[0],
        "desc": "",
        "passhash": hashlib.sha256(args[1].encode()).hexdigest(),
        "online": False,
        "room": 0,
        "inventory": [],
        "keys": [],
        "chat": {
            "enabled": True,
            "ignored": []
        },
        "wizard": False
    }

    # Save.
    database.upsert_user(newuser)
    console.msg("registered user \"" + newuser["name"] + "\"")
    return True
