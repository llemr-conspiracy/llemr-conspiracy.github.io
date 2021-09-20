Title: Launching LLEMR at UMKC
Date: 2021-09-20 10:20
Author: Eshwar Kishore


If you are a member of a student-run free clinic or similar group looking to launch an electronic medical record (EMR) to your clinic, you’re in the right place. My name is Eshwar and I am a student at the University of Missouri-Kansas City (UMKC) School of Medicine who was responsible for driving the deployment of LLEMR (formerly Osler) to our student-run free clinic in August 2020. My goal with this article is to share with you how we went from working nearly 17 years with paper charts to fully transitioning over to electronic medical records, with the help of the LLEMR development team. I’ll discuss:

* a brief history of our clinic’s setup
* what made us specifically choose LLEMR
* the significant obstacles we faced prior to deployment
* some of the biggest tips that I can offer
* how we (and you can!) were able to mold LLEMR to fit our specific needs
* some ongoing challenges we are actively addressing

Let’s get started and dive into how you too can adopt LLEMR at your clinic...

## The Clinic’s History

To provide some background, the Sojourner Health Clinic was established in October 2004 as a student-run free clinic serving the medically indigent of downtown Kansas City, Missouri. Since that time, our clinic has operated a full medical clinic on Sunday mornings with a robust array of resources including an in-house laboratory, medication dispensary, and social work services, as well as fresh meals.

Sojourner is an independent organization affiliated with the UMKC Foundation and supported by the UMKC School of Medicine. We are operated by an executive board composed of UMKC medical and other health science discipline students. More information regarding our clinic’s setup and history can be found [here](www.sojournerhealthclinic.com).

## Life Before EMR: Paper Charts

For medical records, we had previously been using a paper chart system that consisted of folders with patients’ protected health information (PHI) securely stored in on-site filing cabinets. Key issues with this model included handwriting legibility, wear-and-tear of older charts, reliance on alphabetization-based storage that was frequently misordered, and no efficient way to collect quality improvement data.

For many years, we had also been using encrypted Excel spreadsheets for data such as laboratory test results and a medication dispensing log. This resulted in cumbersome communication between departments, such as between students seeing patients and those performing laboratory testing or filling medication prescriptions. Volunteers created temporary solutions to these problems, such as a whiteboard tracker to follow a patient’s progress through the clinic or individual patient lab result sheets that limited the need to go between departments for testing results. However, these workarounds did not resolve the underlying issue. Our clinic was not unique in having these problems, which was something I was able to appreciate when attending the annual Society of Student-Run Free Clinics conference in February 2018.

## What is & Why LLEMR?

LLEMR (**L**LEMR is a **L**ightweight **EMR**) was originally developed by Justin Porter at the Washington University in St. Louis (WUSTL) when he recognized their free clinic (Saturday Neighborhood Health Clinic) had a need for a system not currently available: a lightweight EMR not weighed down by the dozens of features in commercial EMRs that are unnecessary in a free clinic context. After developing the system and successfully running it at the WUSTL free clinic for 2 years, his team presented their work at the Society of Student-Run Free Clinics conference. When I attended this conference in 2018, I was already coming in with the mindset of how we could technologically improve our clinic’s function.

Previously, our clinic had considered paid services like Chronic Disease Electronic Management System around 2010, Practice Fusion around 2015, and Point and Click around 2018. Each service, however, proved to be inflexible with a user interface model focused on collecting billing data that required too many clicks and overall did not suit our uninsured patients’ needs. LLEMR had the added benefit of being free to us as well as being medical student-made with a clear insight into what a free clinic’s EMR needed--other systems were either too complicated or didn’t have the specific features we required.

It’s also important to note that not everyone who has or will deploy LLEMR at their own clinic is necessarily starting from paper records as we were. I have spoken with other folks about their current EMR systems and they echoed how those companies either ultimately switched to a paid model or were failing them in another area such as simplicity.

Additionally, our clinic has high volunteer turnover--there will often be students who only volunteer a handful of times in their medical school career. We needed a system that would not require in-depth EMR training and reorienting prior to use and LLEMR has always been intuitive, even for first-time volunteers.

The last, and extremely important, reason for picking LLEMR was its customizability. The LLEMR development team was committed to helping us mold their current software to our unique clinic flow and patient medical record format. I’ll explain more in-depth below about how it was possible for us to mold LLEMR to fit the Sojourner Clinic’s specific needs and how you can do the same.

Since our first meeting, the team has grown into a fantastic group of helpful individuals with even more support than ever before who have continued to expand upon what LLEMR can offer us. It was truly because of their support and desire to keep the project moving that we were able to approach our technology administrators at UMKC with this novel idea.

## Primary Obstacles: The Process

Our process took almost three years, but it is my goal to identify the key challenges we faced so that it will be easier for the next clinic to take these similar steps. I took these first steps by reaching out to a known contact in our school’s IT department. Overall, we were blessed to have strong support from our information technology (IT) specialists, information security team, legal department, faculty advisors, and Dean’s office. They were critical personnel to get involved in the initial years of approving LLEMR for deployment at our clinic. He was immediately invested in helping champion the process and handled most of the technical aspects from the UMKC side. With only a minimal background in computer programming, I felt confident enough to help drive the conversation and dictate how LLEMR needed to be modified for our clinic--more on developing software feature requirements down below--but was able to lean on Justin and the LLEMR team to do the bulk of explaining and deciphering of UMKC’s technical safety requirements.

There was some natural initial concern to using student-made, open-source code for something as sensitive and protected as PHI. Having the open-source code available on GitHub allowed our IT folks to do their due diligence. Our IT department also initially questioned if the LLEMR team had considered basic data security features such as a vulnerability scan and Health Insurance Portability and Accountability Act (HIPAA) review processes. To our benefit, WUSTL’s IT folks were already performing vulnerability scans on the software multiple times per year, which helped prove the legitimacy of LLEMR’s security. Other considerations from our information security and IT departments included the need for a firewall prior to launching the server, and eventual legal approval.

Our legal counsel from the University of Missouri system was able to assist us by providing both oversight and guidance on UMKC’s Management of Health Information policy--likely other university-affiliated health clinics will have similar policies to review. The bulk of the process during late 2018 into early 2020 involved methodically checking in with the various departments at UMKC to ensure transparency, technical and legal oversight, and feasibility of the project, while slowly moving towards the end goal.

## Secondary Obstacles: Logistics

The other obstacles we faced involved mostly logistics for the hardware and subsequent funding we’d need for these items. Our clinic gratefully has the sponsorship of several federal and private grants providing the bulk of our funding and we were able to include the various costs of running LLEMR into our grant budgets. Listed below are some of the things you may need to consider budgeting for in order to run LLEMR:

1. University servers (hardware)
1. Firewall installation and maintenance
1. University electronic mailbox license
1. Monthly unlimited data plan
1. Internet router
1. On-site laptops *most students/faculty also bring their own
1. Safe for protection of on-site technology/hardware

## Tips

One of the biggest tips I would recommend to anyone wanting to adopt LLEMR to your clinic is tenacity. This was overall a long and arduous process, often feeling like it would not or could not happen. I had the benefit of being able to lean on both the Sojourner Clinic board and the LLEMR team for support because we all had a common goal: launching LLEMR to its first satellite clinic. At this stage, we have definitive proof (us!) that the software works--and a new clinic likely won’t need this amount of troubleshooting after we have paved the way.

It was incredibly important to learn to be an effective administrator, as a lot of the process was communicating between different technical departments and the LLEMR team. At the end of the day, our clinic had a lot of help from people who were not obligated to help us. A majority of the time, I was following along with discussions and taking notes with the goal of summarizing and coming up with a list of action items and deadlines. Being courteous, professional, and well-intentioned was critical to moving the project along, email by email and day by day. If you’re like me, with minimal computer science background or training, then you will be relying on experts in the field to do the hard work. You will be most useful as the clinical representative who is able to visualize and express their end goal. And, of course, befriending your IT department will do you wonders!

I’d also recommend getting faculty advisors and any oversight administrators (i.e. Dean’s office) onboard soon. It was important for me and the rest of our clinic leadership to have their approval before moving forward on such a significant step. The right time to loop them in would be after you’ve done your homework, have more than just a proof of concept, and are ready to explain what obstacles exactly need to be overcome to do that. Hopefully, this article gives you that launching point. I also can’t say it enough--reach out to the LLEMR development team and they will be able to help guide you through this process.

## Shaping LLEMR for Your Clinic: Make Changes!

Personally, I found the most advantageous part of using LLEMR was how we were able to mold the software to fit our specific clinic needs--and you can too! There were significant differences between the original WUSTL/Saturday Neighborhood Clinic deployment and our UMKC/Sojourner Health Clinic deployment.

Some big ones were the existence of a referral system--we only operate on Sundays and take care of everything we can in-house--and the lack of some key departments such as our laboratory and dispensary represented in the EMR. However, as stated above, the similarities just by virtue of being a free clinic meant that, with some tweaking, the system could easily work at our specific site. In fact, LLEMR was a fully functioning system that could have been deployed instantly (IT/legal approval notwithstanding) however due to all of the technical and administrative hoops that we had to jump through, we had the time to fully mold LLEMR to be more “Sojourner-specific”.

Some of these changes were as simple as syntax changes (changing the title of Coordinator to Manager) that were practically non-issues due to the system’s user interface. Other changes such as removing the follow-up or referral system in favor of only a standard medical note and secondary free-text note type required communication with the LLEMR team of our specific needs and some coding changes on their end.

## Shaping LLEMR for Your Clinic: Create New Features!

The most significant changes were for departments unique to us like our point of care laboratory and in-house dispensary. I put together software feature requirements for new EMR modules such as a drug inventory, laboratory test charting, and quality improvement dashboard. My minimal background in programming in addition to my clinical background as a medical student (both in working with a hospital EMR and volunteering at our clinic) was the most useful as I was able to translate what we needed/what worked for us into requests for the LLEMR team.

Some of the differences between the Sojourner-version of LLEMR versus other clinics are now fairly modular (think “build your own EMR”) to toggle between for your specifications. Brand new features require some planning and coding. With some discussion, they were able to build software for practically anything we needed! This was beneficial to our clinic, the LLEMR team, and, hopefully, future clinics as the software has only grown more comprehensive and utilizable over the last several years.

## Training Modules

I also put together [training modules](http://www.sojournerhealthclinic.com/?page_id=1755) to address the issue of high volunteer turnover. The goal was to make them simple to watch and as intuitive to follow as the EMR software. I created one for each major activity a volunteer might have to complete using the EMR and categorized them by department/student discipline. This was important especially for the Sojourner-specific changes that we implemented and are required for all our new volunteers prior to attending a clinic day.

## A Work in Progress: Always Improving

There are also ongoing challenges that we continue to face that are important to recognize as you’ll likely encounter them. With our unique situation of being off-site from the medical school that houses our virtual machine servers, we use a VPN to remotely access these servers. Securing the funding for or access to a stable internet connection has been a vital and sometimes challenging obstacle for our clinic. One way that we’ve prepared for a “day without Wi-Fi” is to have paper chart templates on hand (already used by our clinic volunteers for any handwritten notes they might want to take prior to writing their EMR notes). Although this has never happened to us, we’ve certainly faced days with slower or limited internet connection. We’ve worked through this problem by using personal hotspots and then by obtaining grant funding for a new Wi-Fi hotspot. We also ask volunteers to bring their own personal laptops as they might do for other clinical rotations but have since purchased our own Sojourner Clinic laptops that are available to anyone.

Another difficulty has been the manual process of having a student administrator create LLEMR accounts for each student volunteer, as there needs to be a security measure in place when creating these accounts with access to PHI. One approach in development is to automate the creation of these accounts for a set list of pre-defined, pre-”cleared” users.

Lastly, and more importantly, with student turnover due to eventual graduation, it is critical to establish a transition process so that knowledge on how to administer the EMR from the clinic side, contact information for members of the LLEMR development team, and a relationship with your institution’s IT department (if applicable) is not lost. I established the EMR Liaison position to guarantee sustainability for LLEMR at our clinic and prioritized this in my final year as a student at UMKC. Although the EMR system works, there will always be a need for improvement, further customization, and a good relationship with all the support staff we require to keep LLEMR running smoothly at the Sojourner Clinic.

## My Highest Recommendation to the LLEMR Team

I hope that this article presents you with a clear foundation of how we launched LLEMR to our clinic and how you can take the next steps to do the same. It is a long process but will be incredibly rewarding to both your patients and staff, especially if you are transitioning from paper charts to electronic records. The LLEMR system is not for every clinic but I hope that your clinic model is similar to ours or that you can clearly see how this would work for your needs. At the time of this article being published (September 2021), the Sojourner Health Clinic has been fully operating on LLEMR for one year and we are extremely confident in our decision.

We have already seen significant improvement in our clinic’s efficiency, continuity of care with legible charting, and ability to collect/interpret quality improvement data. These claims are substantiated by the exceptionally positive feedback of our volunteers and we look forward to studying LLEMR’s impact on our clinic in the years to come. As an outsider who has worked closely with the LLEMR development team for over three years, I can wholeheartedly vouch for their work ethic, reliability, and commitment to helping us serve our patients. You are in excellent hands with the LLEMR Conspiracy!

*Thank you to Christopher Boyce, Justin Malyn, Frank Magrone, Shaun Ferguson, and the entire UMKC IT department. Thank you to Mary Anne Jackson, Paul Cuddy, Andy Goodenow, Sheryl Fetuz-Harter, and the entire UMKC Dean’s office and administration. Thank you to Angela Barnett, Dan Purdom, Ed Kraemer, and all of our Sojourner faculty and student board members. Thank you to Justin Porter, Will Wick, Eric Sallinger, Minerva Zhou, Artur Meller, Moses Chung, Clara Liu, and the incredible LLEMR development team. Your patience, hard work, and support for launching this project will always be greatly appreciated!*
