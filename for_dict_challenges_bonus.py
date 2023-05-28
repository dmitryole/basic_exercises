"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from collections import Counter
import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

# 1. Вывести айди пользователя, который написал больше всех сообщений.
def user_with_maximum_messages(messages,users = []):
    for message in messages:
        users += [message['sent_by']]
    repeat_user = Counter(users).most_common(1)[0][0]
    return(f'Aйди пользователя, который написал больше всех сообщений: {repeat_user}')
    
# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
def user_with_the_most_responses_per_post(messages, reply_for = []):    
    for message in messages:
        reply_for += [message['reply_for']]
    popular_reply_for = Counter(reply_for).most_common(2)
    if popular_reply_for[0][0] == None:
        popular_reply_for = popular_reply_for[1][0]
    else:    
        popular_reply_for = popular_reply_for[0][0]
    
    for message in messages:
        if message["reply_for"] == popular_reply_for:
            return (f'Айди пользователя, на сообщения которого больше всего отвечали: {message["sent_by"]}')

#3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
def user_with_the_most_responses(messages, users = [], messages_users_and_seen_by = []):
    for message in messages:
        users += [message['sent_by']]
    users = list(set(users))
    
    for message in messages:
        for user in users:
            if message['seen_by'] != user:
                messages_users_and_seen_by.append({'sent_by': message['sent_by'], 'seen_by': message['seen_by']})
            elif message['seen_by'] == user:
                messages_users_and_seen_by['seen_by'] += message['seen_by']
                messages_users_and_seen_by['seen_by'] = list(set(messages_users_and_seen_by['seen_by']))
    
    N = len(messages_users_and_seen_by)
    max = len(messages_users_and_seen_by[0]['seen_by'])
    sent_by = messages_users_and_seen_by[0]['sent_by']
    for i in range(N-1):
        if max < len(messages_users_and_seen_by[i+1]['seen_by']):
            max = len(messages_users_and_seen_by[i+1]['seen_by'])
            sent_by = messages_users_and_seen_by[i+1]['sent_by']
    return(f'Aйди пользователей, сообщения которых видело больше всего уникальных пользователей: {sent_by}')

#4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
def active_time (messages, morning = 0, day = 0, evening = 0):
    for message in messages:
        hour = message['sent_at'].hour
        if hour < 12:
            morning += 1
        elif 12 <= hour <= 18 :
            day += 1
        elif 18 < hour:
            evening += 1

    if morning < day and morning < evening:
        return (f'Больше всего сообщений: утром')
    elif day < morning and day < evening:
        return (f'Больше всего сообщений: днем')
    else:
        return (f'Больше всего сообщений: вечером')

#5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).
 

if __name__ == "__main__":
    #print(generate_chat_history())
    messages = generate_chat_history()
    print(user_with_maximum_messages(messages))
    print(user_with_the_most_responses_per_post(messages))
    print(user_with_the_most_responses(messages))
    print(active_time(messages))