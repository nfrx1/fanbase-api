# FanBase API

**FanBase API** is the first external API wrapper for the FanBase application, providing an easy way to interact with FanBase programmatically. The library is open source and built to simplify the process of automating tasks on the platform.

---

## Features
- User authentication via email or username.
- Fetching main feed posts.
- Liking posts.
- Commenting on posts.
- Easy-to-use.
- Fully open source.

---

## Installation
Install the library directly from PyPI:

```pip install fanbase-api```

## Usage
```
import FanBase
import time

client = FanBase.fanbase()

client.login("<EMAIL_OR_USERNAME>", "<PASSWORD>")

while True:
    main_feed = client.get_main_feed()
    for id, type, link in zip(main_feed.ids, main_feed.media_types, main_feed.urls):
        try:
            type = type.replace("image", "post")
            client.like(id, type)
            client.comment_in_post(id, "<COMMENT_TEXT>", type)
            print(f"{type} Success - {link}")
        except Exception as e:
            print(f"{type} Failed - {link} {e}")
    time.sleep(3)
```

## Contributing

Contributions are welcome.

1. Fork the repository.


2. Create a new branch.


3. Make your changes.


4. Submit a pull request.

## License

This project is licensed under the **MIT License**

## Links
[FanBase Offical Website](https://fanbase.app/)

[PyPi Project](https://pypi.org/project/fanbase-api/)

[GitHub Repository](https://github.com/nfrx1/fanbase-api/)

[Telegram Channel](https://t.me/preventx)
## Author
Developed by Kapom²
