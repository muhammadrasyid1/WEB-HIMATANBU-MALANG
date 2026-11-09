import re

html_path = r'D:\Web_Himatanbu_Malang\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Optimasi slide transisi dengan translate3d, will-change, and backface-visibility
old_transition_css = '''        body.ppt-mode .ppt-slide {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            overflow-y: auto;
            overflow-x: hidden;
            -webkit-overflow-scrolling: touch;
            display: flex;
            flex-direction: column;
            align-items: center;
            opacity: 0;
            pointer-events: none;
            transition-property: transform, opacity, filter;
            transition-duration: 0.6s;
            transition-timing-function: cubic-bezier(0.25, 1, 0.5, 1);
            padding-top: 1rem;
            padding-bottom: 3.5rem;
        }'''

new_transition_css = '''        body.ppt-mode .ppt-slide {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            overflow-y: auto;
            overflow-x: hidden;
            -webkit-overflow-scrolling: touch;
            display: flex;
            flex-direction: column;
            align-items: center;
            opacity: 0;
            pointer-events: none;
            transition-property: transform, opacity;
            transition-duration: 0.45s;
            transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
            padding-top: 1rem;
            padding-bottom: 3.5rem;
            will-change: transform, opacity;
            transform: translateZ(0);
            backface-visibility: hidden;
            -webkit-backface-visibility: hidden;
        }'''

text = text.replace(old_transition_css, new_transition_css, 1)

# Ganti translateY dengan translate3d untuk akselerasi GPU 60fps di HP
text = text.replace('transform: translateY(-100%);', 'transform: translate3d(0, -100%, 0);')
text = text.replace('transform: translateY(0);', 'transform: translate3d(0, 0, 0);')
text = text.replace('transform: translateY(100%);', 'transform: translate3d(0, 100%, 0);')

# 2. Perbaiki keyframes animasi: ganti translateY murni dengan translate3d (Hardware Accelerated)
old_keyframes = '''        /* CONTINUOUS FLOATING & LIVING SLIDE ANIMATIONS */
        @keyframes floatGentle {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-7px); }
        }
        @keyframes floatGentleAlt {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(6px); }
        }
        @keyframes floatNewspaper {
            0%, 100% { transform: translateY(0px) rotate(-0.5deg) scale(1); }
            50% { transform: translateY(-8px) rotate(0.8deg) scale(1.02); }
        }'''

new_keyframes = '''        /* CONTINUOUS FLOATING & LIVING SLIDE ANIMATIONS (GPU Optimized) */
        @keyframes floatGentle {
            0%, 100% { transform: translate3d(0, 0px, 0); }
            50% { transform: translate3d(0, -5px, 0); }
        }
        @keyframes floatGentleAlt {
            0%, 100% { transform: translate3d(0, 0px, 0); }
            50% { transform: translate3d(0, 5px, 0); }
        }
        @keyframes floatNewspaper {
            0%, 100% { transform: translate3d(0, 0px, 0) rotate(-0.5deg); }
            50% { transform: translate3d(0, -6px, 0) rotate(0.6deg); }
        }'''

text = text.replace(old_keyframes, new_keyframes, 1)

# Ganti pulseGlow & pulseGoldGlow: kurangi box-shadow berat yang bikin GPU HP ngos-ngosan
old_pulses = '''        @keyframes pulseGlow {
            0%, 100% { 
                box-shadow: 0 0 15px rgba(56, 189, 248, 0.3), 0 10px 25px rgba(0, 0, 0, 0.4); 
            }
            50% { 
                box-shadow: 0 0 30px rgba(56, 189, 248, 0.75), 0 15px 35px rgba(0, 0, 0, 0.6); 
            }
        }
        @keyframes pulseGoldGlow {
            0%, 100% { 
                box-shadow: 0 0 15px rgba(245, 158, 11, 0.35), 0 10px 25px rgba(0, 0, 0, 0.4); 
                transform: scale(1);
            }
            50% { 
                box-shadow: 0 0 32px rgba(251, 191, 36, 0.85), 0 15px 35px rgba(0, 0, 0, 0.6); 
                transform: scale(1.02);
            }
        }'''

new_pulses = '''        @keyframes pulseGlow {
            0%, 100% { 
                box-shadow: 0 4px 15px rgba(56, 189, 248, 0.3); 
                transform: translate3d(0, 0, 0);
            }
            50% { 
                box-shadow: 0 8px 25px rgba(56, 189, 248, 0.6); 
                transform: translate3d(0, -2px, 0);
            }
        }
        @keyframes pulseGoldGlow {
            0%, 100% { 
                box-shadow: 0 4px 15px rgba(245, 158, 11, 0.35); 
                transform: translate3d(0, 0, 0) scale(1);
            }
            50% { 
                box-shadow: 0 8px 25px rgba(251, 191, 36, 0.7); 
                transform: translate3d(0, -2px, 0) scale(1.015);
            }
        }'''

text = text.replace(old_pulses, new_pulses, 1)

# Ganti iconBounceLive ke translate3d
old_icon_bounce = '''        @keyframes iconBounceLive {
            0%, 100% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-5px) scale(1.1); }
        }'''

new_icon_bounce = '''        @keyframes iconBounceLive {
            0%, 100% { transform: translate3d(0, 0px, 0) scale(1); }
            50% { transform: translate3d(0, -4px, 0) scale(1.08); }
        }'''

text = text.replace(old_icon_bounce, new_icon_bounce, 1)

# Ganti cardEntranceStagger ke translate3d
old_stagger = '''        @keyframes cardEntranceStagger {
            0% {
                opacity: 0;
                transform: translateY(28px) scale(0.95);
            }
            100% {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }'''

new_stagger = '''        @keyframes cardEntranceStagger {
            0% {
                opacity: 0;
                transform: translate3d(0, 20px, 0) scale(0.97);
            }
            100% {
                opacity: 1;
                transform: translate3d(0, 0, 0) scale(1);
            }
        }'''

text = text.replace(old_stagger, new_stagger, 1)

# 3. Nonaktifkan animasi pada slide yang tidak aktif (.ppt-slide:not(.slide-active)) agar CPU & GPU HP tidak memproses animasi slide yang sedang tersembunyi
text = text.replace('/* Continuous Animation Classes */', '''/* Hentikan animasi di slide yang TIDAK aktif agar HP sangat ringan & super smooth */
        .ppt-slide:not(.slide-active) * {
            animation-play-state: paused !important;
        }

        /* Continuous Animation Classes (Hardware Accelerated) */
        .animate-float-1, .animate-float-2, .animate-float-3, .animate-float-4,
        .animate-float-gentle, .animate-float-newspaper, .animate-pulse-glow,
        .animate-pulse-gold, .animate-crown-aura, .animate-icon-bounce {
            will-change: transform;
            transform: translateZ(0);
        }''')

# 4. Optimasi backdrop-blur di HP: backdrop-filter sangat berat di browser mobile webkit/blink
# Pada layar mobile (max-width: 768px), kurangi backdrop-blur menjadi solid/semi-transparan elegan
mobile_perf_css = '''
        /* MOBILE PERFORMANCE ACCELERATION (Super Smooth 60fps di HP) */
        @media (max-width: 768px) {
            .backdrop-blur-md, .backdrop-blur-xl, .backdrop-blur-sm {
                backdrop-filter: none !important;
                -webkit-backdrop-filter: none !important;
            }
            .glass-card {
                backdrop-filter: none !important;
                -webkit-backdrop-filter: none !important;
                background-color: rgba(255, 255, 255, 0.96) !important;
            }
            .dark .glass-card {
                background-color: rgba(15, 23, 42, 0.94) !important;
            }
            /* Kurangi blur sorot lampu di HP agar GPU tidak drop frame */
            [style*="filter:blur"] {
                filter: none !important;
                opacity: 0.08 !important;
            }
        }
    </style>'''

text = text.replace('    </style>', mobile_perf_css, 1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('GPU Hardware Acceleration and Smoothness Tuning Applied!')

