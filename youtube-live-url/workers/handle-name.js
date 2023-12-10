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
