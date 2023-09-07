from flask import Blueprint, request
from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    matching_users = []

    for user in USERS:
        match_any_criteria = False

        if "id" in args and args["id"] == user["id"]:
            match_any_criteria = True

        if "name" in args and args["name"] in user["name"]:
            match_any_criteria = True

        if "age" in args and user["age"] == args["age"]:
            match_any_criteria = True

        if "occupation" in args and args["occupation"] == user["occupation"]:
            match_any_criteria = True

        if match_any_criteria:
            matching_users.append(user)

    return matching_users


