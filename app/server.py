from flask import Flask
from flask import render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    name = "Hello World."
    return render_template('index.html', name=name)


@app.route('/good')
def good():
    name = "Good"
    return name


@app.route('/bad')
def bad():
    name = "Hey, B.A.D."
    return render_template('bad.html', name=name)


@app.route('/json')
def json():
    name = "Hey, B.A.D."
    data = {"data": name}
    return jsonify(data), 200

# おまじない
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)


# 以下のPHPをこちらに移す
# testも書くか


# // データ追記するだけ
# function s(&$var) {
#     return (string)filter_var($var);
# }


# define("FILE", dirname(__FILE__). "/data/voice_data.txt");

# if(!isset($_POST["message"])){
#     ng("no message");
# }


# if(($fp = fopen(FILE, "a")) === false){
#     error_log("open append failed");
#     ng("open append failed");
# }
# fclose($fp);


# $fp = fopen(FILE, "r");

# if (flock($fp, LOCK_EX)) {  // 排他ロックを確保します
#     $num=count( file( FILE ));
#     if($num > 100) {
#         flock($fp, LOCK_UN);    // ロックを解放します
#         fclose($fp);
#         ng(">100");
#     }

#     flock($fp, LOCK_UN);    // ロックを解放します

# } else {

#     fclose($fp);
#     ng("cannot get lock");

# }
# fclose($fp);


# error_log("TYPE=".$_POST["type"]);
# $type = s($_POST['type']);

# if(intval($type) > 0) file_put_contents("/tmp/color", $type);

# // ここでやっと追記


# file_put_contents(FILE, $_POST["message"]."\n", LOCK_EX|FILE_APPEND);

# ok($_POST["message"]);

# function ok($msg){
#     http_response_code(200);
#     echo json_encode(["code"=>0,"msg"=>$msg]);
#     error_log("OK");
#     exit;
# }

# function ng($err){
#     http_response_code(400);
#     echo json_encode(["code"=>1, "msg"=>$err]);
#     exit;
# }
