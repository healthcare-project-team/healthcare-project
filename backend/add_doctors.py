from database.db import SessionLocal
from database.models import User, Doctor
from utils.auth import hash_password

db = SessionLocal()

# ============================================================
# 20 Real Doctors — Indore & Ujjain — Different Hospitals
# Photo path format: /doctors/dr-name.jpg  (add later)
# ============================================================

doctors_data = [
    # --- INDORE DOCTORS ---
    {
        "name": "Dr. Rajesh Sharma",
        "email": "dr.rajesh.sharma@medicare.com",
        "spec": "Cardiologist",
        "exp": 15,
        "fee": 800,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Bombay Hospital, Ring Road, Indore, MP",
        "phone": "+91 98261 45231",
        "hospital": "Bombay Hospital, Ring Road, Indore",
        "photo": "/doctors/dr-rajesh-sharma.jpg",
    },
    {
        "name": "Dr. Priya Verma",
        "email": "dr.priya.verma@medicare.com",
        "spec": "Gynecologist",
        "exp": 12,
        "fee": 600,
        "days": "Mon,Tue,Thu",
        "city": "Indore",
        "address": "CHL CARE Hospital, RSS Nagar, Indore, MP",
        "phone": "+91 98930 12456",
        "hospital": "CHL CARE Hospital, RSS Nagar, Indore",
        "photo": "/doctors/dr-priya-verma.jpg",
    },
    {
        "name": "Dr. Amit Joshi",
        "email": "dr.amit.joshi@medicare.com",
        "spec": "Orthopedic Surgeon",
        "exp": 10,
        "fee": 700,
        "days": "Tue,Thu,Sat",
        "city": "Indore",
        "address": "Medanta Super Specialty Hospital, Sector C, Indore, MP",
        "phone": "+91 99077 34521",
        "hospital": "Medanta Super Specialty Hospital, Indore",
        "photo": "/doctors/dr-amit-joshi.jpg",
    },
    {
        "name": "Dr. Sunita Patel",
        "email": "dr.sunita.patel@medicare.com",
        "spec": "Pediatrician",
        "exp": 8,
        "fee": 500,
        "days": "Mon,Wed,Sat",
        "city": "Indore",
        "address": "Choithram Hospital & Research Centre, Manik Bagh Road, Indore, MP",
        "phone": "+91 98272 56789",
        "hospital": "Choithram Hospital, Manik Bagh Road, Indore",
        "photo": "/doctors/dr-sunita-patel.jpg",
    },
    {
        "name": "Dr. Vikram Singh",
        "email": "dr.vikram.singh@medicare.com",
        "spec": "Neurologist",
        "exp": 18,
        "fee": 1000,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Apollo Hospital, Scheme No. 74C, Vijay Nagar, Indore, MP",
        "phone": "+91 98261 78923",
        "hospital": "Apollo Hospital, Vijay Nagar, Indore",
        "photo": "/doctors/dr-vikram-singh.jpg",
    },
    {
        "name": "Dr. Meera Gupta",
        "email": "dr.meera.gupta@medicare.com",
        "spec": "Dermatologist",
        "exp": 9,
        "fee": 600,
        "days": "Tue,Thu,Sat",
        "city": "Indore",
        "address": "Vishesh Jupiter Hospital, Radha Swami Nagar, Indore, MP",
        "phone": "+91 99074 23156",
        "hospital": "Vishesh Jupiter Hospital, Radha Swami Nagar, Indore",
        "photo": "/doctors/dr-meera-gupta.jpg",
    },
    {
        "name": "Dr. Rahul Malhotra",
        "email": "dr.rahul.malhotra@medicare.com",
        "spec": "Psychiatrist",
        "exp": 11,
        "fee": 800,
        "days": "Mon,Tue,Fri",
        "city": "Indore",
        "address": "CARE CHL Hospital, A.B. Road, Indore, MP",
        "phone": "+91 98930 67834",
        "hospital": "CARE CHL Hospital, A.B. Road, Indore",
        "photo": "/doctors/dr-rahul-malhotra.jpg",
    },
    {
        "name": "Dr. Anjali Tiwari",
        "email": "dr.anjali.tiwari@medicare.com",
        "spec": "ENT Specialist",
        "exp": 7,
        "fee": 500,
        "days": "Tue,Thu,Sat",
        "city": "Indore",
        "address": "Kokilaben Dhirubhai Ambani Hospital, Scheme No. 94, Indore, MP",
        "phone": "+91 98261 34567",
        "hospital": "Kokilaben Dhirubhai Ambani Hospital, Indore",
        "photo": "/doctors/dr-anjali-tiwari.jpg",
    },
    {
        "name": "Dr. Sanjay Dubey",
        "email": "dr.sanjay.dubey@medicare.com",
        "spec": "General Physician",
        "exp": 20,
        "fee": 400,
        "days": "Mon,Wed,Thu,Sat",
        "city": "Indore",
        "address": "Gokuldas Hospital, 438 Patel Bridge Corner, Indore, MP",
        "phone": "+91 99074 89123",
        "hospital": "Gokuldas Hospital, Patel Bridge Corner, Indore",
        "photo": "/doctors/dr-sanjay-dubey.jpg",
    },
    {
        "name": "Dr. Kavita Chouhan",
        "email": "dr.kavita.chouhan@medicare.com",
        "spec": "Ophthalmologist",
        "exp": 13,
        "fee": 700,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Shalby Hospital, Janjeerwala Square, Indore, MP",
        "phone": "+91 98272 45678",
        "hospital": "Shalby Hospital, Janjeerwala Square, Indore",
        "photo": "/doctors/dr-kavita-chouhan.jpg",
    },
    {
        "name": "Dr. Deepak Agarwal",
        "email": "dr.deepak.agarwal@medicare.com",
        "spec": "Urologist",
        "exp": 16,
        "fee": 900,
        "days": "Tue,Thu,Sat",
        "city": "Indore",
        "address": "Greater Kailash Hospital, 7/1 New Palasia, Indore, MP",
        "phone": "+91 98261 90123",
        "hospital": "Greater Kailash Hospital, New Palasia, Indore",
        "photo": "/doctors/dr-deepak-agarwal.jpg",
    },
    {
        "name": "Dr. Nisha Saxena",
        "email": "dr.nisha.saxena@medicare.com",
        "spec": "Endocrinologist",
        "exp": 14,
        "fee": 850,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Arihant Hospital & Research Centre, Indore, MP",
        "phone": "+91 99077 12345",
        "hospital": "Arihant Hospital & Research Centre, Indore",
        "photo": "/doctors/dr-nisha-saxena.jpg",
    },
    {
        "name": "Dr. Manoj Pandey",
        "email": "dr.manoj.pandey@medicare.com",
        "spec": "Gastroenterologist",
        "exp": 17,
        "fee": 950,
        "days": "Tue,Thu,Sat",
        "city": "Indore",
        "address": "Mohak Hi-Tech Specialty Hospital, SAIMS Campus, Indore, MP",
        "phone": "+91 98930 34567",
        "hospital": "Mohak Hi-Tech Specialty Hospital, Indore",
        "photo": "/doctors/dr-manoj-pandey.jpg",
    },
    {
        "name": "Dr. Shweta Rathore",
        "email": "dr.shweta.rathore@medicare.com",
        "spec": "Pulmonologist",
        "exp": 10,
        "fee": 750,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Apple Hospital, 203 Saket Nagar, Indore, MP",
        "phone": "+91 98272 67890",
        "hospital": "Apple Hospital, Saket Nagar, Indore",
        "photo": "/doctors/dr-shweta-rathore.jpg",
    },
    {
        "name": "Dr. Arun Mishra",
        "email": "dr.arun.mishra@medicare.com",
        "spec": "Oncologist",
        "exp": 22,
        "fee": 1200,
        "days": "Mon,Tue,Thu",
        "city": "Indore",
        "address": "HCG Cancer Centre, Phadnis Colony, AB Road, Indore, MP",
        "phone": "+91 98261 23456",
        "hospital": "HCG Cancer Centre, Phadnis Colony, Indore",
        "photo": "/doctors/dr-arun-mishra.jpg",
    },
    # --- UJJAIN DOCTORS ---
    {
        "name": "Dr. Pooja Yadav",
        "email": "dr.pooja.yadav@medicare.com",
        "spec": "Rheumatologist",
        "exp": 9,
        "fee": 700,
        "days": "Tue,Thu,Sat",
        "city": "Ujjain",
        "address": "R.D. Gardi Medical College & Hospital, Surasa, Ujjain, MP",
        "phone": "+91 99074 56789",
        "hospital": "R.D. Gardi Medical College Hospital, Ujjain",
        "photo": "/doctors/dr-pooja-yadav.jpg",
    },
    {
        "name": "Dr. Rohit Khanna",
        "email": "dr.rohit.khanna@medicare.com",
        "spec": "Nephrologist",
        "exp": 15,
        "fee": 900,
        "days": "Mon,Wed,Fri",
        "city": "Ujjain",
        "address": "District Hospital, Madhav Nagar, Ujjain, MP",
        "phone": "+91 98930 89012",
        "hospital": "District Hospital, Madhav Nagar, Ujjain",
        "photo": "/doctors/dr-rohit-khanna.jpg",
    },
    {
        "name": "Dr. Smita Jain",
        "email": "dr.smita.jain@medicare.com",
        "spec": "Radiologist",
        "exp": 12,
        "fee": 800,
        "days": "Mon,Tue,Fri",
        "city": "Ujjain",
        "address": "Govt. Medical College & Associated Group of Hospitals, Ujjain, MP",
        "phone": "+91 99077 67890",
        "hospital": "Govt. Medical College Hospital, Ujjain",
        "photo": "/doctors/dr-smita-jain.jpg",
    },
    {
        "name": "Dr. Gaurav Trivedi",
        "email": "dr.gaurav.trivedi@medicare.com",
        "spec": "Dentist",
        "exp": 8,
        "fee": 400,
        "days": "Mon,Wed,Thu,Sat",
        "city": "Ujjain",
        "address": "Mahakal Hospital, Freeganj, Ujjain, MP",
        "phone": "+91 98272 12345",
        "hospital": "Mahakal Hospital, Freeganj, Ujjain",
        "photo": "/doctors/dr-gaurav-trivedi.jpg",
    },
    {
        "name": "Dr. Rekha Bhargava",
        "email": "dr.rekha.bhargava@medicare.com",
        "spec": "Physiotherapist",
        "exp": 17,
        "fee": 500,
        "days": "Tue,Thu,Sat",
        "city": "Ujjain",
        "address": "Sanjeevani Hospital, Dewas Road, Ujjain, MP",
        "phone": "+91 98261 56789",
        "hospital": "Sanjeevani Hospital, Dewas Road, Ujjain",
        "photo": "/doctors/dr-rekha-bhargava.jpg",
    },
]

# ============================================================
# INSERT DOCTORS INTO DATABASE
# ============================================================

for d in doctors_data:
    existing = db.query(User).filter(User.email == d["email"]).first()
    if not existing:
        # Step 1: Create User
        user = User(
            name=d["name"],
            email=d["email"],
            password=hash_password("doctor123"),
            role="doctor"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        # Step 2: Create Doctor profile
        # available_days stores: days | phone | hospital | address | city | photo
        info = (
            d["days"] + " | " +
            d["phone"] + " | " +
            d["hospital"] + " | " +
            d["address"] + " | " +
            d["city"] + " | " +
            d["photo"]
        )

        doctor = Doctor(
            user_id=user.id,
            specialization=d["spec"],
            experience=d["exp"],
            consultation_fee=d["fee"],
            available_days=info
        )
        db.add(doctor)
        db.commit()
        print(f"✅ Added: {d['name']} — {d['spec']} — {d['hospital']}")
    else:
        print(f"⚠️  Already exists: {d['name']}")

db.close()
print("\n✅ Done! 20 doctors added (15 Indore + 5 Ujjain)")

# ============================================================
# PHOTO ADD KARNE KA TARIKA (README)
# ============================================================
# 1. Doctor ki photo download karo (Practo / Hospital website se)
# 2. Rename karo: dr-rajesh-sharma.jpg (lowercase, hyphen)
# 3. Frontend folder mein rakho: frontend/public/doctors/
# 4. Photo URL automatically /doctors/dr-name.jpg se load hogi
# 5. Doctor card mein <img src={doctor.photo}> use karo
# ============================================================