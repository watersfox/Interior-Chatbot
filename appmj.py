from flask import Flask, request, jsonify
import re
import pymysql
import json
#http://ec2-13-125-206-239.ap-northeast-2.compute.amazonaws.com:5000

app = Flask(__name__)


db = pymysql.connect(
    host='ezendb.chg7hygdd77i.ap-northeast-2.rds.amazonaws.com',
    user='yechan',
    password='1q2w3e!!',
    database='interiordb',
    port=3306,
    charset='utf8'
)

#v1.0

app = Flask(__name__)

@app.route('/api/sayHello', methods=['GET'])
def hello():
    return "Hello Kakao-Chatbot!!"

# 1) 카카오톡 텍스트형 응답
@app.route('/api/sayHello', methods=['POST'])
def seyHello():
    user_message = request.json.get('userRequest', {}).get('utterance', '')
    #print(body)
    user_message=int(user_message)

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": user_message + 100000
                    }
                }
            ]
        }
    }
    
    return responseBody;

# 2) 카카오톡 이미지형 응답
@app.route('/api/showHello', methods=['POST'])
def showHello():
    body = request.get_json()
    # print(body)
    
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        "altText": "hello I'm Kakao.Chatbot!!"
                    } 
                }
            ]
        }
    }
    
    return responseBody;

@app.route('/api/showHello5', methods=['POST'])
def showHello5():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
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
                                },
                                {
                                    "title": "This is another Title",
                                    "description": "This is another description.",
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
                                },
                                {
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
    
@app.route('/api/showCard', methods=['POST'])
def showCard():
    try:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
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
                                },
                                {
                                    "title": "This is another Title",
                                    "description": "This is another description.",
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
                                },
                                {
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

@app.route('/부품가격', methods=['POST'])
def productPrice():
    try:
        # "인테리어정보" 엔티티 값 추출
        product = request.json.get('action', {}).get('detailParams', {}).get('인테리어정보', {}).get('origin', '')
        cursor = db.cursor()

        # 쿼리 실행
        price_query = "SELECT MAT_NAME, MAT_PRICE FROM material_price WHERE MAT_CAT = %s"
        cursor.execute(price_query, (product,))

        # 결과 가져오기
        results = cursor.fetchall()

        # 결과가 없을 경우 처리
        if not results:
            user_product_price = "해당 제품의 정보가 없습니다."
        else:
            # 결과가 여러 개일 경우를 위해 for문으로 처리
            user_product_price = ""
            for row in results:
                mat_name, mat_price = row[0], row[1]
                user_product_price += f"{mat_name}의 가격은 {mat_price}입니다\n"

        # 응답 구성
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": user_product_price
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
    app.run(host='0.0.0.0', port=5000)  # web server