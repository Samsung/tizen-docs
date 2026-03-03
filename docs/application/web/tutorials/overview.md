<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="theme-color" content="#050507">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <title>ChitraJal | Smart Tv</title>

    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">

    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/shaka-player/4.7.12/shaka-player.ui.js"></script>

    <style>
        :root {
            --bg-body: #050507; --bg-surface: #111116; --primary: #E50914;
            --primary-gradient: linear-gradient(135deg, #e50914 0%, #b80710 100%);
            --glass-border: rgba(255, 255, 255, 0.1); --header-height: 70px; --transition: all 0.3s ease;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: var(--bg-body); color: #fff;
            font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif;
            height: 100vh; width: 100vw; display: flex; flex-direction: column; overflow: hidden;
            overscroll-behavior: none; -webkit-user-select: none; user-select: none;
        }

        /* Header & Logo */
        .logo-box { position: relative; padding: 5px 15px; border-radius: 12px; overflow: hidden; display: inline-flex; align-items: center; justify-content: center; background: #000; text-decoration: none; }
        .logo-box::before { content: ''; position: absolute; width: 150%; height: 150%; background: conic-gradient(transparent, transparent, transparent, #E50914); animation: rotateNeon 2.5s linear infinite; }
        .logo-box::after { content: ''; position: absolute; inset: 2px; background: #050507; border-radius: 10px; z-index: 1; }
        @keyframes rotateNeon { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .snake-svg-logo { position: relative; z-index: 2; overflow: visible; }
        .snake-svg-logo text { font-family: 'Hind Siliguri', sans-serif; font-weight: 800; font-size: 55px; }
        .base-text { fill: rgba(255, 255, 255, 0.1); stroke: rgba(229, 9, 20, 0.15); stroke-width: 1px; }
        .snake-text { fill: transparent; stroke: #E50914; stroke-width: 2.5px; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 40 150; animation: slither 3.5s linear infinite; filter: drop-shadow(0 0 5px #E50914) drop-shadow(0 0 15px #E50914); }
        @keyframes slither { 100% { stroke-dashoffset: -190; } }

        /* Navbar */
        .navbar-custom { height: var(--header-height); background: #000; border-bottom: 1px solid var(--glass-border); padding: 0 20px; display: flex; justify-content: space-between; align-items: center; flex-shrink: 0; }
        .nav-actions { display: flex; align-items: center; gap: 12px; }
        .channel-count { background: rgba(229, 9, 20, 0.15); border: 1px solid rgba(229, 9, 20, 0.5); color: #fff; padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 700; display: none; font-family: 'Hind Siliguri', sans-serif;}
        .sync-btn { background: rgba(255, 255, 255, 0.05); border: 1px solid var(--glass-border); color: white; padding: 8px 18px; border-radius: 50px; cursor: pointer; font-size: 0.85rem; transition: 0.3s; font-weight: 600; display: flex; align-items: center; gap: 8px; font-family: 'Hind Siliguri', sans-serif;}
        .sync-btn:hover, .sync-btn:focus { background: rgba(255,255,255,0.1); outline: none; border-color: var(--primary); }
        .sync-btn i.spin { animation: spin 1s linear infinite; }
        @keyframes spin { 100% { transform: rotate(360deg); } }

        /* Player Area */
        .main-container { display: flex; flex-direction: column; flex-grow: 1; overflow: hidden; }
        .player-area { flex-shrink: 0; background: #000; width: 100%; border-bottom: 1px solid var(--glass-border); display: flex; flex-direction: column; }
        .player-wrapper { width: 100%; aspect-ratio: 16/9; position: relative; background: #000; overflow: hidden; }
        .video-container { width: 100%; height: 100%; position: relative; background: #000; overflow: hidden; display: flex; align-items: center; justify-content: center; }
        #liveVideo { width: 100%; height: 100%; object-fit: contain; }

        /* Custom Controls */
        .controls { position: absolute; bottom: 15px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px; background: rgba(0, 0, 0, 0.7); padding: 8px 15px; border-radius: 30px; z-index: 10; opacity: 0; transition: var(--transition); backdrop-filter: blur(5px); align-items: center; width: max-content; pointer-events: auto; }
        .video-container.controls-hidden .controls { opacity: 0; pointer-events: none; }
        .video-container:not(.controls-hidden) .controls { opacity: 1; pointer-events: auto; }

        .control-btn, .mute-btn, .nav-btn { background: rgba(255, 255, 255, 0.1); color: white; border: none; width: 35px; height: 35px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: var(--transition); font-size: 14px; }
        .control-btn:hover, .mute-btn:hover, .nav-btn:hover, .control-btn:focus, .mute-btn:focus, .nav-btn:focus { background: rgba(255, 255, 255, 0.2); transform: scale(1.1); outline: none; border: 2px solid var(--primary); }
        .nav-btn { width: 40px; height: 40px; background: var(--primary-gradient); }

        .volume-container { display: flex; align-items: center; gap: 5px; }
        .volume-slider { width: 70px; -webkit-appearance: none; height: 4px; border-radius: 2px; background: rgba(255, 255, 255, 0.3); outline: none; cursor: pointer; }
        .volume-slider::-webkit-slider-thumb { -webkit-appearance: none; appearance: none; width: 12px; height: 12px; border-radius: 50%; background: var(--primary); cursor: pointer; }
        .quality-select { border-radius: 20px; padding: 6px 12px; background: rgba(0, 0, 0, 0.7); color: white; border: 1px solid rgba(255, 255, 255, 0.2); font-size: 13px; cursor: pointer; backdrop-filter: blur(5px); display: none; outline: none; font-family: 'Plus Jakarta Sans', sans-serif; }
        .quality-select:focus { border-color: var(--primary); }

        /* Overlays */
        #loadingOverlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.7); color: var(--primary); font-size: 18px; display: none; align-items: center; justify-content: center; z-index: 9; flex-direction: column; gap: 15px; font-weight: bold; }
        .loading-spinner { width: 50px; height: 50px; border: 3px solid rgba(229, 9, 20, 0.3); border-radius: 50%; border-top-color: var(--primary); animation: spin 1s linear infinite; }
        .player-placeholder { position: absolute; inset: 0; background: radial-gradient(circle at center, #111116 0%, #000 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 50; transition: opacity 0.5s ease; pointer-events: none; }
        .player-placeholder p { margin-top: 15px; color: #888; font-size: 1.1rem; animation: pulse 2s infinite; }
        .player-error-overlay { position: absolute; inset: 0; background: rgba(0, 0, 0, 0.95); backdrop-filter: blur(15px); display: none; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 20px; z-index: 1000; font-family: 'Hind Siliguri', sans-serif; }
        .player-error-overlay i { font-size: 3rem; color: var(--primary); margin-bottom: 15px; }

        /* List Area */
        .now-playing-bar { background: #0c0c12; padding: 10px 20px; display: flex; align-items: center; gap: 12px; }
        .live-tag { background: var(--primary); color: white; padding: 3px 8px; border-radius: 4px; font-size: 0.65rem; font-weight: 800; animation: pulseLive 2s infinite; }
        @keyframes pulseLive { 0%, 100% { opacity: 1; box-shadow: 0 0 5px var(--primary); } 50% { opacity: 0.6; box-shadow: none; } }
        .now-playing-text h3 { margin: 0; font-size: 1rem; font-weight: 700; color: #fff; font-family: 'Hind Siliguri', sans-serif;}
        
        .content-area { flex-grow: 1; display: flex; flex-direction: column; overflow: hidden; background: #050507; }
        .search-filter-bar { padding: 15px 15px 10px; display: flex; gap: 10px; flex-shrink: 0; align-items: center; }
        .search-input-wrap { position: relative; flex: 1; }
        .search-input-wrap i { position: absolute; left: 15px; top: 50%; transform: translateY(-50%); color: #888; font-size: 0.9rem;}
        .search-input { width: 100%; background: #121218; border: 1px solid var(--glass-border); color: white; padding: 12px 15px 12px 40px; border-radius: 12px; font-size: 0.95rem; outline: none; transition: 0.3s; font-family: 'Hind Siliguri', sans-serif;}
        .search-input:focus { border-color: var(--primary); background: #1a1a24; }
        .cat-select { background: #121218; border: 1px solid var(--glass-border); color: white; border-radius: 12px; padding: 0 15px; height: 43px; font-weight: 600; outline: none; cursor: pointer; min-width: 130px; font-family: 'Hind Siliguri', sans-serif;}
        .cat-select:focus { border-color: var(--primary); }

        .category-pills-wrapper { display: flex; overflow-x: auto; gap: 10px; padding: 0 15px 15px; border-bottom: 1px solid var(--glass-border); flex-shrink: 0; scrollbar-width: none; -webkit-overflow-scrolling: touch; }
        .category-pills-wrapper::-webkit-scrollbar { display: none; }
        .cat-pill { background: rgba(255,255,255,0.05); color: #ccc; border: 1px solid var(--glass-border); padding: 8px 18px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; white-space: nowrap; transition: 0.3s; font-family: 'Hind Siliguri', sans-serif;}
        .cat-pill.active, .cat-pill:focus { background: rgba(229, 9, 20, 0.2); color: var(--primary); border-color: var(--primary); outline: none; }

        .channels-wrapper { flex-grow: 1; overflow-y: auto; padding: 20px 20px 0 20px; scroll-behavior: smooth; }
        .channels-wrapper::-webkit-scrollbar { width: 5px; }
        .channels-wrapper::-webkit-scrollbar-track { background: #050507; }
        .channels-wrapper::-webkit-scrollbar-thumb { background: #333; border-radius: 10px; }

        .grid-channels { display: grid; grid-template-columns: repeat(auto-fill, minmax(90px, 1fr)); gap: 20px; width: 100%; margin-bottom: 40px; }
        .card-custom { text-decoration: none; display: flex; flex-direction: column; align-items: center; cursor: pointer; color: #fff; outline: none; }
        .card-img-wrap { width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(145deg, #181820, #0d0d12); box-shadow: 4px 4px 10px rgba(0,0,0,0.6), -2px -2px 8px rgba(255,255,255,0.03); display: flex; align-items: center; justify-content: center; padding: 14px; border: 2px solid rgba(255, 255, 255, 0.05); transition: all 0.3s; overflow: hidden; }
        .card-img-wrap img { width: 100%; height: 100%; object-fit: contain; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5)); transition: 0.3s; }
        .card-custom:hover .card-img-wrap, .card-custom.active .card-img-wrap, .card-custom:focus .card-img-wrap { border-color: var(--primary); transform: translateY(-5px) scale(1.05); box-shadow: 0 8px 20px rgba(229, 9, 20, 0.4), inset 0 0 10px rgba(229, 9, 20, 0.1); }
        .card-title { font-size: 0.75rem; font-weight: 700; margin-top: 10px; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: 100%; color: #d1d1d6; transition: 0.3s; font-family: 'Hind Siliguri', sans-serif;}

        .site-footer { padding: 40px 20px 30px; background: var(--bg-body); text-align: center; border-top: 1px solid rgba(255,255,255,0.05); }
        .footer-desc { color: #888; font-size: 0.9rem; max-width: 600px; margin: 0 auto; line-height: 1.5; font-family: 'Hind Siliguri', sans-serif;}
        .footer-credit { margin-top: 20px; font-size: 0.95rem; color: #aaa; font-family: 'Hind Siliguri', sans-serif; }
        .footer-credit a { color: var(--primary); font-weight: 700; text-decoration: none; transition: 0.3s; }

        @media (max-width: 768px) {
            .controls { bottom: 10px; padding: 6px 12px; flex-wrap: wrap; justify-content: center; width: 90%; gap: 5px; }
            .control-btn, .mute-btn { width: 30px; height: 30px; font-size: 12px; }
            .volume-slider { width: 50px; }
            .quality-select { font-size: 11px; padding: 4px 8px; }
        }
        @media (min-width: 900px) {
            .main-container { flex-direction: row; }
            .player-area { width: 65%; border-right: 1px solid var(--glass-border); height: 100%; }
            .content-area { width: 35%; }
            .grid-channels { grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); }
        }
    </style>
</head>
<body>

    <nav class="navbar-custom">
        <a href="#" class="logo-box">
            <svg class="snake-svg-logo" style="width: 100px; height: 35px;" viewBox="0 0 220 80">
                <text class="base-text" x="50%" y="60%" text-anchor="middle">চিত্রজাল</text>
                <text class="snake-text" x="50%" y="60%" text-anchor="middle">চিত্রজাল</text>
            </svg>
        </a>
        <div class="nav-actions">
            <div class="channel-count" id="channelCountBadge">০ চ্যানেল</div>
            <button class="sync-btn" onclick="syncPlaylists()" id="syncBtn" tabindex="0">
                <i class="fa-solid fa-rotate"></i> রিফ্রেশ
            </button>
        </div>
    </nav>

    <div class="main-container">
        <div class="player-area">
            <div class="player-wrapper" id="playerWrapper">
                <div class="video-container" id="videoContainer">
                    <video id="liveVideo" playsinline webkit-playsinline></video>
                    
                    <div id="loadingOverlay">
                        <div class="loading-spinner"></div>
                        <div style="font-family: 'Hind Siliguri', sans-serif; color: white;">লোড হচ্ছে...</div>
                    </div>

                    <div class="controls" id="playerControls">
                        <button class="nav-btn" onclick="prevChannel()" title="Previous Channel" tabindex="0"><i class="fas fa-chevron-left"></i></button>
                        <button class="control-btn" onclick="togglePlayPause()" id="playPauseBtn" title="Play/Pause" tabindex="0"><i class="fas fa-pause"></i></button>
                        <button class="control-btn" onclick="cycleZoom()" title="Change View" tabindex="0"><i class="fas fa-expand-alt"></i></button>
                        <button class="control-btn" onclick="toggleFullscreen()" title="Fullscreen" tabindex="0"><i class="fas fa-expand"></i></button>
                        <button class="control-btn" onclick="togglePiP()" title="Picture-in-Picture" tabindex="0"><i class="fas fa-tv"></i></button>
                        
                        <div class="volume-container">
                            <button class="mute-btn" onclick="toggleMute()" id="muteBtn" title="Mute" tabindex="0"><i class="fas fa-volume-up"></i></button>
                            <input type="range" class="volume-slider" id="volumeSlider" min="0" max="1" step="0.1" value="1" tabindex="0" aria-label="Volume">
                        </div>
                        
                        <button class="nav-btn" onclick="nextChannel()" title="Next Channel" tabindex="0"><i class="fas fa-chevron-right"></i></button>
                        <select class="quality-select" id="qualityMenu" title="Change Quality" tabindex="0" aria-label="Quality Selection"><option value="-1">Auto Quality</option></select>
                    </div>

                    <div class="player-placeholder" id="playerPlaceholder">
                        <div class="logo-box" style="transform: scale(1.6); margin-bottom: 25px;">
                            <svg class="snake-svg-logo" style="width: 100px; height: 35px;" viewBox="0 0 220 80">
                                <text class="base-text" x="50%" y="60%" text-anchor="middle">চিত্রজাল</text>
                                <text class="snake-text" x="50%" y="60%" text-anchor="middle">চিত্রজাল</text>
                            </svg>
                        </div>
                        <p style="font-family: 'Hind Siliguri', sans-serif; color: #888;"><i class="fa-solid fa-tv"></i> লাইভ টিভি দেখতে চ্যানেল নির্বাচন করুন</p>
                    </div>

                    <div class="player-error-overlay" id="playerErrorBox">
                        <i class="fa-solid fa-triangle-exclamation"></i>
                        <h3>চ্যানেলটি লোড হতে পারছে না</h3>
                        <p>ফ্রি সার্ভার বা কপিরাইট ইস্যুর কারণে এটি প্লে হচ্ছে না।<br>দয়া করে লিস্ট থেকে বিকল্প চ্যানেল নির্বাচন করুন।</p>
                    </div>
                </div>
            </div>
            
            <div class="now-playing-bar">
                <div class="live-tag">LIVE</div>
                <div class="now-playing-text"><h3 id="current-title">চ্যানেল নির্বাচন করুন</h3></div>
            </div>
        </div>

        <div class="content-area">
            <div class="search-filter-bar">
                <div class="search-input-wrap">
                    <i class="fa-solid fa-search"></i>
                    <input type="text" id="searchInput" class="search-input" placeholder="চ্যানেল খুঁজুন..." tabindex="0" aria-label="Search Channels">
                </div>
                <select id="categorySelect" class="cat-select" tabindex="0" aria-label="Select Category"><option value="All">সব ক্যাটাগরি</option></select>
            </div>
            <div class="category-pills-wrapper" id="categoryPills"></div>
            <div class="channels-wrapper" id="channelsWrapper">
                <div class="grid-channels" id="channel-list"></div>
                <footer class="site-footer">
                    <div class="logo-box" style="transform: scale(1.2); margin-bottom: 15px; pointer-events: none;">
                        <svg class="snake-svg-logo" style="width: 120px; height: 40px;" viewBox="0 0 220 80">
                            <text class="base-text" x="50%" y="60%" text-anchor="middle">চিত্রজাল</text>
                            <text class="snake-text" x="50%" y="60%" text-anchor="middle">চিত্রজাল</text>
                        </svg>
                    </div>
                    <p class="footer-desc">আমরা দিচ্ছি উচ্চমানের বাফারহীন স্ট্রিমিং অভিজ্ঞতা। সারা বিশ্বের জনপ্রিয় সব টিভি চ্যানেল এখন আপনার হাতের মুঠোয়।</p>
                    <p class="footer-credit">ডিজাইন করেছে <a href="https://www.facebook.com/TajulBhaiya" target="_blank">তাজুল ইসলাম</a></p>
                </footer>
            </div>
        </div>
    </div>

    <script>
        function toBengaliNum(num) {
            const bngNum = ['০','১','২','৩','৪','৫','৬','৭','৮','৯'];
            return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",").split('').map(c => bngNum[c] || c).join('');
        }

        function translateCategory(catName) {
            if(!catName) return "সাধারণ";
            const map = { 'bangla':'বাংলা', 'bengali':'বাংলা', 'bd channels':'বিডি চ্যানেল', 'bangladeshi':'বাংলাদেশি', 'indian':'ভারতীয়', 'international':'আন্তর্জাতিক', 'world':'ওয়ার্ল্ড', 'movies':'সিনেমা', 'movie':'সিনেমা', 'sports':'খেলাধুলা', 'news':'সংবাদ', 'entertainment':'বিনোদন', 'music':'গান', 'kids':'বাচ্চাদের', 'premium':'প্রিমিয়াম', 'world tv':'ওয়ার্ল্ড টিভি', 'local':'লোকাল', 'general':'সাধারণ', 'documentary':'প্রামাণ্যচিত্র', 'religious':'ধর্মীয়', 'islamic':'ইসলামিক' };
            let lowerCat = catName.toLowerCase().trim();
            if(map[lowerCat]) return map[lowerCat];
            for(let key in map) { if(lowerCat.includes(key)) return map[key]; }
            return catName;
        }

        const playerErrorBox = document.getElementById('playerErrorBox'), playerPlaceholder = document.getElementById('playerPlaceholder'), currentTitle = document.getElementById('current-title'), listContainer = document.getElementById('channel-list'), channelsWrapper = document.getElementById('channelsWrapper'), searchInput = document.getElementById('searchInput'), categorySelect = document.getElementById('categorySelect'), categoryPillsContainer = document.getElementById('categoryPills'), syncBtnIcon = document.querySelector('#syncBtn i'), channelCountBadge = document.getElementById('channelCountBadge'), video = document.getElementById("liveVideo"), loadingOverlay = document.getElementById("loadingOverlay"), playPauseBtn = document.getElementById("playPauseBtn"), muteBtn = document.getElementById("muteBtn"), volumeSlider = document.getElementById("volumeSlider"), qualityMenu = document.getElementById("qualityMenu"), videoContainer = document.getElementById("videoContainer");
        
        let hlsPlayer = null, hlsLevels = [], shakaPlayer = null, zoomIndex = 0;
        const zoomModes = ["contain", "cover", "fill"];
        let allChannels = [], currentFilteredChannels = [], displayedCount = 0, currentChannelIndex = 0;
        const CHUNK_SIZE = 150;

        async function syncPlaylists() {
            allChannels = [];
            const playlists = [
                { url: 'https://raw.githubusercontent.com/sm-monirulislam/AynaOTT-auto-update-playlist/refs/heads/main/AynaOTT.m3u', customCat: 'আয়না ওটিটি' },
                { url: 'https://raw.githubusercontent.com/sydul104/main04/refs/heads/main/my', customCat: 'বিডি চ্যানেল' },
                { url: 'https://github.com/abusaeeidx/Mrgify-BDIX-IPTV/raw/main/playlist.m3u', customCat: 'আন্তর্জাতিক' },
                { url: 'https://raw.githubusercontent.com/BINOD-XD/Toffee-Auto-Update-Playlist/refs/heads/main/toffee_NS_Player.m3u', customCat: 'টফি প্লেয়ার' },
                { url: 'https://raw.githubusercontent.com/badalbd53/Rocket-OTV/refs/heads/master/badal.m3u', customCat: 'রকেট ওটিভি' },
                { url: 'https://raw.githubusercontent.com/sm-monirulislam/SM-Live-TV/c39313219bb273dae55f6d200d5d03b7d6b7c9bb/new_sm.m3u', customCat: 'এসএম লাইভ' }
            ];
            syncBtnIcon.classList.add('spin');
            for (const item of playlists) {
                try { const res = await fetch(item.url); if (res.ok) { parseM3U(await res.text(), item.customCat); } } catch (e) { }
            }

            allChannels.sort((a, b) => {
                const aName = a.name.toUpperCase();
                const bName = b.name.toUpperCase();
                const aHasFHD = aName.includes('FHD') || aName.includes('1080P');
                const bHasFHD = bName.includes('FHD') || bName.includes('1080P');
                if (aHasFHD && !bHasFHD) return -1;
                if (!aHasFHD && bHasFHD) return 1;
                if (a.category === 'আয়না ওটিটি' && b.category !== 'আয়না ওটিটি') return -1;
                if (a.category !== 'আয়না ওটিটি' && b.category === 'আয়না ওটিটি') return 1;
                return 0;
            });

            channelCountBadge.style.display = "block";
            channelCountBadge.innerText = toBengaliNum(allChannels.length) + " চ্যানেল";
            updateCategories(); currentFilteredChannels = allChannels; renderChannels(currentFilteredChannels, false); syncBtnIcon.classList.remove('spin');
        }

        function parseM3U(data, customCat) {
            const lines = data.split('\n'); let temp = {};
            lines.forEach(line => {
                if (line.startsWith('#EXTINF:')) {
                    temp.logo = line.match(/tvg-logo="([^"]+)"/)?.[1] || '';
                    let rawCategory = customCat ? customCat : (line.match(/group-title="([^"]+)"/i)?.[1]?.trim() || 'General');
                    temp.category = translateCategory(rawCategory);
                    temp.name = line.split(',')[1]?.trim() || 'Unknown';
                } else if (line.startsWith('http')) {
                    temp.url = line.trim(); allChannels.push({...temp}); temp = {};
                }
            });
        }

        function updateCategories() {
            const cats = [...new Set(allChannels.map(ch => ch.category))].sort();
            categorySelect.innerHTML = '<option value="All" tabindex="0">সব ক্যাটাগরি</option>';
            cats.forEach(c => categorySelect.innerHTML += `<option value="${c}" tabindex="0">${c}</option>`);
            categoryPillsContainer.innerHTML = '<button class="cat-pill active" onclick="filterByCategory(\'All\', this)" tabindex="0">সব চ্যানেল</button>';
            cats.forEach(c => { categoryPillsContainer.innerHTML += `<button class="cat-pill" onclick="filterByCategory('${c}', this)" tabindex="0">${c}</button>`; });
        }

        window.filterByCategory = function(category, element) {
            document.querySelectorAll('.cat-pill').forEach(btn => btn.classList.remove('active'));
            if(element) element.classList.add('active');
            categorySelect.value = category;
            renderChannels(category === 'All' ? allChannels : allChannels.filter(ch => ch.category === category), false);
        };

        categorySelect.addEventListener('change', () => {
            const val = categorySelect.value;
            document.querySelectorAll('.cat-pill').forEach(btn => {
                btn.classList.remove('active');
                if((val === 'All' && btn.innerText === 'সব চ্যানেল') || btn.innerText === val) { btn.classList.add('active'); btn.scrollIntoView({ behavior: 'smooth', inline: 'center' }); }
            });
            renderChannels(val === 'All' ? allChannels : allChannels.filter(ch => ch.category === val), false);
        });

        function renderChannels(channels, append = false) {
            if (!append) { listContainer.innerHTML = ''; currentFilteredChannels = channels; displayedCount = 0; }
            const fragment = document.createDocumentFragment();
            const toDisplay = currentFilteredChannels.slice(displayedCount, displayedCount + CHUNK_SIZE);
            toDisplay.forEach((ch, idx) => {
                const absoluteIndex = displayedCount + idx;
                const div = document.createElement('div'); div.className = 'card-custom'; div.setAttribute('data-index', absoluteIndex);
                div.setAttribute('tabindex', '0');
                div.innerHTML = `<div class="card-img-wrap"><img src="${ch.logo}" loading="lazy" onerror="this.src='https://cdn-icons-png.flaticon.com/512/777/777242.png'"></div><div class="card-title">${ch.name}</div>`;
                div.onclick = () => playStream(ch.url, ch.name, div, absoluteIndex);
                div.onkeydown = (e) => { if(e.key === 'Enter') playStream(ch.url, ch.name, div, absoluteIndex); };
                fragment.appendChild(div);
            });
            listContainer.appendChild(fragment); displayedCount += toDisplay.length;
        }

        channelsWrapper.addEventListener('scroll', () => {
            if (channelsWrapper.scrollTop + channelsWrapper.clientHeight >= channelsWrapper.scrollHeight - 300) {
                if (displayedCount < currentFilteredChannels.length) { renderChannels(currentFilteredChannels, true); }
            }
        });

        function cleanupPlayers() {
            if (hlsPlayer) { hlsPlayer.destroy(); hlsPlayer = null; }
            if (shakaPlayer) { shakaPlayer.unload(); shakaPlayer.destroy(); shakaPlayer = null; }
            video.src = ""; video.load();
        }

        function populateQualityMenu() {
            qualityMenu.innerHTML = '<option value="-1">Auto</option>';
            if (hlsLevels && hlsLevels.length > 1) {
                qualityMenu.style.display = 'block';
                hlsLevels.forEach((level, index) => {
                    const option = document.createElement("option"); option.value = index;
                    option.textContent = level.height ? level.height + "p" : "Quality " + (index + 1);
                    qualityMenu.appendChild(option);
                });
            } else { qualityMenu.style.display = 'none'; }
        }

        function playStream(url, name, el, index) {
            currentChannelIndex = index; playerErrorBox.style.display = 'none'; playerPlaceholder.style.display = 'none';
            document.querySelectorAll('.card-custom').forEach(c => c.classList.remove('active')); if(el) el.classList.add('active');
            currentTitle.innerText = name; cleanupPlayers(); loadingOverlay.style.display = "flex";

            // Update Metadata for Notification
            if(window.Android && window.Android.updateMetadata) {
                window.Android.updateMetadata(name, "ChitraJal Live TV");
            }

            if (Hls.isSupported() && url.includes('.m3u8')) {
                hlsPlayer = new Hls({ maxBufferLength: 30, enableWorker: true, lowLatencyMode: true });
                hlsPlayer.loadSource(url); hlsPlayer.attachMedia(video);
                hlsPlayer.on(Hls.Events.MANIFEST_PARSED, function(event, data) {
                    hlsLevels = data.levels;
                    populateQualityMenu();
                    video.play().catch(e => {});
                    loadingOverlay.style.display = "none";
                });
                hlsPlayer.on(Hls.Events.ERROR, function(event, data) { if (data.fatal) { loadingOverlay.style.display = "none"; playerErrorBox.style.display = 'flex'; } });
            } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
                video.src = url;
                video.addEventListener('loadedmetadata', function() {
                    video.play();
                    loadingOverlay.style.display = "none";
                });
            } else {
                shaka.polyfill.installAll();
                if (shaka.Player.isBrowserSupported()) {
                    shakaPlayer = new shaka.Player(video);
                    shakaPlayer.load(url).then(() => {
                        video.play();
                        loadingOverlay.style.display = "none";
                    }).catch(e => { loadingOverlay.style.display = "none"; playerErrorBox.style.display = 'flex'; });
                }
            }
        }

        function nextChannel() { if (currentFilteredChannels.length === 0) return; triggerChannelPlay((currentChannelIndex + 1) % currentFilteredChannels.length); }
        function prevChannel() { if (currentFilteredChannels.length === 0) return; triggerChannelPlay((currentChannelIndex - 1 + currentFilteredChannels.length) % currentFilteredChannels.length); }
        function triggerChannelPlay(idx) {
            const el = document.querySelector(`.card-custom[data-index="${idx}"]`);
            if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
            playStream(currentFilteredChannels[idx].url, currentFilteredChannels[idx].name, el, idx);
        }

        qualityMenu.addEventListener("change", function() { if (hlsPlayer) { hlsPlayer.currentLevel = parseInt(this.value); } });
        volumeSlider.addEventListener("input", function() { video.volume = this.value; muteBtn.innerHTML = (video.volume == 0) ? '<i class="fas fa-volume-mute"></i>' : '<i class="fas fa-volume-up"></i>'; });
        video.addEventListener("play", function() { playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>'; showControls(); });
        video.addEventListener("pause", function() { playPauseBtn.innerHTML = '<i class="fas fa-play"></i>'; showControls(); });
        video.addEventListener("waiting", function() { loadingOverlay.style.display = "flex"; });
        video.addEventListener("playing", function() { loadingOverlay.style.display = "none"; playerErrorBox.style.display = 'none'; resetControlsTimer(); });
        video.addEventListener("error", function() { loadingOverlay.style.display = "none"; playerErrorBox.style.display = 'flex'; });

        function togglePlayPause() { if (video.paused) { video.play().catch(e => {}); } else { video.pause(); } }
        function toggleMute() { video.muted = !video.muted; if (video.muted) { muteBtn.innerHTML = '<i class="fas fa-volume-mute"></i>'; volumeSlider.value = 0; } else { muteBtn.innerHTML = '<i class="fas fa-volume-up"></i>'; volumeSlider.value = video.volume; } }
        function cycleZoom() { zoomIndex = (zoomIndex + 1) % zoomModes.length; video.style.objectFit = zoomModes[zoomIndex]; }
        function toggleFullscreen() {
            const container = document.getElementById('videoContainer');
            if (!document.fullscreenElement) {
                if (container.requestFullscreen) { container.requestFullscreen(); }
                else if (container.webkitRequestFullscreen) { container.webkitRequestFullscreen(); }
                else if (container.msRequestFullscreen) { container.msRequestFullscreen(); }
            } else {
                if (document.exitFullscreen) { document.exitFullscreen(); }
                else if (document.webkitExitFullscreen) { document.webkitExitFullscreen(); }
                else if (document.msExitFullscreen) { document.msExitFullscreen(); }
            }
        }
        function togglePiP() { if (document.pictureInPictureElement) { document.exitPictureInPicture(); } else if (document.pictureInPictureEnabled) { video.requestPictureInPicture(); } }
        searchInput.addEventListener('input', () => { const q = searchInput.value.toLowerCase(); renderChannels(allChannels.filter(ch => ch.name.toLowerCase().includes(q)), false); });

        let controlsTimer = null;
        function showControls() { videoContainer.classList.remove('controls-hidden'); resetControlsTimer(); }
        function hideControls() { if (!video.paused) { videoContainer.classList.add('controls-hidden'); } }
        function resetControlsTimer() { clearTimeout(controlsTimer); if (!video.paused) { controlsTimer = setTimeout(hideControls, 3000); } }
        videoContainer.addEventListener('mousemove', showControls);
        videoContainer.addEventListener('touchstart', showControls);
        videoContainer.addEventListener('click', showControls);
        window.onload = syncPlaylists;
    </script>
</body>
</html>
