echo $@ #1 argument, the ./<folder>/ that has ./<folder>/*.csv and ./<folder>/*.glb
#will create three folders and corresponding images ./<folder>/output/(opaque|transparent|background)/0..n.png
#and a blend file ./<folder>/output.blend

#Column 0: Y Labels, Column 1: Y Positions, Column 2..n: Values
#Row 0: X Labels, Row 1: X Positions, Row 2..n: Values
#(0..1, 0..1): Unused

#get column length
length=$(head -n 1 $1/*.csv | tr ',' '\n' | wc -l)
echo $length

# the python script will configure
# blender --background --python worker.py -- "$@"
# # ren
# #then rename img 0 to Overview.png and 1..n.png to XLabel[n].png
# echo done rendering
# echo $(ls $1/output/*.png)
#blender --background --python ./container/app/server/worker.py -- "$@" #--render-frame 0..$length --render-output $1/output/
blender/blender -b --python ./container/app/server/worker.py -- "$@" #--render-frame 0..$length --render-output $1/output/
#pause for user
#read -p "Press enter to continue"
#blender --background  $1/output.blend --render-frame 0..$length --render-output $1/output/
blender/blender -b $1/output.blend --render-frame 0..$length --render-output $1/output/
#get row 0 of csv
#remove first column (loop below will start at 0 and skip first elem of this array)
labels=$(head -n 1 $1/*.csv | tr ',' '\n' | tail -n +2)
echo $labels


# #for every folder in output
# for folder in $1/output/*; do
#     #for every file in folder
#     for file in $folder/*; do
#         #if file is a png
#         if [[ $file == *.png ]]; then
#             #if file is not Overview.png
#             if [[ $file != *0.png ]]; then
#                 #rename file to XLabel[n].png
#                 mv $file $folder/$(echo $labels | cut -d' ' -f$(echo $file | cut -d'/' -f3 | cut -d'.' -f1))
#             else
#                 #rename file to Overview.png
#                 mv $file $folder/Overview.png
#             fi
#         fi
#     done
# done
