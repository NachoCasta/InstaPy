""" Quickstart script for InstaPy usage """

# imports
import json
import time
import math
import random
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)
# login credentials
for cuenta in ("memes",):
    with open("credentials.json") as f:
        credentials = json.load(f)[cuenta]
    insta_username = credentials["username"]
    insta_password = credentials["password"]

    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True)

    with smart_run(session):
        """ Activity flow """
        # general settings
        max_follow = 300  # Amount of people to follow

        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        max_followers=4590,
                                        min_followers=45,
                                        min_following=77)
        if cuenta == "memes":
            session.set_do_follow(enabled=True, percentage=10, times=1)
            # activity
            session.unfollow_users(amount=300, InstapyFollowed=(
                True, "all"), style="RANDOM", unfollow_after=24 * 60 * 60, sleep_delay=600)
        tags = ["dji", "gopro", "drone"]
        max_tags = 10  # Max number of total tags to get
        tag_limit = math.ceil(max_tags / len(tags))
        session.set_smart_hashtags(
            tags, limit=tag_limit, sort='top', log_tags=True)
        likes_per_tag = int(max_follow * 10 / max_tags)
        #session.like_by_tags(amount=likes_per_tag, use_smart_hashtags=True)
