#mock_data.py
mock_channel_info_dict_valid = """
{
    "id": "UCKYkVQ",
    "uploader": "SOMECHANNEL",
    "uploader_id": "UCKYkVQ",
    "uploader_url": "https://www.youtube.com/channel/UCKYkVQ",
    "title": "SOMECHANNEL - Videos",
    "availability": null,
    "channel_follower_count": null,
    "description": "",
    "tags": [],
    "thumbnails": [
        {
            "url": "https://yt3.googleusercontent.com/ytc/AGIKgqj",
            "height": 900,
            "width": 900,
            "id": "0",
            "resolution": "900x900"
        },
        {
            "url": "https://yt3.googleusercontent.com/ytc/AGIKgqPv",
            "id": "avatar_uncropped",
            "preference": 1
        }
    ],
    "modified_date": null,
    "view_count": null,
    "playlist_count": 1,
    "channel": "SOMECHANNEL",
    "channel_id": "UCKYkVQ",
    "channel_url": "https://www.youtube.com/channel/UCKYkVQ",
    "_type": "playlist",
    "entries": [
        {
            "_type": "url",
            "ie_key": "Youtube",
            "id": "pcvDIJ",
            "url": "https://www.youtube.com/watch?v=pcvDIJzEeHs",
            "title": "Jakkson at the Mall - 10/18/25",
            "description": "Free concert by Jakkson",
            "duration": 196.0,
            "channel_id": null,
            "channel": null,
            "channel_url": null,
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/pcvDIJzEe/hqdefault",
                    "height": 94,
                    "width": 168
                },
                {
                    "url": "https://i.ytimg.com/vi/pcvDIJzEe/hqdefault",
                    "height": 110,
                    "width": 196
                },
                {
                    "url": "https://i.ytimg.com/vi/pcvDIJzEe/hqdefault",
                    "height": 138,
                    "width": 246
                },
                {
                    "url": "https://i.ytimg.com/vi/pcvDIJzEe/hqdefault",
                    "height": 188,
                    "width": 336
                }
            ],
            "timestamp": null,
            "release_timestamp": null,
            "availability": null,
            "view_count": 123,
            "live_status": null,
            "__x_forwarded_for_ip": null
        }
    ],
    "extractor_key": "YoutubeTab",
    "extractor": "youtube:tab",
    "webpage_url": "https://www.youtube.com/SOMECHANNEL/videos",
    "original_url": "https://www.youtube.com/SOMECHANNEL/videos",
    "webpage_url_basename": "videos",
    "webpage_url_domain": "youtube.com",
    "epoch": 1686571
}
"""
mock_video_info_dict = """
{
    "id": "dQw4w9WgXcQ",
    "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
    "formats": [
        {
            "format_id": "sb2",
            "format_note": "storyboard",
            "ext": "mhtml",
            "protocol": "mhtml",
            "acodec": "none",
            "vcodec": "none",
            "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L0/default.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA8K6eoNau8Nrfvw75AEozRajkKrw",
            "width": 48,
            "height": 27,
            "fps": 0.4716981132075472,
            "rows": 10,
            "columns": 10,
            "fragments": [
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L0/default.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA8K6eoNau8Nrfvw75AEozRajkKrw",
                    "duration": 212.0
                }
            ],
            "resolution": "48x27",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "none",
            "video_ext": "none",
            "format": "sb2 - 48x27 (storyboard)"
        },
        {
            "format_id": "sb1",
            "format_note": "storyboard",
            "ext": "mhtml",
            "protocol": "mhtml",
            "acodec": "none",
            "vcodec": "none",
            "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L1/M$M.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLDwls9iec-gEpWRBfceqOR896b3VQ",
            "width": 80,
            "height": 45,
            "fps": 0.5094339622641509,
            "rows": 10,
            "columns": 10,
            "fragments": [
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L1/M0.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLDwls9iec-gEpWRBfceqOR896b3VQ",
                    "duration": 196.29629629629628
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L1/M1.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLDwls9iec-gEpWRBfceqOR896b3VQ",
                    "duration": 15.703703703703724
                }
            ],
            "resolution": "80x45",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "none",
            "video_ext": "none",
            "format": "sb1 - 80x45 (storyboard)"
        },
        {
            "format_id": "sb0",
            "format_note": "storyboard",
            "ext": "mhtml",
            "protocol": "mhtml",
            "acodec": "none",
            "vcodec": "none",
            "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M$M.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
            "width": 160,
            "height": 90,
            "fps": 0.5094339622641509,
            "rows": 5,
            "columns": 5,
            "fragments": [
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M0.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 49.07407407407407
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M1.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 49.07407407407407
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M2.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 49.07407407407407
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M3.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 49.07407407407407
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M4.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 15.703703703703724
                }
            ],
            "resolution": "160x90",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "none",
            "video_ext": "none",
            "format": "sb0 - 160x90 (storyboard)"
        },
        {
            "asr": 22050,
            "filesize": 817805,
            "format_id": "599",
            "format_note": "ultralow",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 1.0,
            "has_drm": false,
            "tbr": 30.833,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=599&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=817805&dur=212.183&lmt=1674227828689068&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgKJg8bJewSLbo2_I642PHPsVY7ro3y1Jc-su-nZEBluICIQDiYAYLvvqEdDZ5oKjO-ZuA7Gx4yI_UXDk9jZz_sydenA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "m4a",
            "vcodec": "none",
            "acodec": "mp4a.40.5",
            "dynamic_range": null,
            "abr": 30.833,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=599&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=817805&dur=212.183&lmt=1674227828689068&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgKJg8bJewSLbo2_I642PHPsVY7ro3y1Jc-su-nZEBluICIQDiYAYLvvqEdDZ5oKjO-ZuA7Gx4yI_UXDk9jZz_sydenA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J&range=0-817805"
                }
            ],
            "container": "m4a_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "m4a",
            "video_ext": "none",
            "format": "599 - audio only (ultralow)"
        },
        {
            "asr": 48000,
            "filesize": 832823,
            "format_id": "600",
            "format_note": "ultralow",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 1.0,
            "has_drm": false,
            "tbr": 31.418,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=600&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=832823&dur=212.061&lmt=1674227828749650&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAMwP4TL1wQ9lmSnHE5-nWbJOnpbUhGEjgTXAfME_RcFSAiEAkWNFqfpv0meVzval-DRS-8ERJCMLf5_AKHwBUEMhNd8%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "none",
            "acodec": "opus",
            "dynamic_range": null,
            "abr": 31.418,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=600&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=832823&dur=212.061&lmt=1674227828749650&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAMwP4TL1wQ9lmSnHE5-nWbJOnpbUhGEjgTXAfME_RcFSAiEAkWNFqfpv0meVzval-DRS-8ERJCMLf5_AKHwBUEMhNd8%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J&range=0-832823"
                }
            ],
            "container": "webm_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "webm",
            "video_ext": "none",
            "format": "600 - audio only (ultralow)"
        },
        {
            "asr": 22050,
            "filesize": 1294944,
            "format_id": "139",
            "format_note": "low",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 2.0,
            "has_drm": false,
            "tbr": 48.823,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=139&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=1294944&dur=212.183&lmt=1674228035408340&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAJGLVIXjuyy8DPnEM9ubj_nOGctcrXY957ZQrglrCj3XAiEApOQLXkq234Bvq9brPRcaaFSAqzsuNrvDjv40FSKTEP0%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "m4a",
            "vcodec": "none",
            "acodec": "mp4a.40.5",
            "dynamic_range": null,
            "abr": 48.823,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=139&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=1294944&dur=212.183&lmt=1674228035408340&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAJGLVIXjuyy8DPnEM9ubj_nOGctcrXY957ZQrglrCj3XAiEApOQLXkq234Bvq9brPRcaaFSAqzsuNrvDjv40FSKTEP0%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J&range=0-1294944"
                }
            ],
            "container": "m4a_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "m4a",
            "video_ext": "none",
            "format": "139 - audio only (low)"
        },
        {
            "asr": null,
            "filesize": 1859270,
            "format_id": "160",
            "format_note": "144p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 144,
            "quality": 0.0,
            "has_drm": false,
            "tbr": 70.147,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599524&ei=BCOHZKKQEdyE_9EPgdiNgAs&ip=96.250.56.162&id=o-AL9ehfH25OZcxgnqr2O5dl_YkZv-HcPkgorYeNut0fJo&itag=160&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1561250&spc=qEK7B_YFnVd5GeXfVPjPP0IRDHrsqNo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=1859270&dur=212.040&lmt=1674233649874257&mt=1686577548&fvip=2&keepalive=yes&fexp=24007246%2C24363392&beids=24350017&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAIz0Kn4xxZCXPLMhQaP-yB76j2aldsXcT1CSI7nsNPveAiBHSUAVZorf_ARYCTDULCsoDps_OadggV5Ez-Yen61ONg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAKAkuDQm8OIoRyZQnAtaLgrx96ppNVfR2HnDWJVQ97F2AiA0b4mzmAT-_X-Fhp3a0QIwicU8Dr-RYvH4LckKHzwCmQ%3D%3D",
            "width": 256,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.4d400c",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 70.147,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599524&ei=BCOHZKKQEdyE_9EPgdiNgAs&ip=96.250.56.162&id=o-AL9ehfH25OZcxgnqr2O5dl_YkZv-HcPkgorYeNut0fJo&itag=160&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1561250&spc=qEK7B_YFnVd5GeXfVPjPP0IRDHrsqNo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=1859270&dur=212.040&lmt=1674233649874257&mt=1686577548&fvip=2&keepalive=yes&fexp=24007246%2C24363392&beids=24350017&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAIz0Kn4xxZCXPLMhQaP-yB76j2aldsXcT1CSI7nsNPveAiBHSUAVZorf_ARYCTDULCsoDps_OadggV5Ez-Yen61ONg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAKAkuDQm8OIoRyZQnAtaLgrx96ppNVfR2HnDWJVQ97F2AiA0b4mzmAT-_X-Fhp3a0QIwicU8Dr-RYvH4LckKHzwCmQ%3D%3D&range=0-1859270"
                }
            ],
            "container": "mp4_dash",
            "resolution": "256x144",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "160 - 256x144 (144p)"
        },
        {
            "asr": null,
            "filesize": 2157715,
            "format_id": "278",
            "format_note": "144p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 144,
            "quality": 0.0,
            "has_drm": false,
            "tbr": 81.407,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599524&ei=BCOHZKKQEdyE_9EPgdiNgAs&ip=96.250.56.162&id=o-AL9ehfH25OZcxgnqr2O5dl_YkZv-HcPkgorYeNut0fJo&itag=278&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1561250&spc=qEK7B_YFnVd5GeXfVPjPP0IRDHrsqNo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=2157715&dur=212.040&lmt=1674240806546279&mt=1686577548&fvip=2&keepalive=yes&fexp=24007246%2C24363392&beids=24350017&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgA5Y4QZ2IW_4weXK0lZ4yLI_9ZqPzqYNgoYq6zy5vD5oCIBYS6s0rhY2lcTJcJH2Lkj0L9eBlp2goIKP2osj9egWI&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAKAkuDQm8OIoRyZQnAtaLgrx96ppNVfR2HnDWJVQ97F2AiA0b4mzmAT-_X-Fhp3a0QIwicU8Dr-RYvH4LckKHzwCmQ%3D%3D",
            "width": 256,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 81.407,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599524&ei=BCOHZKKQEdyE_9EPgdiNgAs&ip=96.250.56.162&id=o-AL9ehfH25OZcxgnqr2O5dl_YkZv-HcPkgorYeNut0fJo&itag=278&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1561250&spc=qEK7B_YFnVd5GeXfVPjPP0IRDHrsqNo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=2157715&dur=212.040&lmt=1674240806546279&mt=1686577548&fvip=2&keepalive=yes&fexp=24007246%2C24363392&beids=24350017&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgA5Y4QZ2IW_4weXK0lZ4yLI_9ZqPzqYNgoYq6zy5vD5oCIBYS6s0rhY2lcTJcJH2Lkj0L9eBlp2goIKP2osj9egWI&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAKAkuDQm8OIoRyZQnAtaLgrx96ppNVfR2HnDWJVQ97F2AiA0b4mzmAT-_X-Fhp3a0QIwicU8Dr-RYvH4LckKHzwCmQ%3D%3D&range=0-2157715"
                }
            ],
            "container": "webm_dash",
            "resolution": "256x144",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "278 - 256x144 (144p)"
        },
        {
            "asr": null,
            "filesize": 55643203,
            "format_id": "248",
            "format_note": "1080p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 1080,
            "quality": 9.0,
            "has_drm": false,
            "tbr": 2099.347,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D",
            "width": 1920,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 2099.347,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=10485760-20971519"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=20971520-31457279"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=31457280-41943039"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=41943040-52428799"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=52428800-55643203"
                }
            ],
            "container": "webm_dash",
            "resolution": "1920x1080",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "248 - 1920x1080 (1080p)"
        }
    ],
    "thumbnails": [
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/3.jpg",
            "preference": -37,
            "id": "0"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/3.webp",
            "preference": -36,
            "id": "1"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/maxresdefault.webp",
            "height": 1080,
            "width": 1920,
            "preference": 0,
            "id": "41",
            "resolution": "1920x1080"
        }
    ],
    "thumbnail": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/maxresdefault.webp",
    "description": "The official video for \u201cNever Gonna Give You Up\u201d by Rick Astley\n\n\u2018Hold Me In Your Arms\u2019 \u2013 deluxe blue vinyl,  2CD and digital deluxe out 12th May 2023 Pre-order here \u2013 https://rick-astley.lnk.to/HMIYA2023ID\n\n\u201cNever Gonna Give You Up\u201d was a global smash on its release in July 1987, topping the charts in 25 countries including Rick\u2019s native UK and the US Billboard Hot 100.  It also won the Brit Award for Best single in 1988. Stock Aitken and Waterman wrote and produced the track which was the lead-off single and lead track from Rick\u2019s debut LP \u201cWhenever You Need Somebody\u201d.  The album was itself a UK number one and would go on to sell over 15 million copies worldwide.\n\nThe legendary video was directed by Simon West \u2013 who later went on to make Hollywood blockbusters such as Con Air, Lara Croft \u2013 Tomb Raider and The Expendables 2.  The video passed the 1bn YouTube views milestone on 28 July 2021.\n\nSubscribe to the official Rick Astley YouTube channel: https://RickAstley.lnk.to/YTSubID\n\nFollow Rick Astley:\nFacebook: https://RickAstley.lnk.to/FBFollowID \nTwitter: https://RickAstley.lnk.to/TwitterID \nInstagram: https://RickAstley.lnk.to/InstagramID \nWebsite: https://RickAstley.lnk.to/storeID \nTikTok: https://RickAstley.lnk.to/TikTokID\n\nListen to Rick Astley:\nSpotify: https://RickAstley.lnk.to/SpotifyID \nApple Music: https://RickAstley.lnk.to/AppleMusicID \nAmazon Music: https://RickAstley.lnk.to/AmazonMusicID \nDeezer: https://RickAstley.lnk.to/DeezerID \n\nLyrics:\nWe\u2019re no strangers to love\nYou know the rules and so do I\nA full commitment\u2019s what I\u2019m thinking of\nYou wouldn\u2019t get this from any other guy\n\nI just wanna tell you how I\u2019m feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWe\u2019ve known each other for so long\nYour heart\u2019s been aching but you\u2019re too shy to say it\nInside we both know what\u2019s been going on\nWe know the game and we\u2019re gonna play it\n\nAnd if you ask me how I\u2019m feeling\nDon\u2019t tell me you\u2019re too blind to see\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\n#RickAstley #NeverGonnaGiveYouUp #WheneverYouNeedSomebody #OfficialMusicVideo",
    "uploader": "Rick Astley",
    "uploader_id": "@RickAstleyYT",
    "uploader_url": "http://www.youtube.com/@RickAstleyYT",
    "channel_id": "UCuAXFkgsw1L7xaCfnd5JJOw",
    "channel_url": "https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw",
    "duration": 212,
    "view_count": 1405669322,
    "average_rating": null,
    "age_limit": 0,
    "webpage_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "categories": [
        "Music"
    ],
    "tags": [
        "rick astley",
        "Never Gonna Give You Up",
        "nggyu",
        "never gonna give you up lyrics",
        "rick rolled",
        "Rick Roll",
        "rick astley official",
        "rickrolled",
        "Fortnite song",
        "Fortnite event",
        "Fortnite dance",
        "fortnite never gonna give you up",
        "rick roll",
        "rickrolling",
        "rick rolling",
        "never gonna give you up",
        "80s music",
        "rick astley new",
        "animated video",
        "rickroll",
        "meme songs",
        "never gonna give u up lyrics",
        "Rick Astley 2022",
        "never gonna let you down",
        "animated",
        "rick rolls 2022",
        "never gonna give you up karaoke"
    ],
    "playable_in_embed": true,
    "live_status": "not_live",
    "release_timestamp": null,
    "_format_sort_fields": [
        "quality",
        "res",
        "fps",
        "hdr:12",
        "source",
        "vcodec:vp9.2",
        "channels",
        "acodec",
        "lang",
        "proto"
    ],
    "automatic_captions": {
        "af": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=af&fmt=json3",
                "name": "Afrikaans"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=ak&fmt=vtt",
                "name": "Akan"
            }
        ],
        "sq": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=sq&fmt=json3",
                "name": "Albanian"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=sq&fmt=srv1",
                "name": "Albanian"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=sq&fmt=vtt",
                "name": "Albanian"
            }
        ],
                    {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=xh&fmt=vtt",
                "name": "Xhosa"
            }
        ],
        "yi": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=json3",
                "name": "Yiddish"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=srv1",
                "name": "Yiddish"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=srv2",
                "name": "Yiddish"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=srv3",
                "name": "Yiddish"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=ttml",
                "name": "Yiddish"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=vtt",
                "name": "Yiddish"
            }
        ],
        "yo": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=json3",
                "name": "Yoruba"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=srv1",
                "name": "Yoruba"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=srv2",
                "name": "Yoruba"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=srv3",
                "name": "Yoruba"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=ttml",
                "name": "Yoruba"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=vtt",
                "name": "Yoruba"
            }
        ],
        "zu": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=json3",
                "name": "Zulu"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=srv1",
                "name": "Zulu"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=srv2",
                "name": "Zulu"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=srv3",
                "name": "Zulu"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=ttml",
                "name": "Zulu"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=vtt",
                "name": "Zulu"
            }
        ]
    },
    "subtitles": {},
    "comment_count": null,
    "chapters": null,
    "like_count": 16479557,
    "channel": "Rick Astley",
    "channel_follower_count": 3710000,
    "upload_date": "20091025",
    "availability": "public",
    "original_url": "https://youtu.be/dQw4w9WgXcQ",
    "webpage_url_basename": "watch",
    "webpage_url_domain": "youtube.com",
    "extractor": "youtube",
    "extractor_key": "Youtube",
    "playlist": null,
    "playlist_index": null,
    "display_id": "dQw4w9WgXcQ",
    "fulltitle": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
    "duration_string": "3:32",
    "is_live": false,
    "was_live": false,
    "requested_subtitles": null,
    "_has_drm": null,
    "requested_formats": [
        {
            "asr": null,
            "filesize": 55643203,
            "format_id": "248",
            "format_note": "1080p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 1080,
            "quality": 9.0,
            "has_drm": false,
            "tbr": 2099.347,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D",
            "width": 1920,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 2099.347,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=10485760-20971519"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=20971520-31457279"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=31457280-41943039"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=41943040-52428799"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=52428800-55643203"
                }
            ],
            "container": "webm_dash",
            "resolution": "1920x1080",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.24 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "248 - 1920x1080 (1080p)"
        },
        {
            "asr": 48000,
            "filesize": 3437753,
            "format_id": "251",
            "format_note": "medium",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 3.0,
            "has_drm": false,
            "tbr": 129.689,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=251&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=3437753&dur=212.061&lmt=1674228069793936&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgQcD6YPngvU_wfvh76Cuh8oaq4_qGtxvzM_JjhwzzJCMCIH-gbOVTziJC2nYPsJPWALIL71RCIBi1YJxZDi3qkDOP&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "none",
            "acodec": "opus",
            "dynamic_range": null,
            "abr": 129.689,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=251&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=3437753&dur=212.061&lmt=1674228069793936&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgQcD6YPngvU_wfvh76Cuh8oaq4_qGtxvzM_JjhwzzJCMCIH-gbOVTziJC2nYPsJPWALIL71RCIBi1YJxZDi3qkDOP&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=0-3437753"
                }
            ],
            "container": "webm_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.24 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "webm",
            "video_ext": "none",
            "format": "251 - audio only (medium)"
        }
    ],
    "format": "248 - 1920x1080 (1080p)+251 - audio only (medium)",
    "format_id": "248+251",
    "ext": "webm",
    "protocol": "http_dash_segments+http_dash_segments",
    "language": null,
    "format_note": "1080p+medium",
    "filesize_approx": 59080956,
    "tbr": 2229.036,
    "width": 1920,
    "height": 1080,
    "resolution": "1920x1080",
    "fps": 25,
    "dynamic_range": "SDR",
    "vcodec": "vp9",
    "vbr": 2099.347,
    "stretched_ratio": null,
    "aspect_ratio": 1.78,
    "acodec": "opus",
    "abr": 129.689,
    "asr": 48000,
    "audio_channels": 2
}
        
"""
mock_video_mp3 = """
{}
"""
mock_video_mp4 = """
{}
"""
mock_transcribed_text_simple = """
{
    "text": "This is a transcribed text. I'm gonna save goodbye",
    "segments": [
        {
            "id": 80,
            "seek": 19796,
            "start": 208.96,
            "end": 210.96,
            "text": "I'm gonna save goodbye",
            "tokens": [50913, 314, 1101, 8066, 3613, 24829, 51013],
            "temperature": 0.6,
            "avg_logprob": -0.35754344463348386,
            "compression_ratio": 1.6338028169014085,
            "no_speech_prob": 0.15678729116916656
        }
    ],
    "language": "en"
}
"""
mock_transcribed_text_complex = """
{
    "id": "dQw4w9WgXcQ",
    "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
    "formats": [
        {
            "format_id": "sb2",
            "format_note": "storyboard",
            "ext": "mhtml",
            "protocol": "mhtml",
            "acodec": "none",
            "vcodec": "none",
            "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L0/default.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA8K6eoNau8Nrfvw75AEozRajkKrw",
            "width": 48,
            "height": 27,
            "fps": 0.4716981132075472,
            "rows": 10,
            "columns": 10,
            "fragments": [
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L0/default.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA8K6eoNau8Nrfvw75AEozRajkKrw",
                    "duration": 212.0
                }
            ],
            "resolution": "48x27",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "none",
            "video_ext": "none",
            "format": "sb2 - 48x27 (storyboard)"
        },
        {
            "format_id": "sb1",
            "format_note": "storyboard",
            "ext": "mhtml",
            "protocol": "mhtml",
            "acodec": "none",
            "vcodec": "none",
            "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L1/M$M.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLDwls9iec-gEpWRBfceqOR896b3VQ",
            "width": 80,
            "height": 45,
            "fps": 0.5094339622641509,
            "rows": 10,
            "columns": 10,
            "fragments": [
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L1/M0.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLDwls9iec-gEpWRBfceqOR896b3VQ",
                    "duration": 196.29629629629628
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L1/M1.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLDwls9iec-gEpWRBfceqOR896b3VQ",
                    "duration": 15.703703703703724
                }
            ],
            "resolution": "80x45",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "none",
            "video_ext": "none",
            "format": "sb1 - 80x45 (storyboard)"
        },
        {
            "format_id": "sb0",
            "format_note": "storyboard",
            "ext": "mhtml",
            "protocol": "mhtml",
            "acodec": "none",
            "vcodec": "none",
            "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M$M.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
            "width": 160,
            "height": 90,
            "fps": 0.5094339622641509,
            "rows": 5,
            "columns": 5,
            "fragments": [
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M0.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 49.07407407407407
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M1.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 49.07407407407407
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M2.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 49.07407407407407
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M3.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 49.07407407407407
                },
                {
                    "url": "https://i.ytimg.com/sb/dQw4w9WgXcQ/storyboard3_L2/M4.jpg?sqp=-oaymwENSDfyq4qpAwVwAcABBqLzl_8DBgjG6eqGBg==&sigh=rs$AOn4CLA7ioYvdz7gKhqPB3nVq40upUWrbw",
                    "duration": 15.703703703703724
                }
            ],
            "resolution": "160x90",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "none",
            "video_ext": "none",
            "format": "sb0 - 160x90 (storyboard)"
        },
        {
            "asr": 22050,
            "filesize": 817805,
            "format_id": "599",
            "format_note": "ultralow",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 1.0,
            "has_drm": false,
            "tbr": 30.833,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=599&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=817805&dur=212.183&lmt=1674227828689068&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgKJg8bJewSLbo2_I642PHPsVY7ro3y1Jc-su-nZEBluICIQDiYAYLvvqEdDZ5oKjO-ZuA7Gx4yI_UXDk9jZz_sydenA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "m4a",
            "vcodec": "none",
            "acodec": "mp4a.40.5",
            "dynamic_range": null,
            "abr": 30.833,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=599&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=817805&dur=212.183&lmt=1674227828689068&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgKJg8bJewSLbo2_I642PHPsVY7ro3y1Jc-su-nZEBluICIQDiYAYLvvqEdDZ5oKjO-ZuA7Gx4yI_UXDk9jZz_sydenA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J&range=0-817805"
                }
            ],
            "container": "m4a_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "m4a",
            "video_ext": "none",
            "format": "599 - audio only (ultralow)"
        },
        {
            "asr": 48000,
            "filesize": 832823,
            "format_id": "600",
            "format_note": "ultralow",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 1.0,
            "has_drm": false,
            "tbr": 31.418,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=600&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=832823&dur=212.061&lmt=1674227828749650&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAMwP4TL1wQ9lmSnHE5-nWbJOnpbUhGEjgTXAfME_RcFSAiEAkWNFqfpv0meVzval-DRS-8ERJCMLf5_AKHwBUEMhNd8%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "none",
            "acodec": "opus",
            "dynamic_range": null,
            "abr": 31.418,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=600&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=832823&dur=212.061&lmt=1674227828749650&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAMwP4TL1wQ9lmSnHE5-nWbJOnpbUhGEjgTXAfME_RcFSAiEAkWNFqfpv0meVzval-DRS-8ERJCMLf5_AKHwBUEMhNd8%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J&range=0-832823"
                }
            ],
            "container": "webm_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "webm",
            "video_ext": "none",
            "format": "600 - audio only (ultralow)"
        },
        {
            "asr": 22050,
            "filesize": 1294944,
            "format_id": "139",
            "format_note": "low",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 2.0,
            "has_drm": false,
            "tbr": 48.823,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=139&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=1294944&dur=212.183&lmt=1674228035408340&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAJGLVIXjuyy8DPnEM9ubj_nOGctcrXY957ZQrglrCj3XAiEApOQLXkq234Bvq9brPRcaaFSAqzsuNrvDjv40FSKTEP0%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "m4a",
            "vcodec": "none",
            "acodec": "mp4a.40.5",
            "dynamic_range": null,
            "abr": 48.823,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599269&ei=BSKHZNeMJY_T8wTokaiYCg&ip=96.250.56.162&id=o-AB1DnR11MtnAd8nmyDkn5Yh59deUrPXv2FlkfkyNrzsO&itag=139&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1578750&spc=qEK7B0-L838T_2O0YErwMBFPHxn6uxE&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=1294944&dur=212.183&lmt=1674228035408340&mt=1686577330&fvip=2&keepalive=yes&fexp=24007246%2C51000023&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAJGLVIXjuyy8DPnEM9ubj_nOGctcrXY957ZQrglrCj3XAiEApOQLXkq234Bvq9brPRcaaFSAqzsuNrvDjv40FSKTEP0%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPlAqIxNAERasxB8efAByFJMZWb0VSaM-Tx6qaogWWyQCIFUM22X8Cg62wdfkgAPPQrx-HclMlF3GzMyNmNt0Y02J&range=0-1294944"
                }
            ],
            "container": "m4a_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "m4a",
            "video_ext": "none",
            "format": "139 - audio only (low)"
        },
        {
            "asr": null,
            "filesize": 1859270,
            "format_id": "160",
            "format_note": "144p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 144,
            "quality": 0.0,
            "has_drm": false,
            "tbr": 70.147,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599524&ei=BCOHZKKQEdyE_9EPgdiNgAs&ip=96.250.56.162&id=o-AL9ehfH25OZcxgnqr2O5dl_YkZv-HcPkgorYeNut0fJo&itag=160&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1561250&spc=qEK7B_YFnVd5GeXfVPjPP0IRDHrsqNo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=1859270&dur=212.040&lmt=1674233649874257&mt=1686577548&fvip=2&keepalive=yes&fexp=24007246%2C24363392&beids=24350017&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAIz0Kn4xxZCXPLMhQaP-yB76j2aldsXcT1CSI7nsNPveAiBHSUAVZorf_ARYCTDULCsoDps_OadggV5Ez-Yen61ONg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAKAkuDQm8OIoRyZQnAtaLgrx96ppNVfR2HnDWJVQ97F2AiA0b4mzmAT-_X-Fhp3a0QIwicU8Dr-RYvH4LckKHzwCmQ%3D%3D",
            "width": 256,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.4d400c",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 70.147,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599524&ei=BCOHZKKQEdyE_9EPgdiNgAs&ip=96.250.56.162&id=o-AL9ehfH25OZcxgnqr2O5dl_YkZv-HcPkgorYeNut0fJo&itag=160&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1561250&spc=qEK7B_YFnVd5GeXfVPjPP0IRDHrsqNo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=1859270&dur=212.040&lmt=1674233649874257&mt=1686577548&fvip=2&keepalive=yes&fexp=24007246%2C24363392&beids=24350017&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAIz0Kn4xxZCXPLMhQaP-yB76j2aldsXcT1CSI7nsNPveAiBHSUAVZorf_ARYCTDULCsoDps_OadggV5Ez-Yen61ONg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAKAkuDQm8OIoRyZQnAtaLgrx96ppNVfR2HnDWJVQ97F2AiA0b4mzmAT-_X-Fhp3a0QIwicU8Dr-RYvH4LckKHzwCmQ%3D%3D&range=0-1859270"
                }
            ],
            "container": "mp4_dash",
            "resolution": "256x144",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "160 - 256x144 (144p)"
        },
        {
            "asr": null,
            "filesize": 2157715,
            "format_id": "278",
            "format_note": "144p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 144,
            "quality": 0.0,
            "has_drm": false,
            "tbr": 81.407,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599524&ei=BCOHZKKQEdyE_9EPgdiNgAs&ip=96.250.56.162&id=o-AL9ehfH25OZcxgnqr2O5dl_YkZv-HcPkgorYeNut0fJo&itag=278&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1561250&spc=qEK7B_YFnVd5GeXfVPjPP0IRDHrsqNo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=2157715&dur=212.040&lmt=1674240806546279&mt=1686577548&fvip=2&keepalive=yes&fexp=24007246%2C24363392&beids=24350017&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgA5Y4QZ2IW_4weXK0lZ4yLI_9ZqPzqYNgoYq6zy5vD5oCIBYS6s0rhY2lcTJcJH2Lkj0L9eBlp2goIKP2osj9egWI&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAKAkuDQm8OIoRyZQnAtaLgrx96ppNVfR2HnDWJVQ97F2AiA0b4mzmAT-_X-Fhp3a0QIwicU8Dr-RYvH4LckKHzwCmQ%3D%3D",
            "width": 256,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 81.407,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599524&ei=BCOHZKKQEdyE_9EPgdiNgAs&ip=96.250.56.162&id=o-AL9ehfH25OZcxgnqr2O5dl_YkZv-HcPkgorYeNut0fJo&itag=278&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qlsnd6&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1561250&spc=qEK7B_YFnVd5GeXfVPjPP0IRDHrsqNo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=2157715&dur=212.040&lmt=1674240806546279&mt=1686577548&fvip=2&keepalive=yes&fexp=24007246%2C24363392&beids=24350017&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgA5Y4QZ2IW_4weXK0lZ4yLI_9ZqPzqYNgoYq6zy5vD5oCIBYS6s0rhY2lcTJcJH2Lkj0L9eBlp2goIKP2osj9egWI&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAKAkuDQm8OIoRyZQnAtaLgrx96ppNVfR2HnDWJVQ97F2AiA0b4mzmAT-_X-Fhp3a0QIwicU8Dr-RYvH4LckKHzwCmQ%3D%3D&range=0-2157715"
                }
            ],
            "container": "webm_dash",
            "resolution": "256x144",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "278 - 256x144 (144p)"
        },
        {
            "asr": null,
            "filesize": 55643203,
            "format_id": "248",
            "format_note": "1080p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 1080,
            "quality": 9.0,
            "has_drm": false,
            "tbr": 2099.347,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D",
            "width": 1920,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 2099.347,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=10485760-20971519"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=20971520-31457279"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=31457280-41943039"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=41943040-52428799"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686599766&ei=9iOHZKPhNcyL_9EPtbivqAQ&ip=96.250.56.162&id=o-AH06eU5Nd4w3IG1DSqZP-vhT0MG6oP6sYIH51bhyac8r&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&pcm2=no&initcwndbps=1566250&spc=qEK7B_UBK21frOcefvbF56lwzP2cKbc&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686577798&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIloaeDnJb2WSg5yv4MewlXF0DUrVeylDneUe8dyf1G5AiEAhVHT-EhKwR1SzhmBbJvLxu3Qut_tTa24a97WKB8KyEg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPCE5jBv3MW7xNtWZUym-Jsz9kiVEra1LBKr_EthXPqRAiEAn198N19RGqEZTH_0yzHFRXnN3LYoNksu8W84pMYvdXo%3D&range=52428800-55643203"
                }
            ],
            "container": "webm_dash",
            "resolution": "1920x1080",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "248 - 1920x1080 (1080p)"
        }
    ],
    "thumbnails": [
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/3.jpg",
            "preference": -37,
            "id": "0"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/3.webp",
            "preference": -36,
            "id": "1"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/maxresdefault.webp",
            "height": 1080,
            "width": 1920,
            "preference": 0,
            "id": "41",
            "resolution": "1920x1080"
        }
    ],
    "thumbnail": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/maxresdefault.webp",
    "description": "The official video for \u201cNever Gonna Give You Up\u201d by Rick Astley\n\n\u2018Hold Me In Your Arms\u2019 \u2013 deluxe blue vinyl,  2CD and digital deluxe out 12th May 2023 Pre-order here \u2013 https://rick-astley.lnk.to/HMIYA2023ID\n\n\u201cNever Gonna Give You Up\u201d was a global smash on its release in July 1987, topping the charts in 25 countries including Rick\u2019s native UK and the US Billboard Hot 100.  It also won the Brit Award for Best single in 1988. Stock Aitken and Waterman wrote and produced the track which was the lead-off single and lead track from Rick\u2019s debut LP \u201cWhenever You Need Somebody\u201d.  The album was itself a UK number one and would go on to sell over 15 million copies worldwide.\n\nThe legendary video was directed by Simon West \u2013 who later went on to make Hollywood blockbusters such as Con Air, Lara Croft \u2013 Tomb Raider and The Expendables 2.  The video passed the 1bn YouTube views milestone on 28 July 2021.\n\nSubscribe to the official Rick Astley YouTube channel: https://RickAstley.lnk.to/YTSubID\n\nFollow Rick Astley:\nFacebook: https://RickAstley.lnk.to/FBFollowID \nTwitter: https://RickAstley.lnk.to/TwitterID \nInstagram: https://RickAstley.lnk.to/InstagramID \nWebsite: https://RickAstley.lnk.to/storeID \nTikTok: https://RickAstley.lnk.to/TikTokID\n\nListen to Rick Astley:\nSpotify: https://RickAstley.lnk.to/SpotifyID \nApple Music: https://RickAstley.lnk.to/AppleMusicID \nAmazon Music: https://RickAstley.lnk.to/AmazonMusicID \nDeezer: https://RickAstley.lnk.to/DeezerID \n\nLyrics:\nWe\u2019re no strangers to love\nYou know the rules and so do I\nA full commitment\u2019s what I\u2019m thinking of\nYou wouldn\u2019t get this from any other guy\n\nI just wanna tell you how I\u2019m feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWe\u2019ve known each other for so long\nYour heart\u2019s been aching but you\u2019re too shy to say it\nInside we both know what\u2019s been going on\nWe know the game and we\u2019re gonna play it\n\nAnd if you ask me how I\u2019m feeling\nDon\u2019t tell me you\u2019re too blind to see\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\n#RickAstley #NeverGonnaGiveYouUp #WheneverYouNeedSomebody #OfficialMusicVideo",
    "uploader": "Rick Astley",
    "uploader_id": "@RickAstleyYT",
    "uploader_url": "http://www.youtube.com/@RickAstleyYT",
    "channel_id": "UCuAXFkgsw1L7xaCfnd5JJOw",
    "channel_url": "https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw",
    "duration": 212,
    "view_count": 1405669322,
    "average_rating": null,
    "age_limit": 0,
    "webpage_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "categories": [
        "Music"
    ],
    "tags": [
        "rick astley",
        "Never Gonna Give You Up",
        "nggyu",
        "never gonna give you up lyrics",
        "rick rolled",
        "Rick Roll",
        "rick astley official",
        "rickrolled",
        "Fortnite song",
        "Fortnite event",
        "Fortnite dance",
        "fortnite never gonna give you up",
        "rick roll",
        "rickrolling",
        "rick rolling",
        "never gonna give you up",
        "80s music",
        "rick astley new",
        "animated video",
        "rickroll",
        "meme songs",
        "never gonna give u up lyrics",
        "Rick Astley 2022",
        "never gonna let you down",
        "animated",
        "rick rolls 2022",
        "never gonna give you up karaoke"
    ],
    "playable_in_embed": true,
    "live_status": "not_live",
    "release_timestamp": null,
    "_format_sort_fields": [
        "quality",
        "res",
        "fps",
        "hdr:12",
        "source",
        "vcodec:vp9.2",
        "channels",
        "acodec",
        "lang",
        "proto"
    ],
    "automatic_captions": {
        "af": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=af&fmt=json3",
                "name": "Afrikaans"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=ak&fmt=vtt",
                "name": "Akan"
            }
        ],
        "sq": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=sq&fmt=json3",
                "name": "Albanian"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=sq&fmt=srv1",
                "name": "Albanian"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604107&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=064337D990FACE9CF868578961938A2B10A175DC.9F28696FF1CFCC863616AE897F3253BA8FB6F135&key=yt8&kind=asr&lang=en&tlang=sq&fmt=vtt",
                "name": "Albanian"
            }
        ],
                    {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=xh&fmt=vtt",
                "name": "Xhosa"
            }
        ],
        "yi": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=json3",
                "name": "Yiddish"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=srv1",
                "name": "Yiddish"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=srv2",
                "name": "Yiddish"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=srv3",
                "name": "Yiddish"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=ttml",
                "name": "Yiddish"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yi&fmt=vtt",
                "name": "Yiddish"
            }
        ],
        "yo": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=json3",
                "name": "Yoruba"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=srv1",
                "name": "Yoruba"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=srv2",
                "name": "Yoruba"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=srv3",
                "name": "Yoruba"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=ttml",
                "name": "Yoruba"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=yo&fmt=vtt",
                "name": "Yoruba"
            }
        ],
        "zu": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=json3",
                "name": "Zulu"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=srv1",
                "name": "Zulu"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=srv2",
                "name": "Zulu"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=srv3",
                "name": "Zulu"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=ttml",
                "name": "Zulu"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686604822&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=ADE689B89E8E1B8F375037F427B3A4E698768FE3.9F78F31186D2CCCA608FC669862263553BF233A2&key=yt8&kind=asr&lang=en&tlang=zu&fmt=vtt",
                "name": "Zulu"
            }
        ]
    },
    "subtitles": {},
    "comment_count": null,
    "chapters": null,
    "like_count": 16479557,
    "channel": "Rick Astley",
    "channel_follower_count": 3710000,
    "upload_date": "20091025",
    "availability": "public",
    "original_url": "https://youtu.be/dQw4w9WgXcQ",
    "webpage_url_basename": "watch",
    "webpage_url_domain": "youtube.com",
    "extractor": "youtube",
    "extractor_key": "Youtube",
    "playlist": null,
    "playlist_index": null,
    "display_id": "dQw4w9WgXcQ",
    "fulltitle": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
    "duration_string": "3:32",
    "is_live": false,
    "was_live": false,
    "requested_subtitles": null,
    "_has_drm": null,
    "requested_formats": [
        {
            "asr": null,
            "filesize": 55643203,
            "format_id": "248",
            "format_note": "1080p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 1080,
            "quality": 9.0,
            "has_drm": false,
            "tbr": 2099.347,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D",
            "width": 1920,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 2099.347,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=10485760-20971519"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=20971520-31457279"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=31457280-41943039"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=41943040-52428799"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOe6cmnoimhw5yzQdwVpNMX7cETvn9tsbJl_6nP9-6odAiAYUURnondgXkA9Rfx3PABAXs4O2tL4hao7E7bzkwQ3Og%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=52428800-55643203"
                }
            ],
            "container": "webm_dash",
            "resolution": "1920x1080",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.24 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "248 - 1920x1080 (1080p)"
        },
        {
            "asr": 48000,
            "filesize": 3437753,
            "format_id": "251",
            "format_note": "medium",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 3.0,
            "has_drm": false,
            "tbr": 129.689,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=251&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=3437753&dur=212.061&lmt=1674228069793936&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgQcD6YPngvU_wfvh76Cuh8oaq4_qGtxvzM_JjhwzzJCMCIH-gbOVTziJC2nYPsJPWALIL71RCIBi1YJxZDi3qkDOP&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "none",
            "acodec": "opus",
            "dynamic_range": null,
            "abr": 129.689,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686601223&ei=pymHZMD1DNTL0_wP-qq9SA&ip=96.250.56.162&id=o-AOB1sxVrDzU66oOA7GmEjo-LF503NCPwqqpyneXxlXtf&itag=251&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pcm2cms=yes&pl=16&initcwndbps=1518750&spc=qEK7B2VuX1QmY3e1lySorvWS2pCcLF8&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=3437753&dur=212.061&lmt=1674228069793936&mt=1686579243&fvip=5&keepalive=yes&fexp=24007246%2C24362685&beids=24350018&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgQcD6YPngvU_wfvh76Cuh8oaq4_qGtxvzM_JjhwzzJCMCIH-gbOVTziJC2nYPsJPWALIL71RCIBi1YJxZDi3qkDOP&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmnBQlCczaywVAWWuGDVSnUd2GiOT3aTY2I2Hjoi_-yAiB6xFISfnAIfdZU5_APB0hIb02vTiyLFRn8bjnVM15GuA%3D%3D&range=0-3437753"
                }
            ],
            "container": "webm_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.24 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "webm",
            "video_ext": "none",
            "format": "251 - audio only (medium)"
        }
    ],
    "format": "248 - 1920x1080 (1080p)+251 - audio only (medium)",
    "format_id": "248+251",
    "ext": "webm",
    "protocol": "http_dash_segments+http_dash_segments",
    "language": null,
    "format_note": "1080p+medium",
    "filesize_approx": 59080956,
    "tbr": 2229.036,
    "width": 1920,
    "height": 1080,
    "resolution": "1920x1080",
    "fps": 25,
    "dynamic_range": "SDR",
    "vcodec": "vp9",
    "vbr": 2099.347,
    "stretched_ratio": null,
    "aspect_ratio": 1.78,
    "acodec": "opus",
    "abr": 129.689,
    "asr": 48000,
    "audio_channels": 2
}
"""
mock_video_metadata_simple = """
{
    "url": "test_url", "title": "test_title", "description": "test_description",
    "uploader": "test_uploader", "upload_date": "test_date", "duration": "test_duration",
    "view_count": "test_views", "like_count": "test_likes", "dislike_count": "test_dislikes",
    "id": "test_id", "categories": "test_categories", "tags": "test_tags"
}
"""
mock_placeholder = """
"""