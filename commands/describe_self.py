#####################
# Dennis MUD        #
# describe_self.py  #
# Copyright 2020    #
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

NAME = "describe self"
CATEGORIES = ["settings", "users"]
USAGE = "describe self <description>"
DESCRIPTION = """Set your player description, shown when someone looks at you.

A double backslash inserts a newline. Two sets of double backslashes make a paragraph break.
You may have any number of newlines, but you cannot stack more than two together.

Ex. `describe self This guy is obviously some kind of badass.`
Ex2. `describe self This guy is obviously some kind of badass.\\\\You should probably keep some distance.
Ex3. `describe self This guy is obviously some kind of badass.\\\\\\\\You should probably keep some distance."""


def COMMAND(console, args):
    if len(args) == 0:
        console.msg("Usage: " + USAGE)
        return False

    # Make sure we are logged in.
    if not console.user:
        console.msg(NAME + ": must be logged in first")
        return False

    if "\\\\" * 3 in ' '.join(args):
        console.msg(NAME + ": you may only stack two newlines")
        return False

    console.user["desc"] = ' '.join(args).replace("\\\\", "\n")
    console.database.upsert_user(console.user)
    console.msg(NAME + ": done")
    return True
