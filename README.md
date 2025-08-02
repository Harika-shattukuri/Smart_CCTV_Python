# Smart CCTV - REPORT.md

## 1.1 Team Information

**Team Name:** Smart CCTV Team  
**Project Name:** Smart CCTV  
**Team Members:**
- Meghana  
- Trisha  
- Bhuvana  
- Harika  
- Harini  

---

## 1.2 Application Overview

Smart CCTV is an AI-powered surveillance solution designed to enhance traditional CCTV systems by automatically detecting and isolating segments of video footage that contain meaningful activity. Traditional systems record continuously, resulting in vast amounts of idle data. Our Minimum Viable Product (MVP) focuses on identifying human motion and auditory cues such as sudden noises to filter out inactive periods in the footage. The system then trims and flags only the important clips for review. This greatly simplifies and accelerates the process of analyzing surveillance data.

---

## 1.3 AI Integration Details

The application integrates computer vision and audio analysis techniques to detect relevant activity. For video processing, we use OpenCV along with a pre-trained action recognition model (e.g., I3D or MobileNet-based architectures). For sound detection, a simple noise thresholding mechanism combined with audio classification is implemented to capture unusual auditory events. These AI modules are orchestrated to run in real-time or batch mode depending on the system constraints.

---

## 1.4 Technical Architecture & Development

The Smart CCTV system consists of the following components:

- **Input Module:** Receives continuous video and audio streams from surveillance cameras.  
- **Processing Module:** Performs motion detection, action recognition, and noise filtering.  
- **Trimming & Indexing Module:** Extracts relevant video segments and organizes them for review.  
- **Frontend Interface (MVP Scope):** A minimal dashboard that allows users to view flagged events and download footage clips.  

Development Tools & Stack:
- Python (OpenCV, TensorFlow/PyTorch)
- Flask (for API handling)
- SQLite (for MVP-level data logging)
- HTML/CSS + JS (for frontend dashboard)

---

## 1.5 User Testing & Feedback

**Testing Period:** Week 2  
**Methodology:**  
During Week 2, we conducted in-house testing with simulated surveillance data. Each team member acted as a test user to evaluate:
- Accuracy of motion detection
- Relevance of extracted video clips
- Ease of use of the frontend interface  

**Feedback Highlights:**
- Users appreciated the reduction in footage length and found it easier to locate key events.
- Some false positives were noted in low-light conditions, prompting adjustments to threshold sensitivity.
- Dashboard suggestions included adding timestamps and clip previews, which were added in Week 3.

---

## 1.6 Project Lifecycle & Roadmap

The Smart CCTV project followed a structured 4-week timeline:

### **Week 1: Planning & Initial Setup**
- Finalized the project idea and divided roles.
- Researched existing CCTV and action recognition technologies.
- Defined MVP scope and architecture.
- Set up GitHub repo, environment, and initial dataset collection.

### **Week 2: Core Feature Development & Testing**
- Implemented motion and noise detection modules.
- Integrated basic video trimming logic.
- Conducted internal user testing with feedback analysis.
- Identified improvements for model accuracy and user interface.

### **Week 3: AI Model Integration & UI Enhancement**
- Integrated pretrained action recognition models.
- Tuned parameters to reduce false positives.
- Built a simple web dashboard to preview extracted clips.
- Added timestamping and labeling features based on Week 2 feedback.

### **Week 4: Final Optimization & Documentation**
- Cleaned and optimized codebase.
- Final testing using real surveillance data samples.
- Prepared final documentation and presentation materials.
- Reviewed project deliverables for deployment or future expansion.

---


