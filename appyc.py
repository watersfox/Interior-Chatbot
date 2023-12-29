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







# get방식
@app.route('/api/sayHello', methods=['GET'])
def hello():
    return "Hello Kakao-Chatbot!!"

# 카드형 응답
@app.route('/api/showHello', methods=['POST'])
def showHello():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": "This is a Title",
                            "description": "This is a description.",
                            "thumbnail": {
                                "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg"
                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "링크로 이동",
                                    "webLinkUrl": "https://www.naver.com"
                                }
                            ]
                        }
                    }
                ]
            }
        }
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#입력메시지 출력
@app.route('/api/usertext', methods=['POST'])
def sayHello2():
    try:
        # 카카오톡에서 받은 사용자의 입력 메시지
        user_message = request.json.get('userRequest', {}).get('utterance', '')

        # 응답 구성
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": f"사용자가 입력한 메시지: {user_message}"
                        }
                    }
                ]
            }
        }

        return responseBody
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

#아메리카노
@app.route('/아메리카노', methods=['POST'])
def americano():
    try:
        # "커피" 엔티티 값 추출
        coffee_name = request.json.get('action', {}).get('params', {}).get('coffee_name', '')
        coffee_number = request.json.get('action', {}).get('detailParams', {}).get('sys_number', {}).get('origin', '')
        coffee_number = re.findall(r'\d+', coffee_number)[0]

        response_message = f"{coffee_name}를 {coffee_number}잔 주문했습니다."
        json_data = request.get_json()
        print(json_data)

        # 응답 구성
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": response_message
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

# 게시판링크
@app.route('/menuLink', methods=['POST'])
def menuLink():
    try:
        title = "test"
        description = "test"
        imageUrl = ""
        label = "test"
        webLinkUrl = ""
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": title,
                            "description": description,
                            "thumbnail": {
                                "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg"
                            },
                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": label+"로 이동",
                                    "webLinkUrl": "https://www.naver.com"
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
        return jsonify(responseBody)
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return {"error": "Internal Server Error"}, 500

@app.route('/견적', methods=['POST'])
def ruswjr():
    try:
        # "목재_" 엔티티 값 추출
        wood = request.json.get('action', {}).get('detailParams', {}).get('목재_', {}).get('origin', '')
        with get_db_connection() as db:
            cursor = db.cursor()

            # 쿼리 실행
            price_query = "SELECT price FROM wood_price WHERE wood = %s"
            cursor.execute(price_query, (wood,))

            # 결과 가져오기
            user_wood_price = cursor.fetchone()[0]

        response_message = user_wood_price

        # 응답 구성
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": response_message
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