def shorten_url(url_id):
	character_store = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	short_url=""
	while url_id>0:
		new_char_index = url_id % 62
		short_url = character_store[new_char_index] + short_url
		url_id = url_id / 62
	return short_url

def get_url_id(short_url):
	character_store = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	url_id = 0
	for i in range(len(short_url)):
		digit = character_store.index(short_url[-(i+1)])
		url_id = url_id + (digit * 62**i)
	return url_id

def test(url_id):
	print "******************"
	print url_id
	print "Shorted url: " + shorten_url(url_id)
	print "Decoded ID: " + str(get_url_id(shorten_url(url_id)))

def main():

	test(72)
	test(12345)

	print "Program ran!"


if __name__ == '__main__':
	main()