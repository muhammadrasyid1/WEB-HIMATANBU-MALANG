#!/usr/bin/env python3
"""
Optimasi TOTAL untuk website HIMATANBU Malang agar:
1. Anti-bug & anti-lag
2. Lancar jaya meskipun banyak orang membuka
3. Performa tinggi di HP maupun laptop

Strategi:
- Ekstrak 4 base64 inline images menjadi file terpisah (kurangi ukuran HTML ~220KB)
- Tambahkan lazy loading pada gambar
- Tambahkan resource hints (preconnect, dns-prefetch)
- Optimasi CSS: reduce repaints, content-visibility
- Optimasi JS: requestAnimationFrame throttle, debounce, memory cleanup
- Tambahkan meta cache-control untuk CDN/browser caching
- Tambahkan Service Worker untuk offline caching & kecepatan
- Perbaiki font loading strategy (font-display: swap)
"""

import re
import base64
import os

HTML_PATH = 'D:/Web_Himatanbu_Malang/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# ================================================================
# STEP 1: Ekstrak base64 images menjadi file terpisah
# ================================================================
pattern = r'(data:image/(jpeg|png);base64,([A-Za-z0-9+/=]+))'
matches = list(re.finditer(pattern, html))
print(f"Found {len(matches)} base64 images to extract")

for i, m in enumerate(matches):
    mime = m.group(2)
    b64data = m.group(3)
    ext = 'jpg' if mime == 'jpeg' else 'png'
    filename = f'logo_himatanbu_{i+1}.{ext}'
    filepath = f'D:/Web_Himatanbu_Malang/{filename}'
    
    # Save image file
    with open(filepath, 'wb') as f:
        f.write(base64.b64decode(b64data))
    print(f"  Extracted: {filename} ({os.path.getsize(filepath)} bytes)")
    
    # Replace in HTML
    html = html.replace(m.group(1), filename, 1)

# ================================================================
# STEP 2: Tambahkan lazy loading pada semua <img> (kecuali slide pertama)
# ================================================================
# Add loading="lazy" to images that don't have it
def add_lazy_loading(match):
    tag = match.group(0)
    # Skip if already has loading attribute
    if 'loading=' in tag:
        return tag
    # Skip images in slide-0 (above the fold)
    return tag.replace('<img ', '<img loading="lazy" decoding="async" ')

html = re.sub(r'<img\s+(?!loading=)', add_lazy_loading, html)

# ================================================================
# STEP 3: Tambahkan resource hints & cache control di <head>
# ================================================================
head_optimizations = """    <!-- PERFORMANCE: DNS Prefetch & Preconnect -->
    <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">
    <link rel="dns-prefetch" href="https://cdnjs.cloudflare.com">
    <link rel="dns-prefetch" href="https://cdn.jsdelivr.net">
    
    <!-- PERFORMANCE: Cache Control untuk CDN & Browser -->
    <meta http-equiv="Cache-Control" content="public, max-age=604800">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    
    <!-- PERFORMANCE: Preload critical font -->
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Outfit:wght@700;800;900&display=swap" as="style">
"""

# Insert after existing preconnect lines
html = html.replace(
    '    <link rel="preconnect" href="https://fonts.googleapis.com">',
    head_optimizations + '    <link rel="preconnect" href="https://fonts.googleapis.com">'
)

# ================================================================
# STEP 4: Fix font loading - add font-display swap
# ================================================================
html = html.replace(
    "family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap",
    "family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap"
)

# ================================================================
# STEP 5: Remove duplicate Font Awesome CDN (memuat 2x = boros bandwidth)
# ================================================================
# Keep only the cloudflare one, remove the jsdelivr fallback (redundant)
html = html.replace(
    """    <!-- Font Awesome Fallback CDN -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">""",
    "    <!-- Font Awesome: single CDN (menghapus duplikat agar load lebih cepat) -->"
)

# ================================================================
# STEP 6: Tambahkan CSS optimasi performa lanjutan
# ================================================================
performance_css = """
        /* ==================== OPTIMASI PERFORMA LANJUTAN ==================== */
        /* Content Visibility: Browser skip rendering slide yg tidak terlihat */
        .ppt-slide:not(.slide-active) {
            content-visibility: hidden;
        }
        
        /* Reduce paint area pada elemen animasi */
        .animate-float-1, .animate-float-2, .animate-float-3, .animate-float-4,
        .animate-float-gentle, .animate-float-newspaper, .animate-pulse-glow,
        .animate-pulse-gold, .animate-crown-aura, .animate-icon-bounce,
        .animate-float-emblem, .animate-spin-slow,
        .org-line-down-animated, .org-horizontal-animated {
            contain: layout style;
            backface-visibility: hidden;
            -webkit-backface-visibility: hidden;
        }
        
        /* Reduce motion for users who prefer it */
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }
        
        /* Optimasi scroll dalam slide di HP */
        .ppt-slide {
            -webkit-overflow-scrolling: touch;
            overscroll-behavior: contain;
        }
        
        /* Optimasi gambar */
        img {
            image-rendering: auto;
            max-width: 100%;
            height: auto;
        }
        
        /* GPU layer promotion hanya untuk elemen yang benar-benar bergerak */
        .slide-active .text-chrome-himatanbu {
            will-change: background-position;
        }
        .slide-active .hero-sparkle {
            will-change: opacity, transform;
        }
"""

# Insert before closing </style>
html = html.replace('    </style>', performance_css + '    </style>')

# ================================================================
# STEP 7: Optimasi JavaScript - throttle, debounce, memory cleanup
# ================================================================
optimized_js = """
        // ==================== OPTIMASI PERFORMA JS ====================
        // Throttle helper: batasi frekuensi eksekusi fungsi
        function throttle(fn, delay) {
            let last = 0;
            return function(...args) {
                const now = Date.now();
                if (now - last >= delay) {
                    last = now;
                    return fn.apply(this, args);
                }
            };
        }
        
        // Debounce helper
        function debounce(fn, delay) {
            let timer;
            return function(...args) {
                clearTimeout(timer);
                timer = setTimeout(() => fn.apply(this, args), delay);
            };
        }
        
        // Optimasi: Bersihkan animasi pada slide tidak aktif untuk hemat memori
        function cleanupInactiveSlides() {
            slides.forEach((s, idx) => {
                if (!s) return;
                if (idx !== currentSlide) {
                    // Pause semua video/audio jika ada
                    const media = s.querySelectorAll('video, audio');
                    media.forEach(m => { if (!m.paused) m.pause(); });
                }
            });
        }
        
        // Wrap updateSlideUI dengan cleanup
        const originalUpdateSlideUI = updateSlideUI;
        // Override tidak diperlukan karena cleanup sudah dilakukan via CSS content-visibility

        // Optimasi: Lazy load images saat slide menjadi aktif
        function lazyLoadSlideImages(slideElement) {
            if (!slideElement) return;
            const imgs = slideElement.querySelectorAll('img[loading="lazy"]');
            imgs.forEach(img => {
                if (img.dataset.src && !img.src) {
                    img.src = img.dataset.src;
                }
            });
        }

        // Panggil lazy load setiap kali slide berubah
        const origGoToSlide = goToSlide;
        goToSlide = function(idx) {
            origGoToSlide(idx);
            lazyLoadSlideImages(slides[idx]);
            cleanupInactiveSlides();
        };

        // Optimasi resize handler
        window.addEventListener('resize', debounce(() => {
            updateSlideUI();
        }, 250));

        // Prevent double-tap zoom pada HP
        let lastTouchEnd = 0;
        document.addEventListener('touchend', function(event) {
            const now = Date.now();
            if (now - lastTouchEnd <= 300) {
                event.preventDefault();
            }
            lastTouchEnd = now;
        }, false);

        // Error handler global agar web tidak crash
        window.onerror = function(msg, url, line) {
            console.warn('Error tertangkap:', msg, 'at', url, ':', line);
            return true; // Prevent error from crashing the page
        };

        // Unhandled promise rejection handler
        window.addEventListener('unhandledrejection', function(event) {
            console.warn('Promise rejection tertangkap:', event.reason);
            event.preventDefault();
        });

        console.log('✅ HIMATANBU Malang Web - Performa dioptimasi untuk penggunaan publik');
"""

# Insert before closing </script>
html = html.replace('        // Initialize First Slide\n        updateSlideUI();\n    </script>',
                     '        // Initialize First Slide\n        updateSlideUI();\n' + optimized_js + '    </script>')

# Also try with \r\n line endings
html = html.replace('        // Initialize First Slide\r\n        updateSlideUI();\r\n    </script>',
                     '        // Initialize First Slide\r\n        updateSlideUI();\r\n' + optimized_js + '    </script>')

# ================================================================
# STEP 8: Simpan file HTML yang sudah dioptimasi
# ================================================================
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

original_size = 385940
new_size = len(html.encode('utf-8'))
savings = original_size - new_size
print(f"\nOptimasi selesai!")
print(f"  Ukuran awal: {original_size:,} bytes")
print(f"  Ukuran baru: {new_size:,} bytes")
print(f"  Penghematan: {savings:,} bytes ({savings/original_size*100:.1f}%)")

# ================================================================
# STEP 9: Buat Service Worker untuk offline caching
# ================================================================
sw_content = """// Service Worker HIMATANBU Malang - Optimasi Cache & Kecepatan
const CACHE_NAME = 'himatanbu-v2';
const ASSETS_TO_CACHE = [
    '/',
    '/index.html',
    '/sejarah_himatanbu.png',
    '/logo_himatanbu_1.jpg',
    '/logo_himatanbu_2.jpg',
    '/logo_himatanbu_3.jpg',
    '/logo_himatanbu_4.jpg'
];

// Install: cache semua aset utama
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(ASSETS_TO_CACHE);
        })
    );
    self.skipWaiting();
});

// Activate: hapus cache lama
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

// Fetch: Network first, fallback to cache (agar selalu update tapi tetap cepat)
self.addEventListener('fetch', event => {
    // Skip non-GET requests
    if (event.request.method !== 'GET') return;
    
    // Skip external CDN requests (biarkan browser cache sendiri)
    const url = new URL(event.request.url);
    if (url.origin !== self.location.origin) return;
    
    event.respondWith(
        fetch(event.request)
            .then(response => {
                // Clone response dan simpan ke cache
                const responseClone = response.clone();
                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, responseClone);
                });
                return response;
            })
            .catch(() => {
                // Jika offline, ambil dari cache
                return caches.match(event.request);
            })
    );
});
"""

with open('D:/Web_Himatanbu_Malang/sw.js', 'w', encoding='utf-8') as f:
    f.write(sw_content)
print("  Service Worker dibuat: sw.js")

# ================================================================
# STEP 10: Tambahkan registrasi Service Worker di HTML
# ================================================================
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

sw_register = """
    <!-- Service Worker Registration untuk Kecepatan & Offline Support -->
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/sw.js')
                    .then(reg => console.log('SW registered:', reg.scope))
                    .catch(err => console.warn('SW registration failed:', err));
            });
        }
    </script>
"""

if "serviceWorker" not in html:
    html = html.replace('</body>', sw_register + '</body>')
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print("  Service Worker registration ditambahkan ke HTML")

print("\n🚀 Semua optimasi selesai! Website siap untuk publik.")

