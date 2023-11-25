from flask import jsonify
from schemas.analytics_db import UserHobby, app


@app.route('/<int:join_year>', methods=['GET'])
def get_user_hobbies_per_year_customer(join_year):
    user_hobbies = UserHobby.query.filter(UserHobby.join_year > join_year).distinct(UserHobby.hobby_name).all()

    distinct_hobbies = [item.hobby_name for item in user_hobbies]

    return jsonify(distinct_hobbies)


@app.route('/', methods=['GET'])
def get_all_user_hobbies_customer():
    user_hobbies = UserHobby.query.all()
    data = [
        {'hobby_name': item.hobby_name, 'join_year': item.join_year}
        for item in user_hobbies
    ]
    return jsonify(data)

@app.route('/count/<int:join_year>', methods=['GET'])
def get_all_count_user_hobbies_per_year(join_year):
    count = UserHobby.query.filter(UserHobby.join_year == join_year).distinct(UserHobby.hobby_name).count()
    return jsonify({'year': join_year, 'distinct_hobby_count': count})


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000, host="0.0.0.0")
