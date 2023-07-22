<div align="center"><strong>YouTube Live URL</strong></div>

<br>
<hr>

Get YouTube Channel Live **_URL_** using **_Cloudflare Workers_**.

<br>

`Copy code below:`

```js script
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, { status: 500 })
    )
  )
})

async function handleRequest (request) {
  const { pathname } = new URL(request.url)

  if (pathname.startsWith('/channel/')) {

    const channel = pathname.split('/')?.[2]?.split('.')?.[0]

    if (channel !== '') {
      const url = `https://www.youtube.com/channel/${channel}/live`

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800, // 3 hours
          cacheEverything: true
        }
      })

      if (response.ok) {
        const text = await response.text()
        const stream = text.match(/(?<=hlsManifestUrl":").*\.m3u8/g)

        return Response.redirect(stream, 302)
      } else {
        throw Error(`Youtube URL (${url}) failed with status: ${response.status}`)
      }
    } else {
      throw Error(`Channel ID not found: ${pathname}`)
    }
  } else {
    throw Error(`Path not found: ${pathname}`)
  }
}
```

**Save and deploy**

<hr>

Use of **M3U8** links.

```url
https://your-workers.username.workers.dev/channel/channel-id.m3u8
```

Example:

`https://livestream.zazerconer.workers.dev/channel/UCPe9vNjHF1kEExT5kHwc7aw.m3u8`

<br>
<br>
<hr>

### Get channel ID from YouTube Channel

<br>

You can get the channel ID **[HERE](https://commentpicker.com/youtube-channel-id.php)**

<br>
<hr>

### Don't have Cloudflare Workers yet? 

<br>

Go to **[cloudflare.com](https://www.cloudflare.com)**, create your **Cloudflare account** and learn how to use **Workers** on Cloudflare. After that you can copy the above code and paste it there.

<br>
<br>
<hr>

If you don't have much time to do all this and are too lazy to build your own code, don't worry. 

I've thought about it and made it for you. 

<br> 

**GO » [HERE](https://github.com/ZazerConer/liveYTmalaysia/blob/main/README.md#add-youtube-live-url-with-m3u8-link)** 

<br> 

Just click on the link above, follow the steps there. You don't need to build the code from scratch, as it is already built and available to use via **M3U8 [Link](https://github.com/ZazerConer/liveYTmalaysia/blob/main/README.md#m3u8-direct-link-for-youtube-live-channel)**. 

<br>
