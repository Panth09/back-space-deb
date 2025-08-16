A way to find and look at junk in space

   A platform that uses AI to help you find space junk, figure out how likely it is to hit something, and make the data more real with interactive visuals.    The system uses advanced object detection models and a web dashboard to show users threats as they happen. This helps them make more intelligent decisions.

   🚀 Why This Is Important

   Space junk is a big problem for satellites that are already in space and for missions that will happen in the future.    This initiative fixes the problem by automatically finding space junk in satellite images, figuring out how likely it is to hit something, and showing the results in a way that is easy for anyone to comprehend and use.

   What You Get

   Automated Debris Detection: Models like YOLOv5 and Faster R-CNN can use satellite images to find debris with a lot of accuracy.

   AI can tell you how likely it is that two things will hit each other at this moment.

   It's easier to understand complicated data when you can see it in both 2D and 3D with Three.js and D3.js.

   You can get real-time inferences from this because it was made with FastAPI and Flask.

   For reliable metadata and results, use either MongoDB or PostgreSQL.

   The React.js front end makes it easy for people to upload photos and get information right away.

   Cloud Deployment: You can use AWS, Heroku, Vercel, or Netlify to make it bigger and get to it.

   🛠️ A Group of Tools

   You can use Python, MongoDB/PostgreSQL, FastAPI, or Flask for the AI and the backend.

   We use WebSockets/AJAX, React.js, Three.js, and D3.js for the front end.

   You can put your app on AWS, Heroku, Vercel, and Netlify.

   Key Parts

   Preparing the data and teaching the model

   Get satellite data and prepare it for use.

   Change the size of pictures, add to them, and make them look normal.

   Train models that can find things using the best hyperparameters.

   Check with mAP and IoU.

   Connecting models and APIs

   Train models so that they can be used to make predictions.

   The backend sends predictions using REST and WebSocket APIs.

   Store the metadata and results in the database.

   Frontend that lets you do things

   People can send pictures from satellites right away.

   The dashboard shows detections and predictions as they happen.

   You can easily see satellites and trash in 3D.

   🔄 Workflow in Action

   The AI model looks at pictures, finds trash, and figures out how likely it is that a crash will happen.

   The backend API saves the results and then uses them.

   You can get information by clicking on graphs and other pictures on the front-end dashboard.

   The database keeps a complete record for analysis and reporting.

   Things can grow and change right away when you use the cloud.

   ⚡ How to Begin

   Copy the repo:

   git clone https://github.com/Panth09/back-space-deb.git


   Set up the AI, backend, and frontend's dependencies.

   Turn on the model server and the backend, and set up the database.

   Start the front end and link it to the API.

   Upload some sample photos and see what the debris detection found.

   📖 Paperwork

   AI Training and Evaluation → docs/ai_model.md

   Docs/api.md talks about the API on the back end.

   Frontend Guide → docs/frontend.md

   Deployment → docs/deployment.md

   🤝 Working together

   It's best to have regular meetings and check-ins.

   The backend team changes the AI model.

   A lot of the time, the backend and frontend teams work on APIs together.
