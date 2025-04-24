# LinkingLions

# **1. Project Title**

# **LinkingLions**

Linking Lions empowers Loyola Marymount University students and alumni to connect through a dedicated online platform, fostering mentorship, career exploration, and professional development, ultimately strengthening the LMU community and enhancing career outcomes for students.

# **Who are you helping?** 
Loyola Marymount University students, alumni, and professors.
# **What problem are you solving?** 
Bridging the gap between students and alumni to facilitate mentorship, networking, and career development opportunities.
# **How will you solve that problem?**
By creating an online platform with features for creating profiles, finding mentors, scheduling coffee chats, discovering relevant events, and accessing industry-specific resources.
# **What impact will your solution have?**
A stronger LMU community, enhanced student career opportunities, and a more engaged alumni network. Students will feel more prepared and confident going into the job search, and LMU will strengthen the opportunities it can place its students into.

# **What is the real problem being addressed?**
The real problem being addressed is the lack of a dedicated and comprehensive platform for Loyola Marymount University students and alumni to connect for mentorship, career exploration, and professional development. This lack of a centralized platform creates missed opportunities for valuable interactions and knowledge sharing between students and alumni, potentially hindering students' career preparation and alumni engagement with their alma mater. 

# **Past attempts to solve the problem** 
The Career and Professional Development has been put in place to solve this problem by providing the following services. 

**Handshake** is a platform where students can directly apply for open internships and full-time positions. Handshake also provides events for students in person and virtually to increase their knowledge of the industry and help them find new opportunities. The events product of Handshake is inconsistent, and many events that students "RSVP" for are not sent to the hosts of the events. Students who RSVP on Handshake are not guaranteed to be invited to the event, as Handshake is simply the middleman between the students and the employer. Students may waste time preparing for these events, and the individuals posting these events are wasting resources in finding these events. 

**LinkedIn Learning** is a tool that helps students take courses taught by industry professionals around a myriad of subjects. LMU provides this free of charge for its students. This is very good, however, students need direction on specific courses to take to guide them in the right direction. LinkingLions will help in this manner by reducing the time students waste taking courses that might not be relevant to their target professional roles. 

**BigInterview / V Mock** helps students work on their interview skills as well as their resumes. However, they only help with basic interview issues, like eye contact, using filler words, and other basics. While this is still a positive, interviewers are looking for specific industry knowledge, a very inspiring and well-spoken story, as well as a passion to join the specific firm, all of which BigInterview provides little support for. V Mock helps fix the wording and formatting of the resume, but individuals who are hiring students are not the ones giving feedback on the resumes. Students who score higher on V Mock are not more likely to be hired, and they might be wasting time and effort perfecting their resume according to the software rather than professional feedback.   

**The Pride** is a very good resource and has the same function as our end goal. The Pride allows students to set preferences and be given profiles of alumni that fit their criteria. However, it is not promoted well, and students should not have to provide very specific details about their goals, which might cost them a few alumni connections. For example, with simple search criteria of looking for a job, and building my resume for Finance, only two Alumni were selected that I could reach out to. It would be better for me to choose from the list of all Alumni who have obs in financial services, as they all could reasonably give resume help and promote jobs. The Pride is very similar to what we are trying to create, but we'd like to integrate more opportunities and events that students can attend, as well as industry-specific study material that students can learn as underclassmen before looking for internships and full-time roles.
# Links to the aforementioned solutions: 

**Handshake** - https://lmu.joinhandshake.com/explore, 							 

**LinkedIn Learning** - https://careers.lmu.edu/linkedin-learning/

**V - Mock** - https://www.vmock.com/lmu, 

**BigInterview** - https://lmu.biginterview.com/
`	

# **ISBA Subfields**

1. **Data Management** 

**Role**: Crucial for designing and implementing the database that will store and manage all the platform's data. This includes: Designing the schema for user profiles, events, interview questions, case studies, and other relevant data points. Ensuring data integrity and security. Optimizing database performance for efficient data retrieval and analysis.

**Tools**: SQL, database management systems (DBMS) like MySQL or PostgreSQL, and potentially cloud-based database solutions.

2. **Web Development**

**Role**: Essential for building the front-end and back-end of the "Linking Lions" website. This involves: Designing the user interface (UI) and user experience (UX) for optimal usability and engagement. Developing the website's functionality, including user registration, profile creation, search and filtering, event management, and communication features. Integrating the website with Salesforce and potentially other systems (e.g., university databases, authentication systems).

**Tools**: HTML, CSS, JavaScript, web frameworks (e.g., React, Angular), and potentially Salesforce development tools (Apex, Visualforce).

3. **Business Analytics**

**Role**: Valuable for analyzing platform usage data and generating insights to improve the platform's effectiveness. This includes: Tracking key metrics like user engagement, coffee chat frequency, event attendance, and resource usage. Analyzing user behavior and preferences to identify areas for improvement. Generating reports and visualizations to communicate insights to stakeholders.

**Tools**: Data analysis tools (e.g., Python with Pandas, R), data visualization tools (e.g., Tableau, Power BI), and potentially Salesforce reporting and analytics tools.

# **Solution Overview**

We built a dynamic system that connects a growing alumni database to a live website. Using Airtable as the backend, we created a centralized, easy-to-update spreadsheet where new entries can be added at any time. Then, we connected that database to a fully functional Flask-based web app. This allows the website to automatically pull and display up-to-date data, like names, graduation years, job titles, and LinkedIn profiles, without needing to manually update the code.

LMU students can use the website to easily explore and search for alumni who match their career interests — whether by industry, job title, or graduation year — and reach out via LinkedIn to build connections and gain insight.

 # **Tech Stack**

Python
Flask
LinkedIn API
AirTable
Heroku

# **Solution Details**

Our project aimed to build a scalable and user-friendly platform that allows Loyola Marymount University (LMU) students to access and explore an up-to-date alumni directory. We began by uploading an existing dataset into Airtable, which served as the backend database due to its intuitive spreadsheet interface and cloud-based accessibility. This structure allows the dataset to grow over time with minimal technical overhead — new entries can easily be added or modified by non-technical users, ensuring long-term maintainability.

To power the frontend experience, we used Python and the Flask framework to connect to the Airtable database via its API. The requests library handled the API integration, pulling alumni records in JSON format. The data was then parsed and passed into HTML templates rendered with Jinja2, allowing us to dynamically populate the website with real-time information from Airtable. The web application was deployed using Heroku, making the site publicly accessible and easy to scale.

In addition to the core data integration, we incorporated the LinkedIn API to enhance data accuracy and keep information current. Specifically, the API was used to update the "Job Title" column in Airtable by cross-referencing LinkedIn profiles associated with each alumni. This automated enrichment ensured that users accessing the site would be viewing the most relevant and recent career information.

We followed a simplified Software Development Life Cycle (SDLC) methodology to build the solution. The process began with requirements gathering, focusing on LMU students’ need to explore alumni by career field, industry, and graduation year. During the design phase, we chose Airtable for its ease of use and integrated it with Flask for backend logic and Heroku for deployment. We implemented and tested each component locally, verifying that data flowed correctly from Airtable to the live site. Finally, the system was deployed to Heroku with a fully functional web interface that displays clean, organized alumni data, including names, graduation years, job titles, and LinkedIn links labeled as “Profile.”

This solution not only bridges the gap between students and alumni but also provides a live, growing resource that can evolve with future needs. With Airtable as a flexible backend, Flask as the routing engine, and Heroku as a cloud host, the project is both technically sound and accessible to users at every level.

#**Next Steps**

**Abandoned / Scaled**
Initially, we explored using Salesforce as the primary platform to house and manage the alumni database. However, due to the complexity of Salesforce’s data model, permissions system, and integration requirements, we ultimately decided it was not the right fit for our team’s timeline and technical goals. Instead, we pivoted to Airtable, which provided a simpler, more accessible solution for both technical and non-technical contributors.

We also considered building out individual alumni profile pages early on, but due to time constraints and the need to finalize core functionality, that feature was deprioritized in this version.

**Deployment**
Environment variables (like the Airtable API key) should be stored securely using .env files or Heroku Config Vars.
Implement user authentication if write-access or admin panels are needed.
Set up a custom domain and enable HTTPS via Heroku’s free SSL.
Optionally, move static assets to a CDN and enable Flask caching for performance.

**Scaling**

**Throughput**: Airtable's API handles pagination and can support thousands of records. The Flask app is optimized to fetch all records using offsets and sort them efficiently.

**Adoption**: The clean frontend makes it easy for LMU students to engage with the alumni network. Future versions can easily integrate features like search, filtering, or category tags to increase usability.

The system can also support multi-tab expansion (e.g., events, internships, job postings) without major architectural changes.

**Future Improvement**

**Multi-tab Web Navigation**: Add pages or tabs for events, internships, or industry spotlights.

**Alumni Profiles**: Create individual profile pages for each alumnus with additional context (bios, majors, locations, mentorship interests, etc.).

**Data Input Forms**: Implement an alumni-facing submission form where users can update or add their own information, syncing directly to Airtable or an integrated backend.

**Search and Filter Functionality**: Add advanced filtering (e.g., by industry, grad year, role) to enhance discoverability.

**Admin Dashboard**: Build a simple password-protected interface to review submissions or approve updates.
