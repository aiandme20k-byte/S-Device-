const CACHE="s-device-shell-011-v1";const FILES=["/app/","/app/manifest.webmanifest","/app/icon.svg"];
self.addEventListener("install",e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting())));
self.addEventListener("activate",e=>e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener("fetch",e=>{const u=new URL(e.request.url);if(e.request.method!=="GET"||u.origin!==self.location.origin||!u.pathname.startsWith("/app/"))return;
e.respondWith(fetch(e.request).catch(()=>caches.match(e.request)));});
