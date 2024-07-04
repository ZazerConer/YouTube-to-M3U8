## Build your own Cloudflare Workers.

<br>

Method to get YouTube channel live URL with **Workers Script.**

<br>

If you're new to **CF Workers**, visit and get started here: **[workers.cloudflare.com](https://workers.cloudflare.com/)**

<br>

## Build now

<br>

**Follow the steps:**

1.  Your Cloudflare dashboard. <sup>`dash.cloudflare.com`</sup>
    
2.  `Workers & Pages` > `Overview`.
    
3.  `Create`.
    
4.  `Create Worker`.
    
5.  Ignore the workers custom name, you can change it later.
    
6.  Click on `Deploy`.
    
7.  Choose one > `Edit code` or `Continue to project`.
    

*   If `Edit code`, skip step <sup>`8`</sup> and go to **Get Script Code**.
*   If `Continue to project`, follow the step number.

8.  Find `Quick edit` and click.

<br> <hr>

## Get Script Code

<br>

Select and copy the **Script Code** you want below, go to the Worker script editor and remove all existing scripts, then paste the new script code you just copied and then click `Deploy` > `Save and deploy`.

Before closing/exiting the page, make sure the script is running and working properly without errors.

<br>

### Script Code

<br> <br>

<details> <summary><strong>Channel ID</strong></summary>

<br>

`youtube.com/channel/channelID`

<br>

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, {status: 500})
    )
  )
});

async function handleRequest(request) {
  const {pathname} = new URL(request.url);

  if (pathname.startsWith('/channel/')) {
    const channelID = pathname.split('/')[2].split('.')[0];

    if (channelID !== '') {
      const url = `https://www.youtube.com/channel/${channelID}/live`;

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
          cacheEverything: true
        }
      });

      if (response.ok) {
        const text = await response.text();
        const stream = text.match(/(?<=hlsManifestUrl":").*\.m3u8/g)

        return Response.redirect(stream, 302);
      } else {
        throw Error(`Youtube URL (${url}) failed with status: ${response.status}`);
      }
    } else {
      throw Error(`Channel ID not found: ${pathname}`);
    }
  } else {
    throw Error(`Path not found: ${pathname}`);
  }
}
```

</details>

<br> <hr>

<details> <summary><strong>Custom Name</strong></summary>

<br>

`youtube.com/c/customName`

<br>

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, {status: 500})
    )
  )
});

async function handleRequest(request) {
  const {pathname} = new URL(request.url);

  if (pathname.startsWith('/c/')) {
    const customName = pathname.split('/')[2].split('.')[0];

    if (customName !== '') {
      const url = `https://www.youtube.com/c/${customName}/live`;

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
          cacheEverything: true
        }
      });

      if (response.ok) {
        const text = await response.text();
        const stream = text.match(/(?<=hlsManifestUrl":").*\.m3u8/g);

        return Response.redirect(stream, 302);
      } else {
        throw Error(`Youtube URL (${url}) failed with status: ${response.status}`);
      }
    } else {
      throw Error(`Channel Name not found: ${pathname}`);
    }
  } else {
    throw Error(`Path not found: ${pathname}`);
  }
}
```

</details>

<br> <hr>

<details> <summary><strong>User Name</strong></summary>

<br>

`youtube.com/user/userName`

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, {status: 500})
    )
  )
});

async function handleRequest(request) {
  const {pathname} = new URL(request.url);

  if (pathname.startsWith('/user/')) {
    const userName = pathname.split('/')[2].split('.')[0];

    if (userName !== '') {
      const url = `https://www.youtube.com/user/${userName}/live`;

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
          cacheEverything: true
        }
      });

      if (response.ok) {
        const text = await response.text();
        const stream = text.match(/(?<=hlsManifestUrl":").*\.m3u8/g);

        return Response.redirect(stream, 302);
      } else {
        throw Error(`Youtube URL (${url}) failed with status: ${response.status}`);
      }
    } else {
      throw Error(`Channel Name not found: ${pathname}`);
    }
  } else {
    throw Error(`Path not found: ${pathname}`);
  }
}
```

</details>

<br> <hr>

<details> <summary><strong>Live Video ID</strong></summary>

<br>

`youtube.com/live/videoID`

<br>

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, {status: 500})
    )
  )
});

async function handleRequest(request) {
  const {pathname} = new URL(request.url);

  if (pathname.startsWith('/live/')) {
      const videoID = pathname.split('/')[2].split('.')[0];
    
    if (videoID !== '') { 
      const url = `https://www.youtube.com/live/${videoID}/live`;

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
          cacheEverything: true
        }
      });

      if (response.ok) {
        const text = await response.text();
        const stream = text.match(/(?<=hlsManifestUrl":").*\.m3u8/g);

        return Response.redirect(stream, 302);
      } else {
        throw Error(`Youtube URL (${url}) failed with status: ${response.status}`);
      }
    } else {
      throw Error(`Video ID not found: ${pathname}`);
    }
  } else {
    throw Error(`Path not found: ${pathname}`);
  }
}
```

</details>

<br> <hr>

<details> <summary><strong>Handle Name</strong></summary>

<br>

`youtube.com/@handleName`

<br>

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, {status: 500})
    )
  )
});

async function handleRequest(request) {
  const {pathname} = new URL(request.url);

  if (pathname.startsWith('/@')) {
      const handleName = pathname.split('.')[0];
    
    if (handleName !== '') { 
      const url = `https://www.youtube.com/${handleName}/live`;

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
          cacheEverything: true
        }
      });

      if (response.ok) {
        const text = await response.text();
        const stream = text.match(/(?<=hlsManifestUrl":").*\.m3u8/g);

        return Response.redirect(stream, 302);
      } else {
        throw Error(`Youtube URL (${url}) failed with status: ${response.status}`);
      }
    } else {
      throw Error(`Channel Name not found: ${pathname}`);
    }
  } else {
    throw Error(`Path not found: ${pathname}`);
  }
}
```

</details>

<br><hr><br>

OR

<br>

<details>  
<summary><strong>(Combine all)</strong> Get the request in the same URL</summary>

<br>

```js
addEventListener('fetch', (event) => {
  event.respondWith(
    handleRequest(event.request).catch(
      (err) => new Response(err.message, {status: 500})
    )
  )
});

async function handleRequest(request) {
  const {pathname} = new URL(request.url);

  if (pathname.startsWith('/channel/') ||
      pathname.startsWith('/c/') ||
      pathname.startsWith('/user/') ||
      pathname.startsWith('/live/') ||
      pathname.startsWith('/@')) {
      const target = pathname.split('.')[0];
    
    if (target !== '') { 
      const url = `https://www.youtube.com${target}/live`;

      const response = await fetch(url, {
        cf: {
          cacheTtl: 10800,
          cacheEverything: true
        }
      });

      if (response.ok) {
        const text = await response.text();
        const stream = text.match(/(?<=hlsManifestUrl":").*\.m3u8/g);

        return Response.redirect(stream, 302);
      } else {
        throw Error(`Youtube URL (${url}) failed with status: ${response.status}`);
      }
    } else {
      throw Error(`URL path not found: ${pathname}`);
    }
  } else {
    throw Error(`Path not found: ${pathname}`);
  }
}
```

</details>

<br> <hr> <br>

You can test the Workers script here **[Workers Playground](https://workers.cloudflare.com/playground)**

<br>

Don't forget to rename your **workers** > `custom.name.workers.dev`, it's up to you to make it an attractive _custom name_.

To rename your workers:

1.  Your **Workers**.
2.  `Manage`.
3.  `Rename`.
4.  Choose your new Worker name. <sup>`Enter a new name`</sup>
5.  `Continue`.
6.  `Rename Worker`.
7.  `Finish`.

<br>

After deploying the new Worker script, activate the Worker by appending a `.m3u8` link to the end of the URL.

<br>

`/channel/`

```url
https://example.name.workers.dev/channel/channelID.m3u8
```

`/c/`

```url
https://example.name.workers.dev/c/customName.m3u8
```

`/user/`

```url
https://example.name.workers.dev/user/userName.m3u8
```

`/live/`

```url
https://example.name.workers.dev/live/videoID.m3u8
```

`/@`

```url
https://example.name.workers.dev/@handleName.m3u8
```

<br> <br>

> [!IMPORTANT]  
> The **Link** only works if the **YT** channel is Live.

<br> <br>

<details><summary><strong>YouTube Channel ID Finder</strong></summary>

<br>

*   [seostudio.tools/youtube-channel-id](https://seostudio.tools/youtube-channel-id)
    
*   [barrazacarlos.com/free-seo-tools/youtube-channel-id](https://barrazacarlos.com/free-seo-tools/youtube-channel-id)
    
*   [web-seotools.com/youtube-channel-id](https://web-seotools.com/youtube-channel-id)
    
*   [wholeseotools.com/youtube-channel-id](https://wholeseotools.com/youtube-channel-id)
    
*   [sarojmeher.com/smartweb/youtube-channel-id](https://www.sarojmeher.com/smartweb/youtube-channel-id)
    
*   [seotoolstamil.com/youtube-channel-id](https://seotoolstamil.com/youtube-channel-id)
    
*   [webtoolsmate.com/youtube-channel-id](https://webtoolsmate.com/youtube-channel-id)
    
*   [vionlinetools.com/youtube-channel-id](https://vionlinetools.com/youtube-channel-id)
    
*   [onhelpinghand.org/youtube-channel-id](https://www.onhelpinghand.org/youtube-channel-id)
    
*   [bonoseotools.com/youtube-channel-id](https://bonoseotools.com/youtube-channel-id)
    
*   [zoneseotools.com/youtube-channel-id](https://zoneseotools.com/youtube-channel-id)
    
*   [naijaseotools.com/youtube-channel-id](https://naijaseotools.com/youtube-channel-id)
    
*   [seotool247.com/youtube-channel-id](https://seotool247.com/youtube-channel-id)
    
*   [mrephrase.com/en/youtube-channel-id](https://mrephrase.com/en/youtube-channel-id)
    
*   [oceanoftool.com/youtube-channel-id](https://oceanoftool.com/youtube-channel-id)
    
*   [mintseotools.com/youtube-channel-id](https://mintseotools.com/youtube-channel-id)
    
*   [toolsa2z.com/youtube-channel-id/](https://toolsa2z.com/youtube-channel-id/)
    
*   [impif.com/youtube-channel-id](https://impif.com/youtube-channel-id)
    
*   [ytbos.com/find-youtube-channel-id](https://ytbos.com/find-youtube-channel-id.php)
    
*   [beehosting.pro/seotools/youtube-channel-id](https://beehosting.pro/seotools/youtube-channel-id)
    
*   [seostudiotools.com/youtube-channel-id](https://seostudiotools.com/youtube-channel-id)
    
*   [simplifiedwebtools.com/youtube-channel-id](https://simplifiedwebtools.com/youtube-channel-id)
    
*   [codeofaninja.com/tools/find-youtube-channel-id](https://www.codeofaninja.com/tools/find-youtube-channel-id)
    

</details>

<hr> <br> <br>

> [!NOTE]
> **CF Workers:** Request limit is 100,000 per day. If the limit is exceeded, the request returns an error.

<br>
