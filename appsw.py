from flask import Flask, request, jsonify
import re
import pymysql
import json
#http://ec2-13-125-206-239.ap-northeast-2.compute.amazonaws.com:5000

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='ezendb.chg7hygdd77i.ap-northeast-2.rds.amazonaws.com',
        user='yechan',
        password='1q2w3e!!',
        database='test',
        port=3306
    )

@app.route('/견적', methods=['POST'])
def ruswjr():
    try:
        # "목재_" 엔티티 값 추출
        product = request.json.get('action', {}).get('detailParams', {}).get('인테리어정보', {}).get('origin', '')
        url= "https://www.google.com/maps/search/" + product
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text" : product + '의 url은'+url+'입니다.' 
                        }
                    }
                ]
            }
        }

        return jsonify(response)
    except Exception as e:
        # 예외 처리 로그 기록
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5031)