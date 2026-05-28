from database.db import SessionLocal
from database.models import User, Doctor
from utils.auth import hash_password

db = SessionLocal()

# ============================================================
# 20 DOCTORS DATA
# ============================================================

doctors_data = [

    {
        "name": "Dr. Idris Ahmed Khan",
        "email": "dr.idris.khan@medicare.com",
        "spec": "Cardiologist",
        "exp": 30,
        "fee": 700,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Bombay Hospital, Vijay Nagar",
        "phone": "+91 98261 45231",
        "hospital": "Bombay Hospital",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Idris+Ahmed+Khan",
    },

    {
        "name": "Dr. Kawita Bapat",
        "email": "dr.kawita.bapat@medicare.com",
        "spec": "Gynecologist",
        "exp": 38,
        "fee": 800,
        "days": "Mon,Tue,Thu",
        "city": "Indore",
        "address": "One Centre for Gynaecological Excellence",
        "phone": "+91 98272 56789",
        "hospital": "One Centre for Gynaecological Excellence",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Kawita+Bapat",
    },

    {
        "name": "Dr. Nipun Pauranik",
        "email": "dr.nipun.pauranik@medicare.com",
        "spec": "Neurologist",
        "exp": 13,
        "fee": 1000,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Apollo Hospital",
        "phone": "+91 98261 78923",
        "hospital": "Apollo Hospital",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Nipun+Pauranik",
    },

    {
        "name": "Dr. Ashok Bajpai",
        "email": "dr.ashok.bajpai@medicare.com",
        "spec": "General Physician",
        "exp": 52,
        "fee": 1200,
        "days": "Mon,Tue,Wed,Thu,Fri,Sat",
        "city": "Indore",
        "address": "Apollo Hospital",
        "phone": "+91 98272 45678",
        "hospital": "Apollo Hospital",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Ashok+Bajpai",
    },

    {
        "name": "Dr. Sushmita Mukherjee",
        "email": "dr.sushmita.mukherjee@medicare.com",
        "spec": "Gynecologist",
        "exp": 35,
        "fee": 600,
        "days": "Tue,Thu,Sat",
        "city": "Indore",
        "address": "Old Palasia",
        "phone": "+91 99074 12456",
        "hospital": "Mukherjee Fertility Clinic",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Sushmita+Mukherjee",
    },

    {
        "name": "Dr. Kshitij Dubey",
        "email": "dr.kshitij.dubey@medicare.com",
        "spec": "Cardiothoracic Surgeon",
        "exp": 23,
        "fee": 900,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "Apollo Hospital",
        "phone": "+91 99077 34521",
        "hospital": "Apollo Hospital",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Kshitij+Dubey",
    },

    {
        "name": "Dr. Rahul Jain",
        "email": "dr.rahul.jain@medicare.com",
        "spec": "Neurologist",
        "exp": 24,
        "fee": 700,
        "days": "Mon,Tue,Wed,Thu",
        "city": "Indore",
        "address": "Raj Mohalla",
        "phone": "+91 98930 67834",
        "hospital": "Shree Neuro Clinic",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Rahul+Jain",
    },

    {
        "name": "Dr. Anjali Masand",
        "email": "dr.anjali.masand@medicare.com",
        "spec": "Gynecologist",
        "exp": 32,
        "fee": 700,
        "days": "Mon,Wed,Fri",
        "city": "Indore",
        "address": "LIG Colony",
        "phone": "+91 98261 34567",
        "hospital": "Care CHL Hospital",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Anjali+Masand",
    },

    {
        "name": "Dr. Bani Barod Choudhari",
        "email": "dr.bani.choudhari@medicare.com",
        "spec": "Pediatrician",
        "exp": 20,
        "fee": 500,
        "days": "Tue,Thu,Sat",
        "city": "Indore",
        "address": "Vijay Nagar",
        "phone": "+91 99074 89123",
        "hospital": "Advance Childcare Clinic",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Bani+Barod+Choudhari",
    },

    {
        "name": "Dr. Sunil Puraswani",
        "email": "dr.sunil.puraswani@medicare.com",
        "spec": "Pediatrician",
        "exp": 10,
        "fee": 400,
        "days": "Mon,Wed,Thu,Sat",
        "city": "Indore",
        "address": "Pipliyahana",
        "phone": "+91 98272 12345",
        "hospital": "Tender Care Child Clinic",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Sunil+Puraswani",
    },

    {
        "name": "Dr. Arpit Tiwari",
        "email": "dr.arpit.tiwari@medicare.com",
        "spec": "Orthopedic Surgeon",
        "exp": 15,
        "fee": 800,
        "days": "Mon,Tue,Thu,Fri",
        "city": "Indore",
        "address": "Arthros Multispeciality Clinic",
        "phone": "+91 98261 90123",
        "hospital": "Arthros Multispeciality Clinic",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Arpit+Tiwari",
    },

    {
        "name": "Dr. Arpana Jain",
        "email": "dr.arpana.jain@medicare.com",
        "spec": "Gynecologist",
        "exp": 20,
        "fee": 600,
        "days": "Tue,Wed,Fri,Sat",
        "city": "Indore",
        "address": "Sri Mangal Nagar",
        "phone": "+91 99077 67890",
        "hospital": "Motherhood Fertility Clinic",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Arpana+Jain",
    },

    {
        "name": "Dr. Jaideep Singh Chauhan",
        "email": "dr.jaideep.chauhan@medicare.com",
        "spec": "Dentist",
        "exp": 18,
        "fee": 500,
        "days": "Mon,Tue,Wed,Thu,Fri,Sat",
        "city": "Indore",
        "address": "Smile Makers Dental Centre",
        "phone": "+91 98930 34567",
        "hospital": "Smile Makers Dental Centre",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Jaideep+Singh+Chauhan",
    },

    {
        "name": "Dr. Anuj Bhardwaj",
        "email": "dr.anuj.bhardwaj@medicare.com",
        "spec": "Dermatologist",
        "exp": 14,
        "fee": 600,
        "days": "Mon,Wed,Thu,Sat",
        "city": "Indore",
        "address": "Genesis Cosmetology Centre",
        "phone": "+91 98272 67890",
        "hospital": "Genesis Cosmetology Centre",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Anuj+Bhardwaj",
    },

    {
        "name": "Dr. Siddhant Jain",
        "email": "dr.siddhant.jain@medicare.com",
        "spec": "Cardiologist",
        "exp": 19,
        "fee": 800,
        "days": "Mon,Tue,Wed,Thu,Fri",
        "city": "Indore",
        "address": "Rhythm Healthcare",
        "phone": "+91 98261 23456",
        "hospital": "Rhythm Healthcare",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Siddhant+Jain",
    },

    {
        "name": "Dr. Rakesh Jain",
        "email": "dr.rakesh.jain@medicare.com",
        "spec": "Cardiologist",
        "exp": 26,
        "fee": 500,
        "days": "Mon,Wed,Fri,Sat",
        "city": "Ujjain",
        "address": "Mahakal Hospital",
        "phone": "+91 99074 56789",
        "hospital": "Mahakal Hospital",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Rakesh+Jain",
    },

    {
        "name": "Dr. Sunita Chouhan",
        "email": "dr.sunita.chouhan@medicare.com",
        "spec": "Gynecologist",
        "exp": 25,
        "fee": 500,
        "days": "Tue,Thu,Sat",
        "city": "Ujjain",
        "address": "Govt Medical College",
        "phone": "+91 98930 89012",
        "hospital": "Govt Medical College Hospital",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Sunita+Chouhan",
    },

    {
        "name": "Dr. Rahul Jain (Ujjain)",
        "email": "dr.rahul.jain.ujjain@medicare.com",
        "spec": "Neurologist",
        "exp": 24,
        "fee": 600,
        "days": "Mon,Wed,Fri",
        "city": "Ujjain",
        "address": "R.D. Gardi Medical College",
        "phone": "+91 99077 12345",
        "hospital": "R.D. Gardi Medical College",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Rahul+Jain+Ujjain",
    },

    {
        "name": "Dr. Sunil Puraswani (Ujjain)",
        "email": "dr.sunil.ujjain@medicare.com",
        "spec": "Pediatrician",
        "exp": 10,
        "fee": 400,
        "days": "Tue,Thu,Sat",
        "city": "Ujjain",
        "address": "District Hospital",
        "phone": "+91 98272 99999",
        "hospital": "District Hospital",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Sunil+Puraswani+Ujjain",
    },

    {
        "name": "Dr. Arpana Jain (Ujjain)",
        "email": "dr.arpana.jain.ujjain@medicare.com",
        "spec": "Gynecologist",
        "exp": 20,
        "fee": 500,
        "days": "Mon,Wed,Sat",
        "city": "Ujjain",
        "address": "Sanjeevani Hospital",
        "phone": "+91 98261 77777",
        "hospital": "Sanjeevani Hospital",
        "photo": "https://api.dicebear.com/7.x/initials/svg?seed=Arpana+Jain+Ujjain",
    },

]

# ============================================================
# INSERT / UPDATE DATABASE
# ============================================================

added = 0
updated = 0

for d in doctors_data:

    existing = db.query(User).filter(User.email == d["email"]).first()

    info = (
        d["days"] + " | " +
        d["phone"] + " | " +
        d["hospital"] + " | " +
        d["address"] + " | " +
        d["city"] + " | " +
        d["photo"]
    )

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

        doctor = Doctor(
            user_id=user.id,
            specialization=d["spec"],
            experience=d["exp"],
            consultation_fee=d["fee"],
            available_days=info
        )

        db.add(doctor)
        db.commit()

        print(f"✅ Added: {d['name']}")
        added += 1

    else:

        doctor = db.query(Doctor).filter(
            Doctor.user_id == existing.id
        ).first()

        if doctor:
            doctor.specialization = d["spec"]
            doctor.experience = d["exp"]
            doctor.consultation_fee = d["fee"]
            doctor.available_days = info

            db.commit()

            print(f"🔄 Updated: {d['name']}")
            updated += 1

db.close()

print(f"\n🎉 Done! Added: {added} | Updated: {updated}")    