from google.appengine.ext import ndb

class Message(ndb.Model):
    type = ndb.StringProperty()
    data = ndb.StringProperty()


class Question(ndb.Model):
    message = ndb.StructedProperty(Message, repeated = TRUE)


class Answer(ndb.Model):
    message = ndb.StructedProperty(Message, repeated = TRUE)


def AddQuestion(key, type, data):
    question = Question.get_or_insert(key)
    question.message.Append(type = type, data = data)
    question.put()


def AddAnswer(key, type, data):
    answer = Answer.get_or_insert(key)
    answer.message.Append(type = type, data = data)
    answer.put()


def GetQuestion(key)
    question = Question.get_by_id(key)
    return question.message


def GetAnswer(key)
    answer = Answer.get_by_id(key)
    return answer.message

