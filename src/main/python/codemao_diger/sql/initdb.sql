CREATE TABLE
    IF NOT EXISTS posts (
        id INT PRIMARY KEY,
        title TEXT,
        content TEXT,
        user_id TEXT,
        user_nickname TEXT,
        board_id INT,
        board_name TEXT,
        n_views INT,
        n_replies INT,
        n_comments INT
    );

CREATE TABLE
    IF NOT EXISTS noExistPosts (id INT PRIMARY KEY);

CREATE TABLE
    IF NOT EXISTS users (
        id INT PRIMARY KEY, --id
        nickname TEXT, --昵称
        fans_total INT, --粉丝
        liked_total INT, --点赞
        view_times INT, --查看
        collect_times INT, --收藏
        re_created_times INT, --再创作
        attention_total INT --关注
    );

CREATE TABLE
    IF NOT EXISTS not_exist_users (id INT PRIMARY KEY);