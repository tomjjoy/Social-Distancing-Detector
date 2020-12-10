import numpy as np
from scipy import stats



def pixels_per_metric(x):
  '''Calculates Pixel per metric (inches)'''

  tl, br = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))

  top_y = tl[1]
  bottom_y = br[1]
  h = top_y - bottom_y
  avg_height = 54

  return abs(avg_height / h)


def img_height(x, ppm):
  '''Calculates height of bbox'''

  tl, tr, bl, br = (int(x[0]), int(x[1])), (int(x[2]), int(x[1])), (int(x[0]), int(x[3])), (int(x[2]), int(x[3]))
  top_x, top_y, bottom_x, bottom_y = tl[0], tl[1], br[0], br[1]
  height = abs(top_y - bottom_y)*ppm

  return height

def dist(x1, y1, x2, y2, ppm):
  '''calculate the distance between 2 2D points using distance formula'''
  return round(np.sqrt((x2-x1)**2 + (y2-y1)**2) * ppm, 2)


def img_distance(img, obj, count, ppm):
  '''Calculates this distance between bbox with all the other bboxs' on frame'''

  tl1, tr1, bl1, br1 = img[0], img[1], img[2], img[3] #each point is (x,y)
  tl1x, tl1y = tl1[0], tl1[1]
  tr1x, tr1y = tr1[0], tr1[1]
  bl1x, bl1y = bl1[0], bl1[1]
  br1x, br1y = br1[0], br1[1]

  dist_obj = {}
  dist_list = {}
  for k, v in obj.items():
    if v == img:
      pass
    else:
      tl2, tr2, bl2, br2 = v[0], v[1], v[2], v[3] #each point is (x,y)
      tl2x, tl2y = tl2[0], tl2[1]
      tr2x, tr2y = tr2[0], tr2[1]
      bl2x, bl2y = bl2[0], bl2[1]
      br2x, br2y = br2[0], br2[1]

      tl_dist = dist(tl1x, tl1y, tl2x, tl2y, ppm)
      tr_dist = dist(tr1x, tr1y, tr2x, tr2y, ppm)
      bl_dist = dist(bl1x, bl1y, bl2x, bl2y, ppm)
      br_dist = dist(br1x, br1y, br2x, br2y, ppm)

      dist_obj[k] = round(np.mean([tl_dist, tr_dist, bl_dist, br_dist]), 2)
      dist_list[round(np.mean([tl_dist, tr_dist, bl_dist, br_dist]), 2)] = [[tl_dist, tr_dist, bl_dist, br_dist]]
  #print(count,'-',dist_list)
  return dist_obj


    







