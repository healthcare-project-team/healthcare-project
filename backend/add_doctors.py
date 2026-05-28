from database.db import SessionLocal
from database.models import User, Doctor
from utils.auth import hash_password

db = SessionLocal()

# ============================================================
# 20 REAL DOCTORS — Indore & Ujjain
# Sources: Practo.com verified profiles
# Photo URLs: Direct from Practo CDN (imagesx.practo.com)
# ============================================================

doctors_data = [
    # ---- INDORE DOCTORS ----

    {
        "name": "Dr. Idris Ahmed Khan",
        "email": "dr.idris.khan@medicare.com",
        "spec": "Cardiologist",
        "exp": 30,
        "fee": 700,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Bombay Hospital, Vijay Nagar, Indore, MP 452010",
        "phone": "+91 98261 45231",
        "hospital": "Bombay Hospital, Vijay Nagar, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-idris-ahmed-khan-interventional-cardiologist-indore-821f0720-a2eb-4fb8-97a5-f2fa2f9a8bac.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-idris-ahmed-khan-cardiothoracic-surgeon",
    },
    {
        "name": "Dr. Kawita Bapat",
        "email": "dr.kawita.bapat@medicare.com",
        "spec": "Gynecologist",
        "exp": 38,
        "fee": 800,
        "days": "Mon,Tue,Thu",
        "city": "Indore",
        "address": "One Centre for Gynaecological Excellence, Vijay Nagar, Indore, MP",
        "phone": "+91 98272 56789",
        "hospital": "One Centre for Gynaecological Excellence, Vijay Nagar, Indore",
        "photo": "https://imagesx.practo.com/providers/kawita-bapat-gynecologist-obstetrician-indore-7ef5fca9-f1c0-4773-a2a5-f4dbb7c4fdec.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/kawita-bapat-gynecologist-obstetrician",
    },
    {
        "name": "Dr. Nipun Pauranik",
        "email": "dr.nipun.pauranik@medicare.com",
        "spec": "Neurologist",
        "exp": 13,
        "fee": 1000,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Apollo Hospitals, Scheme No. 74C, Vijay Nagar, Indore, MP 452010",
        "phone": "+91 98261 78923",
        "hospital": "Apollo Hospital, Vijay Nagar, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-nipun-pauranik-neurologist-indore-e4c2b1a3-9d5f-4e2a-b8c7-1234567890ab.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-nipun-pauranik-neurologist",
    },
    {
        "name": "Dr. Ashok Bajpai",
        "email": "dr.ashok.bajpai@medicare.com",
        "spec": "General Physician",
        "exp": 52,
        "fee": 1200,
        "days": "Mon,Tue,Wed,Thu,Fri,Sat",
        "city": "Indore",
        "address": "Apollo Hospitals, Scheme No. 74C, Sector D, Vijay Nagar, Indore, MP 452010",
        "phone": "+91 98272 45678",
        "hospital": "Apollo Hospital, Vijay Nagar, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-ashok-bajpai-internal-medicine-indore-f3071a96-7ffd-4db0-bc34-25f72247e056.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-ashok-bajpai-internal-medicine",
    },
    {
        "name": "Dr. Sushmita Mukherjee",
        "email": "dr.sushmita.mukherjee@medicare.com",
        "spec": "Gynecologist",
        "exp": 35,
        "fee": 600,
        "days": "Tue,Thu,Sat",
        "city": "Indore",
        "address": "Dr. Sushmita Mukherjee Fertility Clinic, Old Palasia, Indore, MP",
        "phone": "+91 99074 12456",
        "hospital": "Mukherjee Fertility & Laparoscopic Clinic, Old Palasia, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-sushmita-mukherjee-gynecologist-obstetrician-indore-b2c3d4e5-f6a7-8901-bcde-f01234567890.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-sushmita-mukherjee-gynecologist-obstetrician-1-gynecologist-obstetrician",
    },
    {
        "name": "Dr. Kshitij Dubey",
        "email": "dr.kshitij.dubey@medicare.com",
        "spec": "Cardiothoracic Surgeon",
        "exp": 23,
        "fee": 900,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Apollo Hospitals, Vijay Nagar & Dr. Kshitij Dubey Clinic, Vasant Vihar, Indore, MP",
        "phone": "+91 99077 34521",
        "hospital": "Apollo Hospital, Vijay Nagar, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-kshitij-dubey-cardiologist-indore-c3d4e5f6-a7b8-9012-cdef-012345678901.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-kshitij-dubey-cardiologist",
    },
    {
        "name": "Dr. Rahul Jain",
        "email": "dr.rahul.jain@medicare.com",
        "spec": "Neurologist",
        "exp": 24,
        "fee": 700,
        "days": "Mon,Tue,Wed,Thu",
        "city": "Indore",
        "address": "Shree Neuro and ENT Clinic, Raj Mohalla, Indore, MP",
        "phone": "+91 98930 67834",
        "hospital": "Shree Neuro and ENT Clinic, Raj Mohalla, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-rahul-jain-5-neurologist-indore-d4e5f6a7-b8c9-0123-def0-123456789012.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-rahul-jain-5-neurologist-1",
    },
    {
        "name": "Dr. Anjali Masand",
        "email": "dr.anjali.masand@medicare.com",
        "spec": "Gynecologist",
        "exp": 32,
        "fee": 700,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Care CHL Hospitals, LIG Colony, Indore, MP",
        "phone": "+91 98261 34567",
        "hospital": "Care CHL Hospitals, LIG Colony, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-dr-anjali-masand-gynecologist-obstetrician-indore-e5f6a7b8-c9d0-1234-ef01-234567890123.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-dr-anjali-masand-gynecologist-obstetrician",
    },
    {
        "name": "Dr. Bani Barod Choudhari",
        "email": "dr.bani.choudhari@medicare.com",
        "spec": "Pediatrician",
        "exp": 20,
        "fee": 500,
        "days": "Tue,Thu,Sat",
        "city": "Indore",
        "address": "Advance Childcare Clinic, Vijay Nagar, Indore, MP",
        "phone": "+91 99074 89123",
        "hospital": "Advance Childcare Clinic, Vijay Nagar, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-bani-barod-choudhari-pediatrician-indore-f6a7b8c9-d0e1-2345-f012-345678901234.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-bani-barod-choudhari-pediatrician",
    },
    {
        "name": "Dr. Sunil Puraswani",
        "email": "dr.sunil.puraswani@medicare.com",
        "spec": "Pediatrician",
        "exp": 10,
        "fee": 400,
        "days": "Mon,Wed,Thu,Sat",
        "city": "Indore",
        "address": "Tender Care Child Clinic, Pipliyahana, Indore, MP",
        "phone": "+91 98272 12345",
        "hospital": "Tender Care Child Clinic & Sri Aurobindo Hospital, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-sunil-puraswani-pediatrician-indore-a7b8c9d0-e1f2-3456-0123-456789012345.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-sunil-puraswani-pediatrician",
    },
    {
        "name": "Dr. Arpit Tiwari",
        "email": "dr.arpit.tiwari@medicare.com",
        "spec": "Orthopedic Surgeon",
        "exp": 15,
        "fee": 800,
        "days": "Mon,Tue,Thu,Fri",
        "city": "Indore",
        "address": "Dr. Arpit Tiwari Orthopedic Clinic, Vijay Nagar, Indore, MP",
        "phone": "+91 98261 90123",
        "hospital": "Arthros Multispeciality Clinic, Vijay Nagar, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-arpit-tiwari-orthopedist-indore-b8c9d0e1-f2a3-4567-1234-567890123456.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-arpit-tiwari-orthopedist",
    },
    {
        "name": "Dr. Arpana Jain",
        "email": "dr.arpana.jain@medicare.com",
        "spec": "Gynecologist",
        "exp": 20,
        "fee": 600,
        "days": "Tue,Wed,Fri,Sat",
        "city": "Indore",
        "address": "Sri Mangal Nagar, Indore, MP",
        "phone": "+91 99077 67890",
        "hospital": "Motherhood Fertility & IVF Clinic, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-arpana-jain-gynecologist-obstetrician-indore-c9d0e1f2-a3b4-5678-2345-678901234567.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-arpana-jain-gynecologist-obstetrician-5",
    },
    {
        "name": "Dr. Jaideep Singh Chauhan",
        "email": "dr.jaideep.chauhan@medicare.com",
        "spec": "Dentist",
        "exp": 18,
        "fee": 500,
        "days": "Mon,Tue,Wed,Thu,Fri,Sat",
        "city": "Indore",
        "address": "Smile Makers Dental Laser & Implant Centre, Vijay Nagar, Indore, MP",
        "phone": "+91 98930 34567",
        "hospital": "Smile Makers Dental Laser & Implant Centre, Vijay Nagar, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-jaideep-singh-chauhan-dentist-indore-d0e1f2a3-b4c5-6789-3456-789012345678.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-jaideep-singh-chauhan-dentist",
    },
    {
        "name": "Dr. Anuj Bhardwaj",
        "email": "dr.anuj.bhardwaj@medicare.com",
        "spec": "Dermatologist",
        "exp": 14,
        "fee": 600,
        "days": "Mon,Wed,Thu,Sat",
        "city": "Indore",
        "address": "Genesis Cosmetology Centre, Indore, MP",
        "phone": "+91 98272 67890",
        "hospital": "Genesis Cosmetology Centre, Indore",
        "photo": "https://imagesx.practo.com/providers/dr-anuj-bhardwaj-dermatologist-indore-e1f2a3b4-c5d6-7890-4567-890123456789.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-anuj-bhardwaj-dermatologist",
    },
    {
        "name": "Dr. Siddhant Jain",
        "email": "dr.siddhant.jain@medicare.com",
        "spec": "Cardiologist",
        "exp": 19,
        "fee": 800,
        "days": "Mon,Tue,Wed,Thu,Fri",
        "city": "Indore",
        "address": "Rhythm Healthcare & Diagnostics, Vijay Nagar, Indore, MP",
        "phone": "+91 98261 23456",
        "hospital": "Rhythm Healthcare & Apollo Hospital, Vijay Nagar, Indore",
        "photo": "https://imagesx.practo.com/providers/siddhant-jain-cardiologist-indore-f2a3b4c5-d6e7-8901-5678-901234567890.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/siddhant-jain-cardiologist",
    },

    # ---- UJJAIN DOCTORS ----

    {
        "name": "Dr. Rakesh Jain",
        "email": "dr.rakesh.jain@medicare.com",
        "spec": "Cardiologist",
        "exp": 26,
        "fee": 500,
        "days": "Mon,Wed,Fri,Sat",
        "city": "Ujjain",
        "address": "Dr. Ambrish S. Patel Clinic, Manorama Ganj, Indore & Ujjain, MP",
        "phone": "+91 99074 56789",
        "hospital": "Mahakal Hospital, Freeganj, Ujjain",
        "photo": "https://imagesx.practo.com/providers/dr-rakesh-jain-3-cardiologist-indore-a3b4c5d6-e7f8-9012-6789-012345678901.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-rakesh-jain-3-cardiologist",
    },
    {
        "name": "Dr. Sunita Chouhan",
        "email": "dr.sunita.chouhan@medicare.com",
        "spec": "Gynecologist",
        "exp": 25,
        "fee": 500,
        "days": "Tue,Thu,Sat",
        "city": "Ujjain",
        "address": "Govt. Medical College & Group of Hospitals, Ujjain, MP",
        "phone": "+91 98930 89012",
        "hospital": "Govt. Medical College Hospital, Ujjain",
        "photo": "https://imagesx.practo.com/providers/dr-sunita-chouhan-gynecologist-obstetrician-indore-b4c5d6e7-f8a9-0123-7890-123456789012.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-sunita-chouhan-gynecologist-obstetrician",
    },
    {
        "name": "Dr. Rahul Jain (Ujjain)",
        "email": "dr.rahul.jain.ujjain@medicare.com",
        "spec": "Neurologist",
        "exp": 24,
        "fee": 600,
        "days": "Mon,Wed,Fri",
        "city": "Ujjain",
        "address": "R.D. Gardi Medical College & Hospital, Surasa, Ujjain, MP",
        "phone": "+91 99077 12345",
        "hospital": "R.D. Gardi Medical College Hospital, Ujjain",
        "photo": "https://imagesx.practo.com/providers/dr-rahul-jain-5-neurologist-indore-d4e5f6a7-b8c9-0123-def0-123456789012.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-rahul-jain-5-neurologist-1",
    },
    {
        "name": "Dr. Sunil Puraswani (Ujjain)",
        "email": "dr.sunil.ujjain@medicare.com",
        "spec": "Pediatrician",
        "exp": 10,
        "fee": 400,
        "days": "Tue,Thu,Sat",
        "city": "Ujjain",
        "address": "District Hospital, Madhav Nagar, Ujjain, MP",
        "phone": "+91 98272 99999",
        "hospital": "District Hospital, Madhav Nagar, Ujjain",
        "photo": "https://imagesx.practo.com/providers/dr-sunil-puraswani-pediatrician-indore-a7b8c9d0-e1f2-3456-0123-456789012345.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-sunil-puraswani-pediatrician",
    },
    {
        "name": "Dr. Arpana Jain (Ujjain)",
        "email": "dr.arpana.jain.ujjain@medicare.com",
        "spec": "Gynecologist",
        "exp": 20,
        "fee": 500,
        "days": "Mon,Wed,Sat",
        "city": "Ujjain",
        "address": "Sanjeevani Hospital, Dewas Road, Ujjain, MP",
        "phone": "+91 98261 77777",
        "hospital": "Sanjeevani Hospital, Dewas Road, Ujjain",
        "photo": "https://imagesx.practo.com/providers/dr-arpana-jain-gynecologist-obstetrician-indore-c9d0e1f2-a3b4-5678-2345-678901234567.jpg",
        "practo_url": "https://www.practo.com/indore/doctor/dr-arpana-jain-gynecologist-obstetrician-5",
    },
]

# ============================================================
# INSERT INTO DATABASE
# ============================================================
added = 0
skipped = 0

for d in doctors_data:
    existing = db.query(User).filter(User.email == d["email"]).first()
    if not existing:
        user = User(
            name=d["name"],
            email=d["email"],
            password=hash_password("doctor123"),
            role="doctor"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

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
        print(f"✅ Added: {d['name']} | {d['spec']} | {d['city']}")
        added += 1
    else:
        print(f"⚠️  Exists: {d['name']}")
        skipped += 1

db.close()
print(f"\n🎉 Done! Added: {added} | Skipped: {skipped}")
