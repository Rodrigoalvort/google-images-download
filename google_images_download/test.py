# @title download images
from google_images_download import googleimagesdownload
from multiprocessing import Process, Queue, Pool

search_queries = [
    "gmail interface",
    "outlook interface",
    "windows interface",
    "file system interface",
    "ubuntu interface",
    "paint interface",
    "adobe reader interface",
    "photoshop interface",
    "SAP 2019 interface",
    "chrome interface",
    "instagram interface",
    "pdf interface",
    "windows explorer interface",
    "spotify interface",
    "power point interface",
    "times interface",
    "wallpaper",
    "open office interface",
    "wallpaper pets",
    "wallpaper forest",
    "wallpaper snow",
    "wallpaper cats",
    "excel 2005",
    "excel 2013",
    "excel 2015",
    "excel 2017",
    "excel 2019",
    "excel 2020",
    "excel 2011",
    "linkedin interface",
    "youtube interface",
    "google drive interface",
    "one drive interface",
    "microsoft teams interface",
    "one note interface",
    "skype interface",
    "microsoft word interface",
    "SAP 2019",
    "github interface",
    "bitbucket interface",
    "jira interface",
    "tensor flow interface",
    "playstore interface" "pytorch interface",
    "one note interface",
    "windows update interface",
    "office wallpapers",
    "brands logos wallpaper",
    "linkedin interface",
    "coursera interface",
    "gloud guru interface",
    "computrabajo interface",
    "illustrator interface",
    "avengers endgame wallpaper",
    "apple interface",
    "ubuntu interface",
    "windows explorer interface",
    "aws interface",
    "mongo atlas interface",
    "zendesk interface",
    "cisco interface",
    "whatsapp interface",
    "pinterest interface",
    "galery interface",
    "control panel windows interface",
    "open english interface",
    "trello interface",
    "uber interface",
    "rappi interface",
    "twitter interface",
    "mozilla firefox interface",
    "firefox interface",
    "mozilla interface",
    "tiktok interface",
    "snapchat interface",
    "google forms",
    "matlab forms",
]


def downloadimages(query):
    response = googleimagesdownload()
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    arguments = {
        "keywords": query,
        "format": "jpg",
        "limit": 100,
        "print_urls": False,
        "size": "large",
        "aspect_ratio": "panoramic",
        "silent_mode": True,
    }
    try:
        response.download(arguments)

    # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {
            "keywords": query,
            "format": "jpg",
            "limit": 4,
            "print_urls": False,
            "size": "medium",
        }

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass


# Driver Code
# p = Pool(3)
# _ = p.map(downloadimages, search_queries)

downloadimages(search_queries[0])
