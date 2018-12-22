import requests
import beautifulsoup

def main():
    url = r'https://movie.douban.com/subject/3878007/'

    response = requests.get(url)
    with open('./test.txt', 'w', encoding = 'utf8') as file:
        file.write(response.text)

def testcases():
    main()

if __name__ == '__main__':
    testcases()
