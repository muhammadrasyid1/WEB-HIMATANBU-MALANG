import re

html_path = r'D:\Web_Himatanbu_Malang\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# ==========================================
# 3. UPGRADE SLIDE-3 (Bagan Struktur Pohon)
# ==========================================
theatrical_bg = '''            <!-- THEATRICAL STAGE BACKGROUND: Spotlight Beams, Star Bursts & Stardust -->
            <div style="position:absolute;inset:0;pointer-events:none;overflow:hidden;">
                <!-- Curtain Shadows -->
                <div style="position:absolute;left:-5%;top:0;bottom:0;width:25%;background:linear-gradient(90deg, rgba(6,22,68,0.55) 0%, rgba(15,48,135,0.2) 60%, transparent 100%);"></div>
                <div style="position:absolute;right:-5%;top:0;bottom:0;width:25%;background:linear-gradient(270deg, rgba(6,22,68,0.55) 0%, rgba(15,48,135,0.2) 60%, transparent 100%);"></div>
                
                <!-- Dual Theatrical Spotlight Beams -->
                <div style="position:absolute;top:0;left:10%;width:260px;height:100%;background:linear-gradient(135deg, rgba(255,255,255,0.14) 0%, rgba(96,165,250,0.06) 50%, transparent 80%);transform:rotate(-14deg);transform-origin:top left;filter:blur(14px);"></div>
                <div style="position:absolute;top:0;right:10%;width:260px;height:100%;background:linear-gradient(225deg, rgba(255,255,255,0.14) 0%, rgba(96,165,250,0.06) 50%, transparent 80%);transform:rotate(14deg);transform-origin:top right;filter:blur(14px);"></div>

                <!-- Floating Celestial Stardust Sparkles -->
                <div class="hero-sparkle" style="top:18%;left:15%;animation-delay:0s;"></div>
                <div class="hero-sparkle" style="top:52%;left:12%;animation-delay:1.5s;"></div>
                <div class="hero-sparkle" style="top:22%;right:15%;animation-delay:0.8s;"></div>
                <div class="hero-sparkle" style="top:58%;right:18%;animation-delay:2.2s;"></div>

                <!-- Star Bursts in Blue -->
                <svg style="position:absolute;left:2%;top:10%;opacity:0.6;" width="80" height="80" viewBox="0 0 100 100" fill="none">
                    <path d="M50 0 L55 38 L93 15 L62 45 L100 50 L62 55 L93 85 L55 62 L50 100 L45 62 L7 85 L38 55 L0 50 L38 45 L7 15 L45 38 Z" fill="#60a5fa"/>
                </svg>
                <svg style="position:absolute;right:3%;bottom:12%;opacity:0.45;" width="75" height="75" viewBox="0 0 100 100" fill="none">
                    <path d="M50 0 L55 38 L93 15 L62 45 L100 50 L62 55 L93 85 L55 62 L50 100 L45 62 L7 85 L38 55 L0 50 L38 45 L7 15 L45 38 Z" fill="#93c5fd"/>
                </svg>
                <!-- Bottom Right Accent Ring -->
                <div style="position:absolute;right:-35px;bottom:-35px;width:160px;height:160px;border-radius:9999px;border:18px solid rgba(59,130,246,0.35);"></div>
                <!-- Soft Center Glow -->
                <div style="position:absolute;top:8%;left:50%;transform:translateX(-50%);width:70%;height:45%;border-radius:50%;background:radial-gradient(ellipse, rgba(147,197,253,0.3) 0%, transparent 70%);"></div>
            </div>'''

old_slide_3_start = '<section id="slide-3" class="ppt-slide slide-next">\n            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-3 w-full">'
new_slide_3_start = '<section id="slide-3" class="ppt-slide slide-next bg-curtain-blue select-none">\n' + theatrical_bg + '\n            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-3 w-full relative z-10">'

text = text.replace(old_slide_3_start, new_slide_3_start, 1)

# Ganti judul slide 3 menjadi chrome styling dan pill badge
old_slide_3_header = '''                <div class="ppt-anim-1 text-center max-w-3xl mx-auto mb-6">
                    <span class="px-3.5 py-1 text-xs font-bold uppercase rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">Slide 04 • Hierarki Kepengurusan</span>
                    <h3 class="text-3xl sm:text-4xl font-heading font-black text-slate-900 dark:text-white mt-2">Bagan Struktur Organisasi</h3>
                    <p class="text-slate-600 dark:text-slate-300 text-xs sm:text-sm mt-1">Garis koordinasi dan instruksi Kabinet Bersujud Progresif 2026/2027.</p>'''

new_slide_3_header = '''                <div class="ppt-anim-1 text-center max-w-3xl mx-auto mb-4 sm:mb-5">
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white text-[#091e52] font-black text-xs tracking-wider uppercase shadow-[0_10px_25px_rgba(0,0,0,0.35)] border border-blue-200/60 mb-2 animate-float-gentle">
                        <i class="fa-solid fa-sitemap text-amber-500"></i>
                        <span>Slide 04 • Hierarki Kepengurusan</span>
                    </div>
                    <h3 class="text-3xl sm:text-4xl font-heading font-black text-chrome-himatanbu tracking-wide animate-shine mt-1">
                        BAGAN STRUKTUR ORGANISASI
                    </h3>
                    <p class="text-blue-100/90 text-xs sm:text-sm font-medium mt-1 drop-shadow">Garis koordinasi dan instruksi Kabinet Bersujud Progresif 2026/2027.</p>'''

text = text.replace(old_slide_3_header, new_slide_3_header, 1)

# Ganti org-line-down dengan org-line-down-animated & org-horizontal dengan org-horizontal-animated
text = text.replace('class="org-line-down"', 'class="org-line-down-animated"')
text = text.replace('class="org-horizontal"', 'class="org-horizontal-animated"')

# Tambahkan crown aura dan pulse-gold pada kartu Ketum
old_ketum = '''<div class="glass-card p-4 rounded-3xl border-2 border-emerald-500 text-center shadow-xl glow-emerald w-60 hover:scale-105 transition-transform cursor-pointer" onclick="openMemberModal('ketum')">'''
new_ketum = '''<div class="glass-card p-4 rounded-3xl border-2 border-amber-400 text-center shadow-2xl glow-emerald w-60 hover:scale-105 transition-transform cursor-pointer animate-pulse-gold bg-white/95 dark:bg-slate-900/90" onclick="openMemberModal('ketum')">'''
text = text.replace(old_ketum, new_ketum, 1)

old_crown = '''<i class="fa-solid fa-crown text-amber-400"></i>'''
new_crown = '''<i class="fa-solid fa-crown text-amber-400 animate-crown-aura"></i>'''
text = text.replace(old_crown, new_crown, 1)

# ==========================================
# 4. UPGRADE SLIDE-4 (Daftar Anggota)
# ==========================================
old_slide_4_start = '<section id="slide-4" class="ppt-slide slide-next">\n            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-3 w-full">'
new_slide_4_start = '<section id="slide-4" class="ppt-slide slide-next bg-curtain-blue select-none">\n' + theatrical_bg + '\n            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-3 w-full relative z-10">'

text = text.replace(old_slide_4_start, new_slide_4_start, 1)

old_slide_4_header = '''                <div class="ppt-anim-1 flex flex-col md:flex-row md:items-end justify-between gap-4 mb-6">
                    <div>
                        <span class="text-xs uppercase tracking-widest font-extrabold text-emerald-600 dark:text-emerald-400">Slide 05 • Direktori Anggota</span>
                        <h3 class="text-2xl sm:text-4xl font-heading font-black text-slate-900 dark:text-white mt-1">Daftar Anggota Muda (2026)</h3>
                        <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">22 Mahasiswa perantau Tanah Bumbu di Malang sesuai data resmi.</p>
                    </div>'''

new_slide_4_header = '''                <div class="ppt-anim-1 flex flex-col md:flex-row md:items-end justify-between gap-4 mb-4">
                    <div>
                        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-white text-[#091e52] font-black text-xs tracking-wider uppercase shadow-md border border-blue-200/60 mb-1 animate-float-gentle">
                            <i class="fa-solid fa-users text-amber-500"></i>
                            <span>Slide 05 • Direktori Anggota</span>
                        </div>
                        <h3 class="text-2xl sm:text-4xl font-heading font-black text-chrome-himatanbu mt-1 animate-shine">Daftar Anggota Muda (2026)</h3>
                        <p class="text-xs text-blue-100/90 font-medium mt-0.5">22 Mahasiswa perantau Tanah Bumbu di Malang sesuai data resmi.</p>
                    </div>'''

text = text.replace(old_slide_4_header, new_slide_4_header, 1)

# ==========================================
# 5. UPGRADE SLIDE-5 (Program Kerja & Asrama)
# ==========================================
old_slide_5_start = '<section id="slide-5" class="ppt-slide slide-next">\n            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-3 w-full">'
new_slide_5_start = '<section id="slide-5" class="ppt-slide slide-next bg-curtain-blue select-none">\n' + theatrical_bg + '\n            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-3 w-full relative z-10">'

text = text.replace(old_slide_5_start, new_slide_5_start, 1)

old_slide_5_header = '''                <div class="ppt-anim-1 text-center max-w-3xl mx-auto mb-6">
                    <span class="px-3.5 py-1 text-xs font-bold uppercase rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20">Slide 06 • Agenda & Dedikasi</span>
                    <h3 class="text-3xl sm:text-4xl font-heading font-black text-slate-900 dark:text-white mt-1">Program Kerja & Sekretariat</h3>
                    <p class="text-slate-600 dark:text-slate-300 text-xs sm:text-sm mt-1">Agenda unggulan untuk mahasiswa perantauan dan masyarakat Tanah Bumbu.</p>
                </div>'''

new_slide_5_header = '''                <div class="ppt-anim-1 text-center max-w-3xl mx-auto mb-4 sm:mb-5">
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white text-[#091e52] font-black text-xs tracking-wider uppercase shadow-[0_10px_25px_rgba(0,0,0,0.35)] border border-blue-200/60 mb-2 animate-float-gentle">
                        <i class="fa-solid fa-calendar-check text-amber-500"></i>
                        <span>Slide 06 • Agenda & Dedikasi</span>
                    </div>
                    <h3 class="text-3xl sm:text-4xl font-heading font-black text-chrome-himatanbu mt-1 animate-shine">Program Kerja & Sekretariat</h3>
                    <p class="text-blue-100/90 text-xs sm:text-sm font-medium mt-1 drop-shadow">Agenda unggulan untuk mahasiswa perantauan dan masyarakat Tanah Bumbu.</p>
                </div>'''

text = text.replace(old_slide_5_header, new_slide_5_header, 1)

# Tambahkan animate-float pada 6 kartu proker
text = text.replace('border-l-4 border-l-emerald-500">', 'border-l-4 border-l-emerald-500 animate-float-1 bg-white/95 dark:bg-slate-900/90 backdrop-blur-md">', 1)
text = text.replace('border-l-4 border-l-teal-500">', 'border-l-4 border-l-teal-500 animate-float-2 bg-white/95 dark:bg-slate-900/90 backdrop-blur-md">', 1)
text = text.replace('border-l-4 border-l-blue-500">', 'border-l-4 border-l-blue-500 animate-float-3 bg-white/95 dark:bg-slate-900/90 backdrop-blur-md">', 1)
text = text.replace('border-l-4 border-l-indigo-500">', 'border-l-4 border-l-indigo-500 animate-float-4 bg-white/95 dark:bg-slate-900/90 backdrop-blur-md">', 1)
text = text.replace('border-l-4 border-l-amber-500">', 'border-l-4 border-l-amber-500 animate-float-1 bg-white/95 dark:bg-slate-900/90 backdrop-blur-md">', 1)
text = text.replace('border-l-4 border-l-rose-500">', 'border-l-4 border-l-rose-500 animate-float-2 bg-white/95 dark:bg-slate-900/90 backdrop-blur-md">', 1)

# Simpan kembali
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Slides 3, 4, 5 full upgrade completed!')

