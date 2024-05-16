from queries import Bool, Match

tokens_str = "мой вопрос такой потому что"
pub_id = 5
test_query=  Bool([Match("LemCluster", tokens_str), Match("ParentPubList", pub_id)])
print(test_query)
print(type(test_query))
print(test_query.to_dict())