## Build your own Cloadflare Workers.

<br>

Method to get YouTube channel live URL with **Workers Script.**

<br>

If you're new to **CF Workers**, visit and get started here: **[workers.cloudflare.com](https://workers.cloudflare.com/)**

<br>

## Build now

<br>

**Follow the steps:**

1. Your Cloudflare dashboard. `dash.cloudflare.com`

2. `Workers & Pages` > `Overview`.

3. `Create application`.

4. `Create Worker`.

5. Ignore the workers custom name, you can change it later.

6. Click on `Deploy`.

7. `Configure Worker` <> `Edit code` Choose one.

- If `Configure Worker`, continue to follow step number.
- If `Edit code`, skip step (8) and go to **Get Script Code**.

8. `Quick edit`.

<br>
<hr>

## Get Script Code

<br>

Select and copy the **Script Code** you want below, go to edit script workers and remove all existing scripts, then paste the new script code you just copied. The last **Save and deploy**.

Before closing/exiting the page, make sure the script is running and working properly without errors.

<br>

### Script Code

<br>
<br>

<details>
<summary><strong>Channel URL (ID-based)</strong></summary>

<br>

`youtube.com/channel/UCUZHFZ9jIKrLroW8LcyJEQQ`

<br>

```js
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
          cacheTtl: 10800,
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
</details>

<br>
<hr>

<details>
<summary><strong>Custom URL</strong></summary>

<br>

`youtube.com/c/YouTubeCreators`

<br>

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, { status: 500 })
    )
  )
})

async function handleRequest (request) {
  const { pathname } = new URL(request.url)

  if (pathname.startsWith('/c/')) {
    const customName = pathname.split('/')?.[2]?.split('.')?.[0]

    if (customName !== '') {
      const url = `https://www.youtube.com/c/${customName}/live`

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
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
      throw Error(`Channel Name not found: ${pathname}`)
    }
  } else {
    throw Error(`Path not found: ${pathname}`)
  }
}
```
</details>

<br>
<hr>

<details>
<summary><strong>Legacy Username URL</strong></summary>

<br>

`youtube.com/user/YouTube`

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, { status: 500 })
    )
  )
})

async function handleRequest (request) {
  const { pathname } = new URL(request.url)

  if (pathname.startsWith('/user/')) {
    const userName = pathname.split('/')?.[2]?.split('.')?.[0]

    if (userName !== '') {
      const url = `https://www.youtube.com/user/${userName}/live`

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
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
      throw Error(`Channel Name not found: ${pathname}`)
    }
  } else {
    throw Error(`Path not found: ${pathname}`)
  }
}
```
</details>

<br>
<hr>

<details>
<summary><strong>YouTube Live video URL</strong></summary>

<br>

`youtube.com/live/0vGEr_McaHM`

<br>

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, { status: 500 })
    )
  )
})

async function handleRequest (request) {
  const { pathname } = new URL(request.url)

  if (pathname.startsWith('/live/')) {
      const videoId = pathname.split('/')?.[2]?.split('.')?.[0]
    
    if (videoId !== '') { 
      const url = `https://www.youtube.com/live/${videoId}/live`

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
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
      throw Error(`Video ID not found: ${pathname}`)
    }
  } else {
    throw Error(`Path not found: ${pathname}`)
  }
}
```
</details>

<br>
<hr>

<details>
<summary><strong>YouTube Handle URL</strong></summary>

<br>

`youtube.com/@youtubecreators`

<br>

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, { status: 500 })
    )
  )
})

async function handleRequest (request) {
  const { pathname } = new URL(request.url)

  if (pathname.startsWith('/@')) {
      const handle = pathname.split('.')?.[0]
    
    if (handle !== '') { 
      const url = `https://www.youtube.com/${handle}/live`

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
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
      throw Error(`Channel Name not found: ${pathname}`)
    }
  } else {
    throw Error(`Path not found: ${pathname}`)
  }
}
```
</details>

<br>
<hr>
<br>

Don't forget to rename your **workers** > `yourCustomName.yourName.workers.dev`, it's up to you to make it an attractive _custom name_.

To rename your workers: 

Your workers > `Manage application` > `Rename service` > _Choose your new service name_ > `Continue`.

<br>

After deploying the new workers script, activate the workers by appending a **.m3u8** link to the end of the URL.

`/channel/`
```url
https://workers.name.workers.dev/channel/channel-id.m3u8
```

`/c/`
```url
https://workers.name.workers.dev/c/custom-name.m3u8
```

`/user/`
```url
https://workers.name.workers.dev/user/user-name.m3u8
```

`/live/`
```url
https://workers.name.workers.dev/live/video-id.m3u8
```

`/@`
```url
https://workers.name.workers.dev/@handle-name.m3u8
```

<br>
<br>

- Get the Channel ID **[Here](https://commentpicker.com/youtube-channel-id.php)**

<br>

**Important:** The **Link** only works if the **YT** channel is Live.

<hr>
<br>

**CF Workers:** Request limit is 100,000 per day. If the limit is exceeded, the request returns an error.

<br>
