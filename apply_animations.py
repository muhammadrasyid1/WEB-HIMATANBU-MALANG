import re

html_path = r'D:\Web_Himatanbu_Malang\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ==========================================
# 1. UPGRADE SLIDE-1 (Tujuan Organisasi)
# ==========================================
# Tambahkan animate-float-gentle pada badge & card, icon bounce pada bullseye
slide_1_old = '''        <section id="slide-1" class="ppt-slide slide-next bg-curtain-blue">
            <!-- Background Decorative Curtain & Star Burst (Royal Blue Theme) -->
            <div style="position:absolute;inset:0;pointer-events:none;overflow:hidden;">
                <!-- Left curtain side shadows (Soft royal blue, not black) -->
                <div style="position:absolute;left:-5%;top:0;bottom:0;width:25%;background:linear-gradient(90deg, rgba(6,22,68,0.55) 0%, rgba(15,48,135,0.2) 60%, transparent 100%);"></div>
                <div style="position:absolute;right:-5%;top:0;bottom:0;width:25%;background:linear-gradient(270deg, rgba(6,22,68,0.55) 0%, rgba(15,48,135,0.2) 60%, transparent 100%);"></div>
                <!-- Star Bursts in Blue -->
                <svg style="position:absolute;left:2%;top:10%;opacity:0.6;" width="80" height="80" viewBox="0 0 100 100" fill="none">
                    <path d="M50 0 L55 38 L93 15 L62 45 L100 50 L62 55 L93 85 L55 62 L50 100 L45 62 L7 85 L38 55 L0 50 L38 45 L7 15 L45 38 Z" fill="#60a5fa"/>
                </svg>
                <svg style="position:absolute;left:4%;top:50%;opacity:0.35;" width="50" height="50" viewBox="0 0 100 100" fill="none">
                    <path d="M50 0 L55 38 L93 15 L62 45 L100 50 L62 55 L93 85 L55 62 L50 100 L45 62 L7 85 L38 55 L0 50 L38 45 L7 15 L45 38 Z" fill="#93c5fd"/>
                </svg>
                <!-- Bottom Right Accent Ring -->
                <div style="position:absolute;right:-35px;bottom:-35px;width:160px;height:160px;border-radius:9999px;border:18px solid rgba(59,130,246,0.35);"></div>
                <!-- Soft Center Glow -->
                <div style="position:absolute;top:8%;left:50%;transform:translateX(-50%);width:70%;height:45%;border-radius:50%;background:radial-gradient(ellipse, rgba(147,197,253,0.3) 0%, transparent 70%);"></div>
            </div>

            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-4 sm:py-6 w-full relative z-10">
                <!-- Top Logo Badge (White Pill) -->
                <div class="ppt-anim-1 flex justify-center mb-3">
                    <div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-white shadow-xl">'''

slide_1_new = '''        <section id="slide-1" class="ppt-slide slide-next bg-curtain-blue select-none">
            <!-- THEATRICAL STAGE BACKGROUND: Spotlight Beams, Star Bursts & Stardust -->
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
                <svg style="position:absolute;left:4%;top:50%;opacity:0.35;" width="50" height="50" viewBox="0 0 100 100" fill="none">
                    <path d="M50 0 L55 38 L93 15 L62 45 L100 50 L62 55 L93 85 L55 62 L50 100 L45 62 L7 85 L38 55 L0 50 L38 45 L7 15 L45 38 Z" fill="#93c5fd"/>
                </svg>
                <!-- Bottom Right Accent Ring -->
                <div style="position:absolute;right:-35px;bottom:-35px;width:160px;height:160px;border-radius:9999px;border:18px solid rgba(59,130,246,0.35);"></div>
                <!-- Soft Center Glow -->
                <div style="position:absolute;top:8%;left:50%;transform:translateX(-50%);width:70%;height:45%;border-radius:50%;background:radial-gradient(ellipse, rgba(147,197,253,0.3) 0%, transparent 70%);"></div>
            </div>

            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-4 sm:py-6 w-full relative z-10">
                <!-- Top Logo Badge (White Pill) -->
                <div class="ppt-anim-1 flex justify-center mb-3">
                    <div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-white shadow-xl animate-float-gentle">'''

content = content.replace(slide_1_old, slide_1_new, 1)

# Tambahkan animasi bullseye icon dan main card di slide 1
slide_1_card_old = '''                <!-- Single Clean, Natural, High-Contrast Tujuan Card -->
                <div class="ppt-anim-2 max-w-3xl mx-auto w-full">
                    <div class="rounded-3xl sm:rounded-[2.5rem] p-7 sm:p-12 bg-white shadow-2xl border-4 border-white/95 text-center">
                        
                        <!-- Top Icon Badge -->
                        <div class="w-14 h-14 sm:w-16 sm:h-16 mx-auto mb-5 rounded-2xl bg-[#0c2363] text-white flex items-center justify-center text-2xl sm:text-3xl shadow-lg shadow-blue-900/30">
                            <i class="fa-solid fa-bullseye"></i>
                        </div>'''

slide_1_card_new = '''                <!-- Single Clean, Natural, High-Contrast Tujuan Card -->
                <div class="ppt-anim-2 max-w-3xl mx-auto w-full">
                    <div class="rounded-3xl sm:rounded-[2.5rem] p-7 sm:p-12 bg-white shadow-2xl border-4 border-white/95 text-center animate-float-gentle hover:shadow-cyan-400/40 transition-all duration-300">
                        
                        <!-- Top Icon Badge -->
                        <div class="w-14 h-14 sm:w-16 sm:h-16 mx-auto mb-5 rounded-2xl bg-[#0c2363] text-white flex items-center justify-center text-2xl sm:text-3xl shadow-lg shadow-blue-900/30 animate-icon-bounce">
                            <i class="fa-solid fa-bullseye text-cyan-300"></i>
                        </div>'''

content = content.replace(slide_1_card_old, slide_1_card_new, 1)

# ==========================================
# 2. UPGRADE SLIDE-2 (Sejarah HIMATANBU)
# ==========================================
# Tambahkan animate-float-newspaper, animate-float-1,2,3, dan stagger animations
slide_2_koran_old = '''                    <!-- Kolom Kiri: Visual Kliping Koran / Arsip Resmi -->
                    <div class="lg:col-span-5 flex flex-col items-center">
                        <div class="relative group rounded-3xl p-3 sm:p-4 bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-[0_20px_50px_rgba(0,0,0,0.5)] border-2 border-white/80 dark:border-blue-400/40 hover:shadow-cyan-400/30 hover:scale-[1.02] transition-all duration-300 max-w-md w-full cursor-pointer" onclick="openPhotoModal()" title="Klik untuk memperbesar arsip koran">'''

slide_2_koran_new = '''                    <!-- Kolom Kiri: Visual Kliping Koran / Arsip Resmi -->
                    <div class="lg:col-span-5 flex flex-col items-center">
                        <div class="relative group rounded-3xl p-3 sm:p-4 bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-[0_20px_50px_rgba(0,0,0,0.5)] border-2 border-white/80 dark:border-blue-400/40 hover:shadow-cyan-400/30 hover:scale-[1.02] transition-all duration-300 max-w-md w-full cursor-pointer animate-float-newspaper" onclick="openPhotoModal()" title="Klik untuk memperbesar arsip koran">'''

content = content.replace(slide_2_koran_old, slide_2_koran_new, 1)

# Update 3 highlight cards di slide 2 dengan animate-float-1, 2, 3
slide_2_highlights_old = '''                        <!-- 3 Kotak Sorotan Cepat Prestisius -->
                        <div class="grid grid-cols-3 gap-2 w-full max-w-md mt-3">
                            <div class="rounded-2xl p-2.5 text-center bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-[0_8px_20px_rgba(0,0,0,0.3)] border border-white/60 dark:border-blue-500/30 hover:-translate-y-1 transition-all">
                                <div class="text-[9px] text-[#091e52]/70 dark:text-cyan-300 uppercase font-black tracking-wider">Tahun Berdiri</div>
                                <div class="text-sm sm:text-base font-heading font-black text-[#091e52] dark:text-white">2012</div>
                            </div>
                            <div class="rounded-2xl p-2.5 text-center bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-[0_8px_20px_rgba(0,0,0,0.3)] border border-white/60 dark:border-blue-500/30 hover:-translate-y-1 transition-all">
                                <div class="text-[9px] text-[#091e52]/70 dark:text-cyan-300 uppercase font-black tracking-wider">Basis Awal</div>
                                <div class="text-sm sm:text-base font-heading font-black text-amber-500 dark:text-amber-400 truncate" title="Asrama Mandastana">Mandastana</div>
                            </div>
                            <div class="rounded-2xl p-2.5 text-center bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-[0_8px_20px_rgba(0,0,0,0.3)] border border-white/60 dark:border-blue-500/30 hover:-translate-y-1 transition-all">
                                <div class="text-[9px] text-[#091e52]/70 dark:text-cyan-300 uppercase font-black tracking-wider">Perintis</div>
                                <div class="text-sm sm:text-base font-heading font-black text-emerald-600 dark:text-emerald-400">7 Mahasiswa</div>
                            </div>
                        </div>'''

slide_2_highlights_new = '''                        <!-- 3 Kotak Sorotan Cepat Prestisius -->
                        <div class="grid grid-cols-3 gap-2 w-full max-w-md mt-3">
                            <div class="rounded-2xl p-2.5 text-center bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-[0_8px_20px_rgba(0,0,0,0.3)] border border-white/60 dark:border-blue-500/30 hover:-translate-y-1 transition-all animate-float-1">
                                <div class="text-[9px] text-[#091e52]/70 dark:text-cyan-300 uppercase font-black tracking-wider">Tahun Berdiri</div>
                                <div class="text-sm sm:text-base font-heading font-black text-[#091e52] dark:text-white">2012</div>
                            </div>
                            <div class="rounded-2xl p-2.5 text-center bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-[0_8px_20px_rgba(0,0,0,0.3)] border border-white/60 dark:border-blue-500/30 hover:-translate-y-1 transition-all animate-float-2">
                                <div class="text-[9px] text-[#091e52]/70 dark:text-cyan-300 uppercase font-black tracking-wider">Basis Awal</div>
                                <div class="text-sm sm:text-base font-heading font-black text-amber-500 dark:text-amber-400 truncate" title="Asrama Mandastana">Mandastana</div>
                            </div>
                            <div class="rounded-2xl p-2.5 text-center bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-[0_8px_20px_rgba(0,0,0,0.3)] border border-white/60 dark:border-blue-500/30 hover:-translate-y-1 transition-all animate-float-3">
                                <div class="text-[9px] text-[#091e52]/70 dark:text-cyan-300 uppercase font-black tracking-wider">Perintis</div>
                                <div class="text-sm sm:text-base font-heading font-black text-emerald-600 dark:text-emerald-400">7 Mahasiswa</div>
                            </div>
                        </div>'''

content = content.replace(slide_2_highlights_old, slide_2_highlights_new, 1)

# Tambahkan stagger classes pada 4 poin sejarah di Slide 2
slide_2_narrative_old = '''                        <!-- Poin 1 -->
                        <div class="rounded-2xl p-3.5 sm:p-4 bg-white/95 dark:bg-slate-900/85 backdrop-blur-md shadow-[0_12px_28px_rgba(0,0,0,0.35)] border border-white/60 dark:border-blue-500/30 border-l-4 border-l-emerald-500 hover:-translate-y-0.5 hover:shadow-cyan-500/25 transition-all duration-300">'''

slide_2_narrative_new = '''                        <!-- Poin 1 -->
                        <div class="stagger-1 rounded-2xl p-3.5 sm:p-4 bg-white/95 dark:bg-slate-900/85 backdrop-blur-md shadow-[0_12px_28px_rgba(0,0,0,0.35)] border border-white/60 dark:border-blue-500/30 border-l-4 border-l-emerald-500 hover:-translate-y-0.5 hover:shadow-cyan-500/25 transition-all duration-300 animate-float-gentle">'''

content = content.replace(slide_2_narrative_old, slide_2_narrative_new, 1)

slide_2_p2_old = '''                        <!-- Poin 2 -->
                        <div class="rounded-2xl p-3.5 sm:p-4 bg-white/95 dark:bg-slate-900/85 backdrop-blur-md shadow-[0_12px_28px_rgba(0,0,0,0.35)] border border-white/60 dark:border-blue-500/30 border-l-4 border-l-teal-500 hover:-translate-y-0.5 hover:shadow-cyan-500/25 transition-all duration-300">'''

slide_2_p2_new = '''                        <!-- Poin 2 -->
                        <div class="stagger-2 rounded-2xl p-3.5 sm:p-4 bg-white/95 dark:bg-slate-900/85 backdrop-blur-md shadow-[0_12px_28px_rgba(0,0,0,0.35)] border border-white/60 dark:border-blue-500/30 border-l-4 border-l-teal-500 hover:-translate-y-0.5 hover:shadow-cyan-500/25 transition-all duration-300">'''

content = content.replace(slide_2_p2_old, slide_2_p2_new, 1)

slide_2_p3_old = '''                        <!-- Poin 3: Hari Jadi (Special Gold Glow Highlight) -->
                        <div class="rounded-2xl p-3.5 sm:p-4 bg-gradient-to-r from-amber-400/20 via-white/95 to-white/95 dark:from-amber-500/20 dark:via-slate-900/90 dark:to-slate-900/90 backdrop-blur-md shadow-[0_15px_35px_rgba(245,158,11,0.25)] border-2 border-amber-400/80 border-l-4 border-l-amber-500 hover:-translate-y-0.5 hover:shadow-amber-500/30 transition-all duration-300">'''

slide_2_p3_new = '''                        <!-- Poin 3: Hari Jadi (Special Gold Glow Highlight) -->
                        <div class="stagger-3 rounded-2xl p-3.5 sm:p-4 bg-gradient-to-r from-amber-400/20 via-white/95 to-white/95 dark:from-amber-500/20 dark:via-slate-900/90 dark:to-slate-900/90 backdrop-blur-md shadow-[0_15px_35px_rgba(245,158,11,0.25)] border-2 border-amber-400/80 border-l-4 border-l-amber-500 hover:-translate-y-0.5 hover:shadow-amber-500/30 transition-all duration-300 animate-pulse-gold">'''

content = content.replace(slide_2_p3_old, slide_2_p3_new, 1)

slide_2_p4_old = '''                        <!-- Poin 4: Peran Berkelanjutan -->
                        <div class="rounded-2xl p-3 sm:p-3.5 bg-white/95 dark:bg-slate-900/85 backdrop-blur-md shadow-[0_12px_28px_rgba(0,0,0,0.35)] border border-white/60 dark:border-blue-500/30 border-l-4 border-l-blue-500 flex items-start gap-3 hover:-translate-y-0.5 hover:shadow-cyan-500/25 transition-all duration-300">'''

slide_2_p4_new = '''                        <!-- Poin 4: Peran Berkelanjutan -->
                        <div class="stagger-4 rounded-2xl p-3 sm:p-3.5 bg-white/95 dark:bg-slate-900/85 backdrop-blur-md shadow-[0_12px_28px_rgba(0,0,0,0.35)] border border-white/60 dark:border-blue-500/30 border-l-4 border-l-blue-500 flex items-start gap-3 hover:-translate-y-0.5 hover:shadow-cyan-500/25 transition-all duration-300">'''

content = content.replace(slide_2_p4_old, slide_2_p4_new, 1)

# Simpan hasil perubahan
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Slide 1 and Slide 2 animation upgrade completed successfully!')

