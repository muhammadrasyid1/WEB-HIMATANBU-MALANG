// Service Worker HIMATANBU Malang - Optimasi Cache & Kecepatan
const CACHE_NAME = 'himatanbu-v3';
const ASSETS_TO_CACHE = [
    '/',
    '/index.html',
    '/logo_himatanbu.png',
    '/logo_himatanbu_1.jpg',
    '/logo_himatanbu_2.jpg',
    '/logo_himatanbu_3.jpg',
    '/logo_himatanbu_4.jpg',
    '/sejarah_himatanbu.png',
    '/favicon.ico'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(async cache => {
            for (const asset of ASSETS_TO_CACHE) {
                try {
                    await cache.add(asset);
                } catch (e) {
                    console.warn('SW cache note for', asset, e);
                }
            }
        })
    );
    self.skipWaiting();
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
            );
        })
    );
    self.clients.claim();
});

self.addEventListener('fetch', event => {
    if (event.request.method !== 'GET') return;
    const url = new URL(event.request.url);
    if (url.origin !== self.location.origin) return;
    
    event.respondWith(
        fetch(event.request)
            .then(response => {
                if (response && response.status === 200) {
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then(cache => {
                        cache.put(event.request, responseClone);
                    });
                }
                return response;
            })
            .catch(() => {
                return caches.match(event.request);
            })
    );
});
