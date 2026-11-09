import re

html_path = r'D:\Web_Himatanbu_Malang\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# ==============================================================
# TEMPLATE BACKGROUND TEATER ROYAL BLUE SELARAS (GPU SMOOTH)
# ==============================================================
theatrical_bg = '''            <!-- THEATRICAL STAGE BACKGROUND: Spotlight Beams, Star Bursts & Stardust -->
            <div style="position:absolute;inset:0;pointer-events:none;overflow:hidden;">
                <!-- Curtain Shadows -->
                <div style="position:absolute;left:-5%;top:0;bottom:0;width:25%;background:linear-gradient(90deg, rgba(6,22,68,0.55) 0%, rgba(15,48,135,0.2) 60%, transparent 100%);"></div>
                <div style="position:absolute;right:-5%;top:0;bottom:0;width:25%;background:linear-gradient(270deg, rgba(6,22,68,0.55) 0%, rgba(15,48,135,0.2) 60%, transparent 100%);"></div>
                
                <!-- Dual Theatrical Spotlight Beams -->
                <div style="position:absolute;top:0;left:10%;width:260px;height:100%;background:linear-gradient(135deg, rgba(255,255,255,0.14) 0%, rgba(96,165,250,0.06) 50%, transparent 80%);transform:rotate(-14deg);transform-origin:top left;"></div>
                <div style="position:absolute;top:0;right:10%;width:260px;height:100%;background:linear-gradient(225deg, rgba(255,255,255,0.14) 0%, rgba(96,165,250,0.06) 50%, transparent 80%);transform:rotate(14deg);transform-origin:top right;"></div>

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

# ==============================================================
# SLIDE BARU 1: BIDANG PKA (Pengembangan Kualitas Anggota)
# ==============================================================
slide_pka = f'''
        <!-- ==========================================
             SLIDE 5: BIDANG PKA
             ========================================== -->
        <section id="slide-4" class="ppt-slide slide-next bg-curtain-blue select-none">
{theatrical_bg}
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-4 sm:py-6 w-full relative z-10">
                <!-- Header Slide -->
                <div class="ppt-anim-1 text-center max-w-3xl mx-auto mb-4 sm:mb-6">
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white text-[#091e52] font-black text-xs tracking-wider uppercase shadow-[0_10px_25px_rgba(0,0,0,0.35)] border border-blue-200/60 mb-2 animate-float-gentle">
                        <i class="fa-solid fa-graduation-cap text-emerald-500"></i>
                        <span>Slide 05 • Bidang 01</span>
                    </div>
                    <h3 class="text-3xl sm:text-5xl font-heading font-black text-chrome-himatanbu tracking-wide animate-shine mt-1">
                        BIDANG PKA
                    </h3>
                    <p class="text-amber-300 font-extrabold text-sm sm:text-base tracking-wider uppercase drop-shadow mt-0.5">
                        Pengembangan Kualitas Anggota
                    </p>
                    <p class="text-blue-100/90 text-xs sm:text-sm font-medium mt-1">
                        Pilar kaderisasi, pembentukan karakter, kepemimpinan, dan peningkatan kapasitas intelektual mahasiswa perantau.
                    </p>
                </div>

                <!-- Konten Grid: Visi Fokus & Program Kerja Unggulan -->
                <div class="ppt-anim-2 grid grid-cols-1 lg:grid-cols-12 gap-4 sm:gap-6 items-stretch">
                    <!-- Kolom Kiri: Profil & Peran Bidang -->
                    <div class="lg:col-span-5 flex flex-col justify-between p-5 sm:p-6 rounded-3xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-2xl border-2 border-white/80 dark:border-emerald-500/30 animate-float-gentle">
                        <div>
                            <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-200 dark:border-slate-800">
                                <span class="px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300 font-black text-xs uppercase flex items-center gap-1.5">
                                    <i class="fa-solid fa-shield-halved text-emerald-600"></i> FOKUS KADERISASI
                                </span>
                                <span class="text-xs font-bold text-slate-500 dark:text-slate-400">Periode 2026/2027</span>
                            </div>
                            <h4 class="text-lg sm:text-xl font-heading font-black text-[#091e52] dark:text-white mb-2">
                                Membentuk Kader Unggul & Berkarakter
                            </h4>
                            <p class="text-xs sm:text-sm text-slate-700 dark:text-blue-100/90 leading-relaxed mb-4">
                                Bertanggung jawab penuh dalam mengawal regenerasi, pembinaan mental, nilai-nilai kekeluargaan, serta loyalitas anggota terhadap himpunan dan daerah asal Kabupaten Tanah Bumbu.
                            </p>
                        </div>

                        <!-- Badge Poin Utama PKA -->
                        <div class="space-y-2 pt-2 border-t border-slate-200 dark:border-slate-800">
                            <div class="flex items-center gap-2.5 text-xs font-bold text-slate-800 dark:text-slate-200">
                                <i class="fa-solid fa-circle-check text-emerald-500"></i>
                                <span>Kaderisasi Bertahap & Berkelanjutan</span>
                            </div>
                            <div class="flex items-center gap-2.5 text-xs font-bold text-slate-800 dark:text-slate-200">
                                <i class="fa-solid fa-circle-check text-emerald-500"></i>
                                <span>Pelatihan Soft Skills & Leadership</span>
                            </div>
                            <div class="flex items-center gap-2.5 text-xs font-bold text-slate-800 dark:text-slate-200">
                                <i class="fa-solid fa-circle-check text-emerald-500"></i>
                                <span>Pendampingan Akademik Mahasiswa Rantau</span>
                            </div>
                        </div>
                    </div>

                    <!-- Kolom Kanan: Rencana Program Kerja PKA -->
                    <div class="lg:col-span-7 flex flex-col gap-3">
                        <!-- Proker 1 -->
                        <div class="p-4 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-emerald-500 hover:-translate-y-1 transition-all">
                            <div class="flex items-center justify-between mb-1">
                                <h5 class="text-sm sm:text-base font-heading font-black text-[#091e52] dark:text-white flex items-center gap-2">
                                    <i class="fa-solid fa-seedling text-emerald-500"></i> Latihan Keterampilan Manajemen Mahasiswa (LKMM)
                                </h5>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-extrabold uppercase">Wajib</span>
                            </div>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                                Pelatihan kepemimpinan dasar, manajemen organisasi, persidangan, dan analisis problem solving bagi seluruh kader baru HIMATANBU Malang.
                            </p>
                        </div>

                        <!-- Proker 2 -->
                        <div class="p-4 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-teal-500 hover:-translate-y-1 transition-all">
                            <div class="flex items-center justify-between mb-1">
                                <h5 class="text-sm sm:text-base font-heading font-black text-[#091e52] dark:text-white flex items-center gap-2">
                                    <i class="fa-solid fa-chalkboard-user text-teal-500"></i> Upgrading & Workshop Keorganisasian
                                </h5>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-teal-100 text-teal-800 font-extrabold uppercase">Internal</span>
                            </div>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                                Penguatan kapasitas internal pengurus dalam hal administrasi, manajemen waktu, public speaking, dan kerja sama tim.
                            </p>
                        </div>

                        <!-- Proker 3 -->
                        <div class="p-4 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-amber-500 hover:-translate-y-1 transition-all">
                            <div class="flex items-center justify-between mb-1">
                                <h5 class="text-sm sm:text-base font-heading font-black text-[#091e52] dark:text-white flex items-center gap-2">
                                    <i class="fa-solid fa-hand-holding-heart text-amber-500"></i> Mentorship & Pendampingan Maba
                                </h5>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-amber-100 text-amber-800 font-extrabold uppercase">Rutin</span>
                            </div>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                                Pendampingan belajar dan sharing session lintas angkatan guna membantu mahasiswa baru beradaptasi dengan iklim perkuliahan di Kota Malang.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# ==============================================================
# SLIDE BARU 2: BIDANG SKMB (Silaturahmi Kreativitas Minat dan Bakat)
# ==============================================================
slide_skmb = f'''
        <!-- ==========================================
             SLIDE 6: BIDANG SKMB
             ========================================== -->
        <section id="slide-5" class="ppt-slide slide-next bg-curtain-blue select-none">
{theatrical_bg}
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-4 sm:py-6 w-full relative z-10">
                <!-- Header Slide -->
                <div class="ppt-anim-1 text-center max-w-3xl mx-auto mb-4 sm:mb-6">
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white text-[#091e52] font-black text-xs tracking-wider uppercase shadow-[0_10px_25px_rgba(0,0,0,0.35)] border border-blue-200/60 mb-2 animate-float-gentle">
                        <i class="fa-solid fa-palette text-amber-500"></i>
                        <span>Slide 06 • Bidang 02</span>
                    </div>
                    <h3 class="text-3xl sm:text-5xl font-heading font-black text-chrome-himatanbu tracking-wide animate-shine mt-1">
                        BIDANG SKMB
                    </h3>
                    <p class="text-amber-300 font-extrabold text-sm sm:text-base tracking-wider uppercase drop-shadow mt-0.5">
                        Silaturahmi, Kreativitas, Minat & Bakat
                    </p>
                    <p class="text-blue-100/90 text-xs sm:text-sm font-medium mt-1">
                        Wadah pengikat kekeluargaan, penyaluran minat bakat seni & olahraga, serta kepedulian sosial masyarakat.
                    </p>
                </div>

                <!-- Konten Grid: 2 Departemen Utama & Program Kerja Resmi -->
                <div class="ppt-anim-2 grid grid-cols-1 lg:grid-cols-12 gap-4 sm:gap-6 items-stretch">
                    <!-- Kolom Kiri: 2 Departemen Naungan SKMB -->
                    <div class="lg:col-span-5 flex flex-col gap-3 justify-between">
                        <!-- Dept 1 -->
                        <div class="p-4 rounded-3xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-xl border-2 border-white/80 dark:border-amber-500/30 animate-float-1">
                            <div class="flex items-center gap-3 mb-2">
                                <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-500 to-yellow-400 text-slate-950 flex items-center justify-center text-lg font-black shadow-md">
                                    <i class="fa-solid fa-futbol"></i>
                                </div>
                                <div>
                                    <h4 class="font-heading font-black text-sm sm:text-base text-[#091e52] dark:text-white">Dept. Kesenian & Olahraga</h4>
                                    <span class="text-[10px] text-amber-600 font-extrabold uppercase">Apresiasi Bakat & Sportivitas</span>
                                </div>
                            </div>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                                Menampung dan memfasilitasi bakat seni, budaya daerah Banjar/Tanbu, serta kebugaran olahraga antar anggota dan ormada.
                            </p>
                        </div>

                        <!-- Dept 2 -->
                        <div class="p-4 rounded-3xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-xl border-2 border-white/80 dark:border-rose-500/30 animate-float-2">
                            <div class="flex items-center gap-3 mb-2">
                                <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-rose-500 to-pink-500 text-white flex items-center justify-center text-lg font-black shadow-md">
                                    <i class="fa-solid fa-handshake-angle"></i>
                                </div>
                                <div>
                                    <h4 class="font-heading font-black text-sm sm:text-base text-[#091e52] dark:text-white">Dept. Kesejahteraan Masyarakat</h4>
                                    <span class="text-[10px] text-rose-600 font-extrabold uppercase">Kepedulian Sosial & Lingkungan</span>
                                </div>
                            </div>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                                Menggerakkan kepedulian sosial, aksi kemanusiaan, pengabdian masyarakat, dan penguatan tali persaudaraan rukun tetangga perantauan.
                            </p>
                        </div>
                    </div>

                    <!-- Kolom Kanan: Program Kerja Nyata (Sesuai LPJ SKMB Resmi) -->
                    <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div class="p-3.5 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-amber-500 hover:-translate-y-1 transition-all">
                            <span class="text-[10px] font-black text-amber-600 uppercase">Turnamen Antar ORDA</span>
                            <h5 class="text-xs sm:text-sm font-heading font-black text-[#091e52] dark:text-white mt-0.5">ORDA Unity Games</h5>
                            <p class="text-[11px] text-slate-600 dark:text-slate-300 mt-1 leading-snug">
                                Turnamen E-Sport (Mobile Legends) dan fun sport bersama 8 Organisasi Daerah se-Indonesia di Malang.
                            </p>
                        </div>

                        <div class="p-3.5 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-emerald-500 hover:-translate-y-1 transition-all">
                            <span class="text-[10px] font-black text-emerald-600 uppercase">Pengabdian Sosial</span>
                            <h5 class="text-xs sm:text-sm font-heading font-black text-[#091e52] dark:text-white mt-0.5">Aksi Berdampak</h5>
                            <p class="text-[11px] text-slate-600 dark:text-slate-300 mt-1 leading-snug">
                                Kegiatan senam sehat ceria dan bakti sosial bersama anak-anak sekolah dasar dan warga sekitar asrama.
                            </p>
                        </div>

                        <div class="p-3.5 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-teal-500 hover:-translate-y-1 transition-all">
                            <span class="text-[10px] font-black text-teal-600 uppercase">Kebugaran Rutin</span>
                            <h5 class="text-xs sm:text-sm font-heading font-black text-[#091e52] dark:text-white mt-0.5">Aktif Bersama HIMATANBU</h5>
                            <p class="text-[11px] text-slate-600 dark:text-slate-300 mt-1 leading-snug">
                                Latihan rutin futsal, badminton, dan jogging bersama demi menjaga kebugaran jasmani seluruh anggota.
                            </p>
                        </div>

                        <div class="p-3.5 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-blue-500 hover:-translate-y-1 transition-all">
                            <span class="text-[10px] font-black text-blue-600 uppercase">Keluarga & Relasi</span>
                            <h5 class="text-xs sm:text-sm font-heading font-black text-[#091e52] dark:text-white mt-0.5">Study Lembaga & Escape to Nature</h5>
                            <p class="text-[11px] text-slate-600 dark:text-slate-300 mt-1 leading-snug">
                                Kunjungan sharing wawasan kerja bersama alumni serta camping keakraban alam terbuka untuk mempererat persaudaraan.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# ==============================================================
# SLIDE BARU 3: BIDANG INFOKOM (Informasi dan Komunikasi)
# ==============================================================
slide_infokom = f'''
        <!-- ==========================================
             SLIDE 7: BIDANG INFOKOM
             ========================================== -->
        <section id="slide-6" class="ppt-slide slide-next bg-curtain-blue select-none">
{theatrical_bg}
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 my-0 lg:my-auto py-4 sm:py-6 w-full relative z-10">
                <!-- Header Slide -->
                <div class="ppt-anim-1 text-center max-w-3xl mx-auto mb-4 sm:mb-6">
                    <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white text-[#091e52] font-black text-xs tracking-wider uppercase shadow-[0_10px_25px_rgba(0,0,0,0.35)] border border-blue-200/60 mb-2 animate-float-gentle">
                        <i class="fa-solid fa-bullhorn text-cyan-500"></i>
                        <span>Slide 07 • Bidang 03</span>
                    </div>
                    <h3 class="text-3xl sm:text-5xl font-heading font-black text-chrome-himatanbu tracking-wide animate-shine mt-1">
                        BIDANG INFOKOM
                    </h3>
                    <p class="text-amber-300 font-extrabold text-sm sm:text-base tracking-wider uppercase drop-shadow mt-0.5">
                        Informasi & Komunikasi
                    </p>
                    <p class="text-blue-100/90 text-xs sm:text-sm font-medium mt-1">
                        Corong publikasi digital, penghubung jaringan komunikasi, dan pengelola citra positif organisasi.
                    </p>
                </div>

                <!-- Konten Grid: Pilar Media & Program Kerja Infokom -->
                <div class="ppt-anim-2 grid grid-cols-1 lg:grid-cols-12 gap-4 sm:gap-6 items-stretch">
                    <!-- Kolom Kiri: Profil & Peran Strategis Infokom -->
                    <div class="lg:col-span-5 flex flex-col justify-between p-5 sm:p-6 rounded-3xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-2xl border-2 border-white/80 dark:border-cyan-500/30 animate-float-gentle">
                        <div>
                            <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-200 dark:border-slate-800">
                                <span class="px-3 py-1 rounded-full bg-cyan-100 text-cyan-800 dark:bg-cyan-950/60 dark:text-cyan-300 font-black text-xs uppercase flex items-center gap-1.5">
                                    <i class="fa-solid fa-tower-broadcast text-cyan-600"></i> MEDIA & HUBUNGAN LUAR
                                </span>
                                <span class="text-xs font-bold text-slate-500 dark:text-slate-400">Periode 2026/2027</span>
                            </div>
                            <h4 class="text-lg sm:text-xl font-heading font-black text-[#091e52] dark:text-white mb-2">
                                Wajah & Suara HIMATANBU Malang
                            </h4>
                            <p class="text-xs sm:text-sm text-slate-700 dark:text-blue-100/90 leading-relaxed mb-4">
                                Mengelola seluruh saluran informasi resmi (media sosial, website profil, publikasi arsip, dan siaran pers) serta menjadi jembatan diplomasi kemitraan dengan Pemkab Tanah Bumbu, alumni, kampus, dan sesama ormada.
                            </p>
                        </div>

                        <!-- 3 Kanal Digital Utama -->
                        <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-200 dark:border-slate-800 text-center">
                            <div class="p-2 rounded-xl bg-blue-50 dark:bg-slate-800">
                                <i class="fa-brands fa-instagram text-pink-600 text-lg"></i>
                                <div class="text-[10px] font-bold text-slate-700 dark:text-slate-200 mt-1">Instagram</div>
                            </div>
                            <div class="p-2 rounded-xl bg-blue-50 dark:bg-slate-800">
                                <i class="fa-solid fa-globe text-cyan-600 text-lg"></i>
                                <div class="text-[10px] font-bold text-slate-700 dark:text-slate-200 mt-1">Website</div>
                            </div>
                            <div class="p-2 rounded-xl bg-blue-50 dark:bg-slate-800">
                                <i class="fa-solid fa-podcast text-emerald-600 text-lg"></i>
                                <div class="text-[10px] font-bold text-slate-700 dark:text-slate-200 mt-1">Podcast</div>
                            </div>
                        </div>
                    </div>

                    <!-- Kolom Kanan: Rencana Program Kerja Infokom -->
                    <div class="lg:col-span-7 flex flex-col gap-3">
                        <!-- Proker 1 -->
                        <div class="p-4 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-cyan-500 hover:-translate-y-1 transition-all">
                            <div class="flex items-center justify-between mb-1">
                                <h5 class="text-sm sm:text-base font-heading font-black text-[#091e52] dark:text-white flex items-center gap-2">
                                    <i class="fa-solid fa-microphone-lines text-cyan-500"></i> Podcast Rantau & Dialog Inspiratif
                                </h5>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-cyan-100 text-cyan-800 font-extrabold uppercase">Media</span>
                            </div>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                                Konten bincang interaktif mengangkat kisah sukses mahasiswa perantau, sharing beasiswa pemda, info dunia kerja, dan kiprah tokoh daerah.
                            </p>
                        </div>

                        <!-- Proker 2 -->
                        <div class="p-4 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-blue-500 hover:-translate-y-1 transition-all">
                            <div class="flex items-center justify-between mb-1">
                                <h5 class="text-sm sm:text-base font-heading font-black text-[#091e52] dark:text-white flex items-center gap-2">
                                    <i class="fa-solid fa-laptop-code text-blue-500"></i> Digitalisasi Data & Portal Ormada
                                </h5>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-extrabold uppercase">Teknologi</span>
                            </div>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                                Pengelolaan platform website modern, pendataan anggota digital secara berkala, dan penyediaan dokumen arsip sejarah himpunan secara transparan.
                            </p>
                        </div>

                        <!-- Proker 3 -->
                        <div class="p-4 rounded-2xl bg-white/95 dark:bg-slate-900/90 backdrop-blur-md shadow-lg border-l-4 border-l-emerald-500 hover:-translate-y-1 transition-all">
                            <div class="flex items-center justify-between mb-1">
                                <h5 class="text-sm sm:text-base font-heading font-black text-[#091e52] dark:text-white flex items-center gap-2">
                                    <i class="fa-solid fa-handshake text-emerald-500"></i> Publikasi Prestasi & Humas Antar Lembaga
                                </h5>
                                <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-extrabold uppercase">Humas</span>
                            </div>
                            <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                                Penyebaran informasi berkala mengenai kabar Tanah Bumbu, perayaan hari besar nasional/keagamaan, ucapan wisuda, serta jalinan komunikasi antar ormada di Malang.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

# Ganti slide-4 lama menjadi slide-7 (Daftar Anggota)
text = text.replace('<section id="slide-4" class="ppt-slide slide-next bg-curtain-blue select-none">', '<section id="slide-7" class="ppt-slide slide-next bg-curtain-blue select-none">')
text = text.replace('<span>Slide 05 • Direktori Anggota</span>', '<span>Slide 08 • Direktori Anggota</span>')

# Ganti slide-5 lama menjadi slide-8 (Program Kerja & Asrama)
text = text.replace('<section id="slide-5" class="ppt-slide slide-next bg-curtain-blue select-none">', '<section id="slide-8" class="ppt-slide slide-next bg-curtain-blue select-none">')
text = text.replace('<span>Slide 06 • Agenda & Dedikasi</span>', '<span>Slide 09 • Agenda & Dedikasi</span>')

# Sisipkan 3 slide baru tepat setelah </section> milik slide-3
slide_3_end = '</section>\n\n        <!-- ==========================================\n             SLIDE 5: DAFTAR PENGURUS'
if slide_3_end not in text:
    # Cari dengan regex
    match = re.search(r'(<section id="slide-3".*?</section>)', text, re.DOTALL)
    if match:
        target = match.group(1)
        text = text.replace(target, target + '\n' + slide_pka + '\n' + slide_skmb + '\n' + slide_infokom)
        print('Inserted 3 slides via regex match')
else:
    text = text.replace(slide_3_end, '</section>\n' + slide_pka + '\n' + slide_skmb + '\n' + slide_infokom + '\n\n        <!-- ==========================================\n             SLIDE 8: DAFTAR PENGURUS')
    print('Inserted 3 slides via exact target')

# ==============================================================
# UPDATE JS SLIDE SYSTEM & SIDEBAR NAVIGATION
# ==============================================================
# Update totalSlides & slideNames
old_slide_names = '''        const slideNames = [
            "Beranda & Ringkasan",
            "Tujuan Organisasi",
            "Sejarah HIMATANBU",
            "Bagan Struktur Pohon",
            "Daftar Anggota Muda (2026)",
            "Program Kerja & Asrama"
        ];
        const totalSlides = 6;
        let currentSlide = 0;
        const slides = [
            document.getElementById('slide-0'),
            document.getElementById('slide-1'),
            document.getElementById('slide-2'),
            document.getElementById('slide-3'),
            document.getElementById('slide-4'),
            document.getElementById('slide-5')
        ];'''

new_slide_names = '''        const slideNames = [
            "Beranda & Ringkasan",
            "Tujuan Organisasi",
            "Sejarah HIMATANBU",
            "Bagan Struktur Pohon",
            "Bidang PKA (Kaderisasi)",
            "Bidang SKMB (Bakat & Sosial)",
            "Bidang INFOKOM (Media)",
            "Daftar Anggota Muda (2026)",
            "Program Kerja & Asrama"
        ];
        const totalSlides = 9;
        let currentSlide = 0;
        const slides = [
            document.getElementById('slide-0'),
            document.getElementById('slide-1'),
            document.getElementById('slide-2'),
            document.getElementById('slide-3'),
            document.getElementById('slide-4'),
            document.getElementById('slide-5'),
            document.getElementById('slide-6'),
            document.getElementById('slide-7'),
            document.getElementById('slide-8')
        ];'''

text = text.replace(old_slide_names, new_slide_names, 1)

# Update sidebar navigation menu
old_nav = '''                <nav class="flex flex-col gap-1.5 w-full">
                    <button onclick="goToSlide(0); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2.5 rounded-xl font-bold text-xs flex items-center gap-3 transition-all" data-slide="0">
                        <i class="fa-solid fa-house w-4 text-center"></i>
                        <span class="flex-1 truncate">1. Beranda</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(1); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2.5 rounded-xl font-bold text-xs flex items-center gap-3 transition-all" data-slide="1">
                        <i class="fa-solid fa-bullseye w-4 text-center"></i>
                        <span class="flex-1 truncate">2. Tujuan Organisasi</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(2); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2.5 rounded-xl font-bold text-xs flex items-center gap-3 transition-all" data-slide="2">
                        <i class="fa-solid fa-clock-rotate-left w-4 text-center"></i>
                        <span class="flex-1 truncate">3. Sejarah</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(3); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2.5 rounded-xl font-bold text-xs flex items-center gap-3 transition-all" data-slide="3">
                        <i class="fa-solid fa-sitemap w-4 text-center"></i>
                        <span class="flex-1 truncate">4. Bagan Struktur</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(4); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2.5 rounded-xl font-bold text-xs flex items-center gap-3 transition-all" data-slide="4">
                        <i class="fa-solid fa-users w-4 text-center"></i>
                        <span class="flex-1 truncate">5. Daftar Anggota</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(5); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2.5 rounded-xl font-bold text-xs flex items-center gap-3 transition-all" data-slide="5">
                        <i class="fa-solid fa-clipboard-list w-4 text-center"></i>
                        <span class="flex-1 truncate">6. Program Kerja</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                </nav>'''

new_nav = '''                <nav class="flex flex-col gap-1.5 w-full">
                    <button onclick="goToSlide(0); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2 rounded-xl font-bold text-xs flex items-center gap-2.5 transition-all" data-slide="0">
                        <i class="fa-solid fa-house w-4 text-center"></i>
                        <span class="flex-1 truncate">1. Beranda</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(1); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2 rounded-xl font-bold text-xs flex items-center gap-2.5 transition-all" data-slide="1">
                        <i class="fa-solid fa-bullseye w-4 text-center"></i>
                        <span class="flex-1 truncate">2. Tujuan Organisasi</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(2); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2 rounded-xl font-bold text-xs flex items-center gap-2.5 transition-all" data-slide="2">
                        <i class="fa-solid fa-clock-rotate-left w-4 text-center"></i>
                        <span class="flex-1 truncate">3. Sejarah</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(3); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2 rounded-xl font-bold text-xs flex items-center gap-2.5 transition-all" data-slide="3">
                        <i class="fa-solid fa-sitemap w-4 text-center"></i>
                        <span class="flex-1 truncate">4. Bagan Struktur</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(4); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2 rounded-xl font-bold text-xs flex items-center gap-2.5 transition-all" data-slide="4">
                        <i class="fa-solid fa-graduation-cap w-4 text-center text-emerald-500"></i>
                        <span class="flex-1 truncate">5. Bidang PKA</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(5); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2 rounded-xl font-bold text-xs flex items-center gap-2.5 transition-all" data-slide="5">
                        <i class="fa-solid fa-palette w-4 text-center text-amber-500"></i>
                        <span class="flex-1 truncate">6. Bidang SKMB</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(6); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2 rounded-xl font-bold text-xs flex items-center gap-2.5 transition-all" data-slide="6">
                        <i class="fa-solid fa-bullhorn w-4 text-center text-cyan-500"></i>
                        <span class="flex-1 truncate">7. Bidang INFOKOM</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(7); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2 rounded-xl font-bold text-xs flex items-center gap-2.5 transition-all" data-slide="7">
                        <i class="fa-solid fa-users w-4 text-center"></i>
                        <span class="flex-1 truncate">8. Anggota Muda</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                    <button onclick="goToSlide(8); toggleSidebar(false)" class="nav-tab w-full text-left px-3.5 py-2 rounded-xl font-bold text-xs flex items-center gap-2.5 transition-all" data-slide="8">
                        <i class="fa-solid fa-clipboard-list w-4 text-center"></i>
                        <span class="flex-1 truncate">9. Proker & Asrama</span>
                        <i class="fa-solid fa-chevron-right text-[9px] opacity-40"></i>
                    </button>
                </nav>'''

text = text.replace(old_nav, new_nav, 1)

# Update jumpToDept agar mengarah ke slide yang sesuai (slide 7 adalah daftar anggota)
text = text.replace('goToSlide(4);', 'goToSlide(7);')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Slide additions (PKA, SKMB, INFOKOM) and system updates completed!')

