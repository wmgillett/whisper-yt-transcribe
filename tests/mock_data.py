#mock_data.py
# complete info_dict from a YouTube channel
mock_channel_info_dict = """
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
mock_video_mp3 = """
{}
"""
mock_video_mp4 = """
{}
"""
# simple placeholder transcription text
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
# real output from Rick Roll Video
# https://www.youtube.com/watch?v=dQw4w9WgXcQ
mock_transcribed_text_complex = '''
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
    "description": "The official video for Never Gonna Give You Up by Rick Astley",
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
'''
# simple placeholder video metadata
mock_video_metadata_simple = '''
{
	"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
	"title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
	"description": "The official video for Never Gonna Give You Up by Rick Astley",
	"channel": "Rick Astley",
	"uploader": "Rick Astley",
	"upload_date": "20091025",
	"duration": 212,
	"view_count": 1407368421,
	"like_count": 16495466,
	"id": "dQw4w9WgXcQ",
	"categories": ["Music"],
	"tags": ["rick astley", "Never Gonna Give You Up", "nggyu", "never gonna give you up lyrics", "rick rolled", "Rick Roll", "rick astley official", "rickrolled", "Fortnite song", "Fortnite event", "Fortnite dance", "fortnite never gonna give you up", "rick roll", "rickrolling", "rick rolling", "never gonna give you up", "80s music", "rick astley new", "animated video", "rickroll", "meme songs", "never gonna give u up lyrics", "Rick Astley 2022", "never gonna let you down", "animated", "rick rolls 2022", "never gonna give you up karaoke"]
}
'''
mock_playlist_metadata = '''
{
	'url': 'https://www.youtube.com/playlist?list=PLlaN88a7y2_oyxwuMg72dcUz1S5qeoJYv',
	'title': 'Covered by Rick Astley',
	'description': '',
	'channel': 'Rick Astley',
	'uploader': 'Rick Astley',
	'upload_date': None,
	'duration': None,
	'view_count': 67631,
	'like_count': None,
	'id': 'PLlaN88a7y2_oyxwuMg72dcUz1S5qeoJYv',
	'categories': None,
	'tags': []
}
'''
mock_placeholder1 = """
"""
# from Rick Roll Video
# https://www.youtube.com/watch?v=dQw4w9WgXcQ
#* note - mock_video_info_dict is a very long 2000 line string
mock_video_info_dict = '''
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
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=599&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=817805&dur=212.183&lmt=1674227828689068&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIge234iE-CY6svqxvZcBSGrUepM6wuF0GepyBtue8CRyoCIELCZXyMnF4hKd7kF_FPRyRt0EPXmJmY9UKA3fjRjL9w&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
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
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=599&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=817805&dur=212.183&lmt=1674227828689068&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIge234iE-CY6svqxvZcBSGrUepM6wuF0GepyBtue8CRyoCIELCZXyMnF4hKd7kF_FPRyRt0EPXmJmY9UKA3fjRjL9w&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-817805"
                }
            ],
            "container": "m4a_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=600&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=832823&dur=212.061&lmt=1674227828749650&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAKoBB2ftr7S_ltGeadq0wpz4gn_2kIb7y2HFQT6tDOh7AiB92LMtXt_nQwgI9Boi5KSQs2pgCCYlvCisktvKfVx8NA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
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
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=600&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=832823&dur=212.061&lmt=1674227828749650&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAKoBB2ftr7S_ltGeadq0wpz4gn_2kIb7y2HFQT6tDOh7AiB92LMtXt_nQwgI9Boi5KSQs2pgCCYlvCisktvKfVx8NA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-832823"
                }
            ],
            "container": "webm_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=139&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=1294944&dur=212.183&lmt=1674228035408340&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOqEimhgBAV8p4mhYKnX0lbupDzw1EQkoGl4rvNPyvdZAiBcGWUF462XTX7EtrwTyo3PUxfJpWDDV79hPZuq1q3IzQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
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
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=139&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=1294944&dur=212.183&lmt=1674228035408340&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOqEimhgBAV8p4mhYKnX0lbupDzw1EQkoGl4rvNPyvdZAiBcGWUF462XTX7EtrwTyo3PUxfJpWDDV79hPZuq1q3IzQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-1294944"
                }
            ],
            "container": "m4a_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "m4a",
            "video_ext": "none",
            "format": "139 - audio only (low)"
        },
        {
            "asr": 48000,
            "filesize": 1232413,
            "format_id": "249",
            "format_note": "low",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 2.0,
            "has_drm": false,
            "tbr": 46.492,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=249&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=1232413&dur=212.061&lmt=1674228035778779&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIgk_5DYp7xM-p7wDpYpohF9qWfGXmo0P471XF2SbeQCAiEA2oc4mq2SEYY88vChczvKL-u0lb4YR19c3fNmkAshAuc%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "none",
            "acodec": "opus",
            "dynamic_range": null,
            "abr": 46.492,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=249&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=1232413&dur=212.061&lmt=1674228035778779&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIgk_5DYp7xM-p7wDpYpohF9qWfGXmo0P471XF2SbeQCAiEA2oc4mq2SEYY88vChczvKL-u0lb4YR19c3fNmkAshAuc%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-1232413"
                }
            ],
            "container": "webm_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "webm",
            "video_ext": "none",
            "format": "249 - audio only (low)"
        },
        {
            "asr": 48000,
            "filesize": 1630086,
            "format_id": "250",
            "format_note": "low",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 2.0,
            "has_drm": false,
            "tbr": 61.494,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=250&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=1630086&dur=212.061&lmt=1674228035073530&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAPs1Z8RLQBEOyORYcmN5qMXC151qtZ-YtKWrW_PA49JUAiEArt6XnorJD8FcduModj6tHvOVMtT5V8o-WHYmFI5WkGQ%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "none",
            "acodec": "opus",
            "dynamic_range": null,
            "abr": 61.494,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=250&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=1630086&dur=212.061&lmt=1674228035073530&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAPs1Z8RLQBEOyORYcmN5qMXC151qtZ-YtKWrW_PA49JUAiEArt6XnorJD8FcduModj6tHvOVMtT5V8o-WHYmFI5WkGQ%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-1630086"
                }
            ],
            "container": "webm_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "webm",
            "video_ext": "none",
            "format": "250 - audio only (low)"
        },
        {
            "asr": 44100,
            "filesize": 3433514,
            "format_id": "140",
            "format_note": "medium",
            "source_preference": -1,
            "fps": null,
            "audio_channels": 2,
            "height": null,
            "quality": 3.0,
            "has_drm": false,
            "tbr": 129.51,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=140&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=3433514&dur=212.091&lmt=1674228035651780&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAJ95ucY3bGui-l2t4rMKeWN1D3OrQOXP9PRMgT36QC0cAiEAl6RCF6IM--RFKk0kN7PUMs-8MToK1hl4c_VMcjU4SNM%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": null,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "m4a",
            "vcodec": "none",
            "acodec": "mp4a.40.2",
            "dynamic_range": null,
            "abr": 129.51,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=140&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fmp4&gir=yes&clen=3433514&dur=212.091&lmt=1674228035651780&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAJ95ucY3bGui-l2t4rMKeWN1D3OrQOXP9PRMgT36QC0cAiEAl6RCF6IM--RFKk0kN7PUMs-8MToK1hl4c_VMcjU4SNM%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-3433514"
                }
            ],
            "container": "m4a_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "m4a",
            "video_ext": "none",
            "format": "140 - audio only (medium)"
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
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=251&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=3437753&dur=212.061&lmt=1674228069793936&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAI8dC2RD4d8oGuz13vWKzwnU2cdCKV2czChgl6c8l0KBAiEAnbJomc_cIebFApvYCrQvEyzytuWWLdwKs6MWObfe-no%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
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
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=251&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=3437753&dur=212.061&lmt=1674228069793936&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAI8dC2RD4d8oGuz13vWKzwnU2cdCKV2czChgl6c8l0KBAiEAnbJomc_cIebFApvYCrQvEyzytuWWLdwKs6MWObfe-no%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-3437753"
                }
            ],
            "container": "webm_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "audio_ext": "webm",
            "video_ext": "none",
            "format": "251 - audio only (medium)"
        },
        {
            "asr": 22050,
            "filesize": 2089080,
            "format_id": "17",
            "format_note": "144p",
            "source_preference": -1,
            "fps": 6,
            "audio_channels": 1,
            "height": 144,
            "quality": 0.0,
            "has_drm": false,
            "tbr": 78.782,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=17&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2F3gpp&gir=yes&clen=2089080&dur=212.137&lmt=1674230576328521&mt=1686916877&fvip=5&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAP342fHEWgjiu6e_a8V0CS-XjJHExZ9O73_b7zsqK8-1AiAUbsi_mSFj-9ef8I9P6-SnjtH_c6_Itq9O3GugX2zu1w%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 176,
            "language": null,
            "language_preference": -1,
            "preference": -2,
            "ext": "3gp",
            "vcodec": "mp4v.20.3",
            "acodec": "mp4a.40.2",
            "dynamic_range": "SDR",
            "protocol": "https",
            "resolution": "176x144",
            "aspect_ratio": 1.22,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "3gp",
            "audio_ext": "none",
            "vbr": 78.782,
            "abr": 0.0,
            "format": "17 - 176x144 (144p)"
        },
        {
            "asr": null,
            "filesize": 849009,
            "format_id": "597",
            "format_note": "144p",
            "source_preference": -1,
            "fps": 13,
            "audio_channels": null,
            "height": 144,
            "quality": 0.0,
            "has_drm": false,
            "tbr": 32.025,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=597&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=849009&dur=212.080&lmt=1674230524982416&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453C434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAMDrfwyYBvLmkjz9gM4aIP73zz3s1BNlJtCLnNvmQbcDAiEAqRMl12MJ0Bd-SskiJuTXRAMALT5IBmC6Dul2pggZZPQ%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 256,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.4d400b",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 32.025,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=597&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=849009&dur=212.080&lmt=1674230524982416&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453C434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAMDrfwyYBvLmkjz9gM4aIP73zz3s1BNlJtCLnNvmQbcDAiEAqRMl12MJ0Bd-SskiJuTXRAMALT5IBmC6Dul2pggZZPQ%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-849009"
                }
            ],
            "container": "mp4_dash",
            "resolution": "256x144",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "597 - 256x144 (144p)"
        },
        {
            "asr": null,
            "filesize": 646728,
            "format_id": "598",
            "format_note": "144p",
            "source_preference": -1,
            "fps": 13,
            "audio_channels": null,
            "height": 144,
            "quality": 0.0,
            "has_drm": false,
            "tbr": 24.395,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=598&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=646728&dur=212.080&lmt=1674230542133060&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453C434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgSQipZsQARVVXZ34n4sHrcHRAjwj68bepQMCzFbrLz0ACIGt8ZE3eGZTD2UXqoufUmsizv30k_UxvDJffAjX_X-T-&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 256,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 24.395,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=598&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=646728&dur=212.080&lmt=1674230542133060&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453C434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgSQipZsQARVVXZ34n4sHrcHRAjwj68bepQMCzFbrLz0ACIGt8ZE3eGZTD2UXqoufUmsizv30k_UxvDJffAjX_X-T-&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-646728"
                }
            ],
            "container": "webm_dash",
            "resolution": "256x144",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "598 - 256x144 (144p)"
        },
        {
            "asr": null,
            "filesize": 1502336,
            "format_id": "394",
            "format_note": "144p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 144,
            "quality": 0.0,
            "has_drm": false,
            "tbr": 56.681,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=394&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=1502336&dur=212.040&lmt=1674230544069590&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgeS76_qkzKhHBP1VswDBRTQN_a1dp8Biy9oiWQfLrT7MCIH_Q4WH_WEowYntHnDi2Vr2N-fbFxvIDeYVGvuXAksN8&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 256,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "av01.0.00M.08",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 56.681,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=394&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=1502336&dur=212.040&lmt=1674230544069590&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgeS76_qkzKhHBP1VswDBRTQN_a1dp8Biy9oiWQfLrT7MCIH_Q4WH_WEowYntHnDi2Vr2N-fbFxvIDeYVGvuXAksN8&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-1502336"
                }
            ],
            "container": "mp4_dash",
            "resolution": "256x144",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "394 - 256x144 (144p)"
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
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=160&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=1859270&dur=212.040&lmt=1674233649874257&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhALKrLcgiO6cOe8qMrdvSbUflXHW1-SoHFBIVxEZhxiMYAiBr0hwngT34kbhPYu7fnXvGYWtbJSQ4t38TY6UXUoBHQw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
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
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=160&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=1859270&dur=212.040&lmt=1674233649874257&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhALKrLcgiO6cOe8qMrdvSbUflXHW1-SoHFBIVxEZhxiMYAiBr0hwngT34kbhPYu7fnXvGYWtbJSQ4t38TY6UXUoBHQw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-1859270"
                }
            ],
            "container": "mp4_dash",
            "resolution": "256x144",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=278&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=2157715&dur=212.040&lmt=1674240806546279&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMR1uC5gZoA_LnNP1PyCSXiOT_lGGP48reo1lUCkyoSrAiBMWV6O3wbBqxN7dOXMNMsLbfApM-xvgGiC8Rw7aNuyag%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
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
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=278&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=2157715&dur=212.040&lmt=1674240806546279&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMR1uC5gZoA_LnNP1PyCSXiOT_lGGP48reo1lUCkyoSrAiBMWV6O3wbBqxN7dOXMNMsLbfApM-xvgGiC8Rw7aNuyag%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-2157715"
                }
            ],
            "container": "webm_dash",
            "resolution": "256x144",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
            "filesize": 3198834,
            "format_id": "395",
            "format_note": "240p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 240,
            "quality": 5.0,
            "has_drm": false,
            "tbr": 120.687,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=395&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=3198834&dur=212.040&lmt=1674230758960693&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgHEkHih__nIC9ufceJdG59aS-XGnwx39U4trwi3rCNwsCIQDm9hMIaCN0KuRKKP5464uG2WUHJ3avwiBYRpWj3Ioy5w%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 426,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "av01.0.00M.08",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 120.687,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=395&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=3198834&dur=212.040&lmt=1674230758960693&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgHEkHih__nIC9ufceJdG59aS-XGnwx39U4trwi3rCNwsCIQDm9hMIaCN0KuRKKP5464uG2WUHJ3avwiBYRpWj3Ioy5w%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-3198834"
                }
            ],
            "container": "mp4_dash",
            "resolution": "426x240",
            "aspect_ratio": 1.77,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "395 - 426x240 (240p)"
        },
        {
            "asr": null,
            "filesize": 3013651,
            "format_id": "133",
            "format_note": "240p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 240,
            "quality": 5.0,
            "has_drm": false,
            "tbr": 113.701,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=133&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=3013651&dur=212.040&lmt=1674233650420154&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAIohieVTCzZ8reMv8KJN0gqZG4DgUlQkK6btLrOjAXwCAiAHXVjNTFICzLuMpTKlpPpzNWoeWdSRJzRQovgM_eFzEg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 426,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.4d4015",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 113.701,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=133&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=3013651&dur=212.040&lmt=1674233650420154&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAIohieVTCzZ8reMv8KJN0gqZG4DgUlQkK6btLrOjAXwCAiAHXVjNTFICzLuMpTKlpPpzNWoeWdSRJzRQovgM_eFzEg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-3013651"
                }
            ],
            "container": "mp4_dash",
            "resolution": "426x240",
            "aspect_ratio": 1.77,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "133 - 426x240 (240p)"
        },
        {
            "asr": null,
            "filesize": 3896369,
            "format_id": "242",
            "format_note": "240p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 240,
            "quality": 5.0,
            "has_drm": false,
            "tbr": 147.005,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=242&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=3896369&dur=212.040&lmt=1674240781687118&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgIser1FUITfFxLwuQ8ZuyF3wgSD_BHo3Z0hlXQPDh3psCIAN62qUDDUyvx-_KHBnEXmzBBVX0qxhvlRbk9neh6DNY&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 426,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 147.005,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=242&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=3896369&dur=212.040&lmt=1674240781687118&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgIser1FUITfFxLwuQ8ZuyF3wgSD_BHo3Z0hlXQPDh3psCIAN62qUDDUyvx-_KHBnEXmzBBVX0qxhvlRbk9neh6DNY&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-3896369"
                }
            ],
            "container": "webm_dash",
            "resolution": "426x240",
            "aspect_ratio": 1.77,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "242 - 426x240 (240p)"
        },
        {
            "asr": null,
            "filesize": 5953258,
            "format_id": "396",
            "format_note": "360p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 360,
            "quality": 6.0,
            "has_drm": false,
            "tbr": 224.608,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=396&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=5953258&dur=212.040&lmt=1674230525337110&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgSEIOV0hCBKifvysLP9g6ndNp7XB7Fk4s3l_yKOH1SnoCIQCUHglAhbE_E1qYndQ0oLhggztrkhYqDAZBmlmCE4rSgg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 640,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "av01.0.01M.08",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 224.608,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=396&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=5953258&dur=212.040&lmt=1674230525337110&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgSEIOV0hCBKifvysLP9g6ndNp7XB7Fk4s3l_yKOH1SnoCIQCUHglAhbE_E1qYndQ0oLhggztrkhYqDAZBmlmCE4rSgg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-5953258"
                }
            ],
            "container": "mp4_dash",
            "resolution": "640x360",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "396 - 640x360 (360p)"
        },
        {
            "asr": null,
            "filesize": 5661008,
            "format_id": "134",
            "format_note": "360p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 360,
            "quality": 6.0,
            "has_drm": false,
            "tbr": 213.582,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=134&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=5661008&dur=212.040&lmt=1674233649463738&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAKi5ocl0lgvKKUc-QZvw1VVt4buVfWNt2iLdXe7yClRpAiEArn7_0HwYMX-YZgbhPk67GVxdo4t9B7OMXjCEWaGyqvk%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 640,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.4d401e",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 213.582,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=134&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=5661008&dur=212.040&lmt=1674233649463738&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAKi5ocl0lgvKKUc-QZvw1VVt4buVfWNt2iLdXe7yClRpAiEArn7_0HwYMX-YZgbhPk67GVxdo4t9B7OMXjCEWaGyqvk%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-5661008"
                }
            ],
            "container": "mp4_dash",
            "resolution": "640x360",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "134 - 640x360 (360p)"
        },
        {
            "asr": 44100,
            "filesize": null,
            "format_id": "18",
            "format_note": "360p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": 2,
            "height": 360,
            "quality": 6.0,
            "has_drm": false,
            "tbr": 342.654,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=18&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=212.091&lmt=1674233743350828&mt=1686916877&fvip=5&fexp=24007246%2C24363392&c=ANDROID&txp=4530434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAJo0moUxTsytOKGkzdS2xYSbsRHtoBth6qnqzHFhX-NiAiEAy4nBH0SzfEGeIxG8XFebd5eGNrkMiDWXSgHFYRSh_2w%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 640,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.42001E",
            "acodec": "mp4a.40.2",
            "dynamic_range": "SDR",
            "protocol": "https",
            "resolution": "640x360",
            "aspect_ratio": 1.78,
            "filesize_approx": 9298258,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "vbr": 342.654,
            "abr": 0.0,
            "format": "18 - 640x360 (360p)"
        },
        {
            "asr": null,
            "filesize": 6839345,
            "format_id": "243",
            "format_note": "360p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 360,
            "quality": 6.0,
            "has_drm": false,
            "tbr": 258.039,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=243&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=6839345&dur=212.040&lmt=1674240781766819&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAPpOM1bOl2UQFenAzWvFWOrswt-3xHVkzbKxSL__lZXKAiABQTfkoYB1mwUhEUVCSWlaJWasC8x7MqjOEQquKYKYUQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 640,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 258.039,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=243&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=6839345&dur=212.040&lmt=1674240781766819&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAPpOM1bOl2UQFenAzWvFWOrswt-3xHVkzbKxSL__lZXKAiABQTfkoYB1mwUhEUVCSWlaJWasC8x7MqjOEQquKYKYUQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-6839345"
                }
            ],
            "container": "webm_dash",
            "resolution": "640x360",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "243 - 640x360 (360p)"
        },
        {
            "asr": null,
            "filesize": 10609264,
            "format_id": "397",
            "format_note": "480p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 480,
            "quality": 7.0,
            "has_drm": false,
            "tbr": 400.274,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=397&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=10609264&dur=212.040&lmt=1674230502296592&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhALelXjKBYvFBr_EVJKZ_kkyy022hurRrPIv2pc6tvO95AiEAzzu7ib_v7FHcVxlIdhetfDcyM2U6xJO9C-JY4aftLtA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 854,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "av01.0.04M.08",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 400.274,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=397&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=10609264&dur=212.040&lmt=1674230502296592&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhALelXjKBYvFBr_EVJKZ_kkyy022hurRrPIv2pc6tvO95AiEAzzu7ib_v7FHcVxlIdhetfDcyM2U6xJO9C-JY4aftLtA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=397&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=10609264&dur=212.040&lmt=1674230502296592&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhALelXjKBYvFBr_EVJKZ_kkyy022hurRrPIv2pc6tvO95AiEAzzu7ib_v7FHcVxlIdhetfDcyM2U6xJO9C-JY4aftLtA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=10485760-10609264"
                }
            ],
            "container": "mp4_dash",
            "resolution": "854x480",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "397 - 854x480 (480p)"
        },
        {
            "asr": null,
            "filesize": 8648011,
            "format_id": "135",
            "format_note": "480p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 480,
            "quality": 7.0,
            "has_drm": false,
            "tbr": 326.278,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=135&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=8648011&dur=212.040&lmt=1674233685333989&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgI4g4hSLLaeypgy9UN63I6cL2ZdyW26-mhQCDuuwYpYACIQCoKYIpI0GZyLhfLCZbvFdASbkZ6WJBSDda7BNaQ0jLzA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 854,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.4d401e",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 326.278,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=135&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=8648011&dur=212.040&lmt=1674233685333989&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgI4g4hSLLaeypgy9UN63I6cL2ZdyW26-mhQCDuuwYpYACIQCoKYIpI0GZyLhfLCZbvFdASbkZ6WJBSDda7BNaQ0jLzA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-8648011"
                }
            ],
            "container": "mp4_dash",
            "resolution": "854x480",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "135 - 854x480 (480p)"
        },
        {
            "asr": null,
            "filesize": 9767682,
            "format_id": "244",
            "format_note": "480p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 480,
            "quality": 7.0,
            "has_drm": false,
            "tbr": 368.522,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=244&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=9767682&dur=212.040&lmt=1674240828512305&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhANBFAbJF0ZFUcnK-ilD-WAEUkR4yliP_cng-lxhoJNZFAiBsbOIgTvtHEE1rh4xjwibXF_rHr2IeZdThXQrWfUy8Vw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 854,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 368.522,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=244&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=9767682&dur=212.040&lmt=1674240828512305&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhANBFAbJF0ZFUcnK-ilD-WAEUkR4yliP_cng-lxhoJNZFAiBsbOIgTvtHEE1rh4xjwibXF_rHr2IeZdThXQrWfUy8Vw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-9767682"
                }
            ],
            "container": "webm_dash",
            "resolution": "854x480",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "244 - 854x480 (480p)"
        },
        {
            "asr": 44100,
            "filesize": null,
            "format_id": "22",
            "format_note": "720p",
            "source_preference": -5,
            "fps": 25,
            "audio_channels": 2,
            "height": 720,
            "quality": 8.0,
            "has_drm": false,
            "tbr": 755.309,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=22&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=212.091&lmt=1674233742818000&mt=1686916877&fvip=5&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAKfENDpw8senq1QHjAG2qZPy8QXHfaJWkmR7bvWGKnFgAiBofbVAH1KaE8QZWXl2etDupFeDgwZEeq7a8KEU7K514w%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 1280,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.64001F",
            "acodec": "mp4a.40.2",
            "dynamic_range": "SDR",
            "protocol": "https",
            "resolution": "1280x720",
            "aspect_ratio": 1.78,
            "filesize_approx": 20496065,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "vbr": 755.309,
            "abr": 0.0,
            "format": "22 - 1280x720 (720p)"
        },
        {
            "asr": null,
            "filesize": 19086092,
            "format_id": "398",
            "format_note": "720p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 720,
            "quality": 8.0,
            "has_drm": false,
            "tbr": 720.094,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=398&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=19086092&dur=212.040&lmt=1674231669611955&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgQAFvoSQa7il9pQI0x7IaS9oBjhkhD_tMVdW9yB8LGtgCIGkrEzjAd05GHwvCT1a9xDtSpXKN7J61CzcJD5k7k6kk&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 1280,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "av01.0.05M.08",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 720.094,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=398&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=19086092&dur=212.040&lmt=1674231669611955&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgQAFvoSQa7il9pQI0x7IaS9oBjhkhD_tMVdW9yB8LGtgCIGkrEzjAd05GHwvCT1a9xDtSpXKN7J61CzcJD5k7k6kk&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=398&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=19086092&dur=212.040&lmt=1674231669611955&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgQAFvoSQa7il9pQI0x7IaS9oBjhkhD_tMVdW9yB8LGtgCIGkrEzjAd05GHwvCT1a9xDtSpXKN7J61CzcJD5k7k6kk&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=10485760-19086092"
                }
            ],
            "container": "mp4_dash",
            "resolution": "1280x720",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "398 - 1280x720 (720p)"
        },
        {
            "asr": null,
            "filesize": 16598002,
            "format_id": "136",
            "format_note": "720p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 720,
            "quality": 8.0,
            "has_drm": false,
            "tbr": 626.221,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=136&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=16598002&dur=212.040&lmt=1674233649417590&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgW8VVEZ1wjd0SrRKpEOGA70zYx3RU-zXlO4zwCKZxVA8CIFEyzzkr-VoM4rURK1ZCL6mQkK2pyqhT5nWaOBYR57-r&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 1280,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.4d401f",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 626.221,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=136&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=16598002&dur=212.040&lmt=1674233649417590&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgW8VVEZ1wjd0SrRKpEOGA70zYx3RU-zXlO4zwCKZxVA8CIFEyzzkr-VoM4rURK1ZCL6mQkK2pyqhT5nWaOBYR57-r&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=136&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=16598002&dur=212.040&lmt=1674233649417590&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgW8VVEZ1wjd0SrRKpEOGA70zYx3RU-zXlO4zwCKZxVA8CIFEyzzkr-VoM4rURK1ZCL6mQkK2pyqhT5nWaOBYR57-r&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=10485760-16598002"
                }
            ],
            "container": "mp4_dash",
            "resolution": "1280x720",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "136 - 1280x720 (720p)"
        },
        {
            "asr": null,
            "filesize": 17149834,
            "format_id": "247",
            "format_note": "720p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 720,
            "quality": 8.0,
            "has_drm": false,
            "tbr": 647.041,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=247&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=17149834&dur=212.040&lmt=1674240770945966&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgO_WfG5ag84GQrm8PAc_IL-f2vfW6SAgZ2BiU38724cYCIBlgHs68TSxvGB_opkceoIPXW10PptzcMC90KMK4o7xy&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 1280,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "webm",
            "vcodec": "vp9",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 647.041,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=247&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=17149834&dur=212.040&lmt=1674240770945966&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgO_WfG5ag84GQrm8PAc_IL-f2vfW6SAgZ2BiU38724cYCIBlgHs68TSxvGB_opkceoIPXW10PptzcMC90KMK4o7xy&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=247&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=17149834&dur=212.040&lmt=1674240770945966&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgO_WfG5ag84GQrm8PAc_IL-f2vfW6SAgZ2BiU38724cYCIBlgHs68TSxvGB_opkceoIPXW10PptzcMC90KMK4o7xy&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=10485760-17149834"
                }
            ],
            "container": "webm_dash",
            "resolution": "1280x720",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "webm",
            "audio_ext": "none",
            "format": "247 - 1280x720 (720p)"
        },
        {
            "asr": null,
            "filesize": 34279919,
            "format_id": "399",
            "format_note": "1080p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 1080,
            "quality": 9.0,
            "has_drm": false,
            "tbr": 1293.337,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=399&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=34279919&dur=212.040&lmt=1674232705915481&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgHXfBrRzyEpZJY3_-te6EmrPF7nolIdXmQaQnDON-6hACIQDdflKndYxoqqVY917sc6ep0-whyeSvnC7L2YAWP11B_Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 1920,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "av01.0.08M.08",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 1293.337,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=399&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=34279919&dur=212.040&lmt=1674232705915481&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgHXfBrRzyEpZJY3_-te6EmrPF7nolIdXmQaQnDON-6hACIQDdflKndYxoqqVY917sc6ep0-whyeSvnC7L2YAWP11B_Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=399&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=34279919&dur=212.040&lmt=1674232705915481&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgHXfBrRzyEpZJY3_-te6EmrPF7nolIdXmQaQnDON-6hACIQDdflKndYxoqqVY917sc6ep0-whyeSvnC7L2YAWP11B_Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=10485760-20971519"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=399&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=34279919&dur=212.040&lmt=1674232705915481&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgHXfBrRzyEpZJY3_-te6EmrPF7nolIdXmQaQnDON-6hACIQDdflKndYxoqqVY917sc6ep0-whyeSvnC7L2YAWP11B_Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=20971520-31457279"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=399&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=34279919&dur=212.040&lmt=1674232705915481&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4537434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgHXfBrRzyEpZJY3_-te6EmrPF7nolIdXmQaQnDON-6hACIQDdflKndYxoqqVY917sc6ep0-whyeSvnC7L2YAWP11B_Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=31457280-34279919"
                }
            ],
            "container": "mp4_dash",
            "resolution": "1920x1080",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "399 - 1920x1080 (1080p)"
        },
        {
            "asr": null,
            "filesize": 78662712,
            "format_id": "137",
            "format_note": "1080p",
            "source_preference": -1,
            "fps": 25,
            "audio_channels": null,
            "height": 1080,
            "quality": 9.0,
            "has_drm": false,
            "tbr": 2967.844,
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=137&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=78662712&dur=212.040&lmt=1674234004910329&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgC78Vw5JqFVfQq9RXCxwbG10Wf3GKqCVN8hxcOnJbcpUCIFp9_MkADP6LX6LgQhVwceq54wSteSh5LFAPGcWG8SvJ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
            "width": 1920,
            "language": null,
            "language_preference": -1,
            "preference": null,
            "ext": "mp4",
            "vcodec": "avc1.640028",
            "acodec": "none",
            "dynamic_range": "SDR",
            "vbr": 2967.844,
            "protocol": "http_dash_segments",
            "fragments": [
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=137&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=78662712&dur=212.040&lmt=1674234004910329&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgC78Vw5JqFVfQq9RXCxwbG10Wf3GKqCVN8hxcOnJbcpUCIFp9_MkADP6LX6LgQhVwceq54wSteSh5LFAPGcWG8SvJ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=137&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=78662712&dur=212.040&lmt=1674234004910329&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgC78Vw5JqFVfQq9RXCxwbG10Wf3GKqCVN8hxcOnJbcpUCIFp9_MkADP6LX6LgQhVwceq54wSteSh5LFAPGcWG8SvJ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=10485760-20971519"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=137&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=78662712&dur=212.040&lmt=1674234004910329&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgC78Vw5JqFVfQq9RXCxwbG10Wf3GKqCVN8hxcOnJbcpUCIFp9_MkADP6LX6LgQhVwceq54wSteSh5LFAPGcWG8SvJ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=20971520-31457279"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=137&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=78662712&dur=212.040&lmt=1674234004910329&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgC78Vw5JqFVfQq9RXCxwbG10Wf3GKqCVN8hxcOnJbcpUCIFp9_MkADP6LX6LgQhVwceq54wSteSh5LFAPGcWG8SvJ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=31457280-41943039"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=137&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=78662712&dur=212.040&lmt=1674234004910329&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgC78Vw5JqFVfQq9RXCxwbG10Wf3GKqCVN8hxcOnJbcpUCIFp9_MkADP6LX6LgQhVwceq54wSteSh5LFAPGcWG8SvJ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=41943040-52428799"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=137&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=78662712&dur=212.040&lmt=1674234004910329&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgC78Vw5JqFVfQq9RXCxwbG10Wf3GKqCVN8hxcOnJbcpUCIFp9_MkADP6LX6LgQhVwceq54wSteSh5LFAPGcWG8SvJ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=52428800-62914559"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=137&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=78662712&dur=212.040&lmt=1674234004910329&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgC78Vw5JqFVfQq9RXCxwbG10Wf3GKqCVN8hxcOnJbcpUCIFp9_MkADP6LX6LgQhVwceq54wSteSh5LFAPGcWG8SvJ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=62914560-73400319"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=137&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fmp4&gir=yes&clen=78662712&dur=212.040&lmt=1674234004910329&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgC78Vw5JqFVfQq9RXCxwbG10Wf3GKqCVN8hxcOnJbcpUCIFp9_MkADP6LX6LgQhVwceq54wSteSh5LFAPGcWG8SvJ&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=73400320-78662712"
                }
            ],
            "container": "mp4_dash",
            "resolution": "1920x1080",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate"
            },
            "video_ext": "mp4",
            "audio_ext": "none",
            "format": "137 - 1920x1080 (1080p)"
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
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
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
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=10485760-20971519"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=20971520-31457279"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=31457280-41943039"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=41943040-52428799"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=52428800-55643203"
                }
            ],
            "container": "webm_dash",
            "resolution": "1920x1080",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/2.jpg",
            "preference": -35,
            "id": "2"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/2.webp",
            "preference": -34,
            "id": "3"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/1.jpg",
            "preference": -33,
            "id": "4"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/1.webp",
            "preference": -32,
            "id": "5"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/mq3.jpg",
            "preference": -31,
            "id": "6"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/mq3.webp",
            "preference": -30,
            "id": "7"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/mq2.jpg",
            "preference": -29,
            "id": "8"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/mq2.webp",
            "preference": -28,
            "id": "9"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/mq1.jpg",
            "preference": -27,
            "id": "10"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/mq1.webp",
            "preference": -26,
            "id": "11"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hq3.jpg",
            "preference": -25,
            "id": "12"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/hq3.webp",
            "preference": -24,
            "id": "13"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hq2.jpg",
            "preference": -23,
            "id": "14"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/hq2.webp",
            "preference": -22,
            "id": "15"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hq1.jpg",
            "preference": -21,
            "id": "16"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/hq1.webp",
            "preference": -20,
            "id": "17"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/sd3.jpg",
            "preference": -19,
            "id": "18"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/sd3.webp",
            "preference": -18,
            "id": "19"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/sd2.jpg",
            "preference": -17,
            "id": "20"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/sd2.webp",
            "preference": -16,
            "id": "21"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/sd1.jpg",
            "preference": -15,
            "id": "22"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/sd1.webp",
            "preference": -14,
            "id": "23"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/default.jpg",
            "preference": -13,
            "id": "24"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/default.webp",
            "height": 90,
            "width": 120,
            "preference": -12,
            "id": "25",
            "resolution": "120x90"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/mqdefault.jpg",
            "preference": -11,
            "id": "26"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/mqdefault.webp",
            "height": 180,
            "width": 320,
            "preference": -10,
            "id": "27",
            "resolution": "320x180"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/0.jpg",
            "preference": -9,
            "id": "28"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/0.webp",
            "preference": -8,
            "id": "29"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
            "preference": -7,
            "id": "30"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLDd2KtelLHaNSXrI9_5K-NvTscKNw",
            "height": 94,
            "width": 168,
            "preference": -7,
            "id": "31",
            "resolution": "168x94"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLBUpEOOWUXWkNyijQuZ4UPzp2BE-w",
            "height": 110,
            "width": 196,
            "preference": -7,
            "id": "32",
            "resolution": "196x110"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBCyhr8AqpJ1SxKVU6SyK5ODJ_IpA",
            "height": 138,
            "width": 246,
            "preference": -7,
            "id": "33",
            "resolution": "246x138"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB_p0PncTtkrhaNDZtntrE3gKkoYw",
            "height": 188,
            "width": 336,
            "preference": -7,
            "id": "34",
            "resolution": "336x188"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/hqdefault.webp",
            "height": 360,
            "width": 480,
            "preference": -6,
            "id": "35",
            "resolution": "480x360"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/sddefault.jpg",
            "preference": -5,
            "id": "36"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/sddefault.webp",
            "height": 480,
            "width": 640,
            "preference": -4,
            "id": "37",
            "resolution": "640x480"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hq720.jpg",
            "preference": -3,
            "id": "38"
        },
        {
            "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/hq720.webp",
            "preference": -2,
            "id": "39"
        },
        {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg",
            "height": 720,
            "width": 1280,
            "preference": -1,
            "id": "40",
            "resolution": "1280x720"
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
    "description": "The official video for Never Gonna Give You Up by Rick Astley",
    "uploader": "Rick Astley",
    "uploader_id": "@RickAstleyYT",
    "uploader_url": "http://www.youtube.com/@RickAstleyYT",
    "channel_id": "UCuAXFkgsw1L7xaCfnd5JJOw",
    "channel_url": "https://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw",
    "duration": 212,
    "view_count": 1407301320,
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
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=af&fmt=json3",
                "name": "Afrikaans"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=af&fmt=srv1",
                "name": "Afrikaans"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=af&fmt=srv2",
                "name": "Afrikaans"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=af&fmt=srv3",
                "name": "Afrikaans"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=af&fmt=ttml",
                "name": "Afrikaans"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=af&fmt=vtt",
                "name": "Afrikaans"
            }
        ],
        "ak": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=ak&fmt=json3",
                "name": "Akan"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=ak&fmt=srv1",
                "name": "Akan"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=ak&fmt=srv2",
                "name": "Akan"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=ak&fmt=srv3",
                "name": "Akan"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=ak&fmt=ttml",
                "name": "Akan"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=ak&fmt=vtt",
                "name": "Akan"
            }
        ],
        "yi": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yi&fmt=json3",
                "name": "Yiddish"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yi&fmt=srv1",
                "name": "Yiddish"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yi&fmt=srv2",
                "name": "Yiddish"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yi&fmt=srv3",
                "name": "Yiddish"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yi&fmt=ttml",
                "name": "Yiddish"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yi&fmt=vtt",
                "name": "Yiddish"
            }
        ],
        "yo": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yo&fmt=json3",
                "name": "Yoruba"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yo&fmt=srv1",
                "name": "Yoruba"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yo&fmt=srv2",
                "name": "Yoruba"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yo&fmt=srv3",
                "name": "Yoruba"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yo&fmt=ttml",
                "name": "Yoruba"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=yo&fmt=vtt",
                "name": "Yoruba"
            }
        ],
        "zu": [
            {
                "ext": "json3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=zu&fmt=json3",
                "name": "Zulu"
            },
            {
                "ext": "srv1",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=zu&fmt=srv1",
                "name": "Zulu"
            },
            {
                "ext": "srv2",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=zu&fmt=srv2",
                "name": "Zulu"
            },
            {
                "ext": "srv3",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=zu&fmt=srv3",
                "name": "Zulu"
            },
            {
                "ext": "ttml",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=zu&fmt=ttml",
                "name": "Zulu"
            },
            {
                "ext": "vtt",
                "url": "https://www.youtube.com/api/timedtext?v=dQw4w9WgXcQ&caps=asr&opi=112496729&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1686942488&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Copi%2Cxoaf&signature=66FDA10348C66320690BAA3C012A1F2295673C2B.3FB8DB4C06DA646A9B9FD88A3AFFB6EF41D067B9&key=yt8&kind=asr&lang=en&tlang=zu&fmt=vtt",
                "name": "Zulu"
            }
        ]
    },
    "subtitles": {},
    "comment_count": null,
    "chapters": null,
    "like_count": 16494583,
    "channel": "Rick Astley",
    "channel_follower_count": 3720000,
    "upload_date": "20091025",
    "availability": "public",
    "original_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
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
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
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
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-10485759"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=10485760-20971519"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=20971520-31457279"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=31457280-41943039"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=41943040-52428799"
                },
                {
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=248&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=video%2Fwebm&gir=yes&clen=55643203&dur=212.040&lmt=1674241092388391&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=453D434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAOfWLe3lwXCNZ50wwDJtg2VIT4boftgiX-7_TKbnT4rAAiEA_01-YMsx666M-6OwQO0Z92BeDbLwmdCL86ZoO-ieVeA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=52428800-55643203"
                }
            ],
            "container": "webm_dash",
            "resolution": "1920x1080",
            "aspect_ratio": 1.78,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
            "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=251&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=3437753&dur=212.061&lmt=1674228069793936&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAI8dC2RD4d8oGuz13vWKzwnU2cdCKV2czChgl6c8l0KBAiEAnbJomc_cIebFApvYCrQvEyzytuWWLdwKs6MWObfe-no%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D",
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
                    "url": "https://rr3---sn-8xgp1vo-ab5l.googlevideo.com/videoplayback?expire=1686938888&ei=qFCMZPbtJozQ8wTmqIToCQ&ip=96.250.56.162&id=o-AEMY1GH729MvaF6BLcZCmyFpHJADupWHUMg5IgLFsj-3&itag=251&source=youtube&requiressl=yes&mh=7c&mm=31%2C26&mn=sn-8xgp1vo-ab5l%2Csn-p5qs7nsr&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=1653750&spc=qEK7B6SBY5KbH6g4rXlpiHrxFQEI9Wo&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=3437753&dur=212.061&lmt=1674228069793936&mt=1686916877&fvip=5&keepalive=yes&fexp=24007246%2C24363392&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAI8dC2RD4d8oGuz13vWKzwnU2cdCKV2czChgl6c8l0KBAiEAnbJomc_cIebFApvYCrQvEyzytuWWLdwKs6MWObfe-no%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJtTuPt8GGZeMQU2qilFZQVFdlHXDwdJw-2Tg1iepKPvAiEApHNx8U9gLBhk_-U6RDKtfzgxLPjvzekrDEhMInCq6bA%3D&range=0-3437753"
                }
            ],
            "container": "webm_dash",
            "resolution": "audio only",
            "aspect_ratio": null,
            "http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
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
'''