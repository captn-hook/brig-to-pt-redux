# brig-to-pt-redux
## Setup
DOWNLOAD Blender and EXTRACT into this dir and RENAME dir to blender
https://mirrors.ocf.berkeley.edu/blender/release/Blender3.6/blender-3.6.4-linux-x64.tar.xz

put SECRETS in /secrets/key.json

# Run as container
docker build --tag=brigo .
docker run -p 6743:6743 brigo

# Run Locally with gunicorn
gunicorn --bind 0.0.0.0:6743 wsgi:app

## TEST Example
curl -X POST http://127.0.0.1:6743/ \
-H 'Content-Type: application/json' \
-d '{"csv":"Labels,M0,M1,M2,M3,M4,M5,M6\\nT0,XYZ,0.17563477758749513/4.490553112218072/-1.5146760940551758,-2.4134653117772578/4.424593555763652/-1.5146760940551758,-4.494030955522833/2.320687800201369/-1.5146760940551758,-3.8836981419199446/-4.770267617961238/-0.7210200428962708,-0.10254079079052375/-3.0129642278473985/-1.0994699001312256,3.9143245405279052/0.39631540602334114/-1.5146760940551758\\nD1,0.4311639838603687/2.3706164862575227/-1.5146760940551758,1,1,2,0.5,0.01,0.1\\nD2,-4.9760013686234394/4.898032086315533/-1.5146760940551793,0.01,0.5,5,0.15,0.3,0.15\\nD3,2.5247297225413945/1.7026304622719601/-1.514676094055174,0.5,0.01,0.5,0.5,0.3,0.3\\nD4,-2.300522732717726/2.3692873775680363/-1.514676094055174,0.01,0.15,10,0.5,0.3,0.1\\nD5,-0.31667054786028265/0.5821998575768994/-1.5146760940551758,0.3,0.3,0.5,0.5,0.5,0.3\\nD6,-4.299745076052533/-1.4840413308192257/-1.5146760940551722,0.3,0.1,0.5,20,0.5,0.1\\nD7,-1.1049336410660688/-1.225188887261904/-0.6922810702606128,0.1,0.3,0.5,100,15,0.3\\nD8,2.8423047873323792/-1.6578241576393582/-1.3005728721618688,0.15,0.3,0.5,0.5,0.5,50\\nINSIGHTS,,,,,,,\\nVIEWS,11.301858186721802/30.08887505531311/9.464874505996704,11.521122455596924/30.790950894355774/14.72138786315918,22.561708450317383/30.00527387857437/11.633445501327515,22.359580039978027/30.81994366645813/13.898128986358643,29.85641574859619/30.48754271864891/14.573328495025635,33.78324317932129/31.02504527568817/13.945435047149658", "model":"Example/Example.glb", "bucket":"brig-b2ca3.appspot.com"}'

curl -X POST http://127.0.0.1:6743/ \
-H 'Content-Type: application/json' \
-d '{"csv":"Labels,M0,M1,M2,M3,M4,M5,M6\nT0,XYZ,0.17563477758749513/4.490553112218072/-1.5146760940551758,-2.4134653117772578/4.424593555763652/-1.5146760940551758,-4.494030955522833/2.320687800201369/-1.5146760940551758,-3.8836981419199446/-4.770267617961238/-0.7210200428962708,-0.10254079079052375/-3.0129642278473985/-1.0994699001312256,3.9143245405279052/0.39631540602334114/-1.5146760940551758\nD1,0.4311639838603687/2.3706164862575227/-1.5146760940551758,1,1,2,0.5,0.01,0.1\nD2,-4.9760013686234394/4.898032086315533/-1.5146760940551793,0.01,0.5,5,0.15,0.3,0.15\nD3,2.5247297225413945/1.7026304622719601/-1.514676094055174,0.5,0.01,0.5,0.5,0.3,0.3\nD4,-2.300522732717726/2.3692873775680363/-1.514676094055174,0.01,0.15,10,0.5,0.3,0.1\nD5,-0.31667054786028265/0.5821998575768994/-1.5146760940551758,0.3,0.3,0.5,0.5,0.5,0.3\nD6,-4.299745076052533/-1.4840413308192257/-1.5146760940551722,0.3,0.1,0.5,20,0.5,0.1\nD7,-1.1049336410660688/-1.225188887261904/-0.6922810702606128,0.1,0.3,0.5,100,15,0.3\nD8,2.8423047873323792/-1.6578241576393582/-1.3005728721618688,0.15,0.3,0.5,0.5,0.5,50\nINSIGHTS,,,,,,,\nVIEWS,11.301858186721802/30.08887505531311/9.464874505996704,11.521122455596924/30.790950894355774/14.72138786315918,22.561708450317383/30.00527387857437/11.633445501327515,22.359580039978027/30.81994366645813/13.898128986358643,29.85641574859619/30.48754271864891/14.573328495025635,33.78324317932129/31.02504527568817/13.945435047149658", "model":"Example/Example.glb", "bucket":"brig-b2ca3.appspot.com"}'

curl -X POST http://127.0.0.1:6743/ \
-H 'Content-Type: application/json' \
-d '{"csv":"Labels,M0,M1\nT0,XYZ,0.17563477758749513/4.490553112218072/-1.5146760940551758\nD1,0.4311639838603687/2.3706164862575227/-1.5146760940551758,1\nINSIGHTS\nVIEWS,11.301858186721802/30.08887505531311/9.464874505996704", "model":"Sites/SmallHouse/SmallHouse.glb", "bucket":"brig-b2ca3.appspot.com"}'



# NOTES
https://console.cloud.google.com/run?project=brig-b2ca3
cloud run should handle auth when running in same project

images are currentl uploaded to 
gs://brig-b2ca3.appspot.com/Images/model/output
where 'model' is the supplied model name

#notes
files need better naming for upload
first letter of images is getting clipped
upload .blend
fix cameras
put invis plane in brig for click
image viewer
single image gen

#notes
files need better naming for upload
first letter of images is getting clipped
upload .blend
fix cameras
put invis plane in brig for click
image viewer
single image gen