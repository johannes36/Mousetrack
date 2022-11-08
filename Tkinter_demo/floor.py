#! /usr/bin/env python

"""
floor.py

This demonstration script creates a canvas widet that displays the
floorplan for DEC's Western Research Laboratory.

June 20, 2005

"""


import Tkinter as Tk
import template as A


##-----------------------------------------------------------------------------------
## data


floor1_ = \
(347, 80, 349, 82, 351, 84, 353, 85, 363, 92, 375, 99, 386, 104, \
386, 129, 398, 129, 398, 162, 484, 162, 484, 129, 559, 129, 559, 133, 725, \
133, 725, 129, 802, 129, 802, 389, 644, 389, 644, 391, 559, 391, 559, 327, \
508, 327, 508, 311, 484, 311, 484, 278, 395, 278, 395, 288, 400, 288, 404, \
288, 409, 290, 413, 292, 418, 297, 421, 302, 422, 309, 421, 318, 417, 325, \
411, 330, 405, 332, 397, 333, 344, 333, 340, 334, 336, 336, 335, 338, 332, \
342, 331, 347, 332, 351, 334, 354, 336, 357, 341, 359, 340, 360, 335, 363, \
331, 365, 326, 366, 304, 366, 304, 355, 258, 355, 258, 387, 60, 387, 60, 391, \
0, 391, 0, 337, 3, 337, 3, 114, 8, 114, 8, 25, 30, 25, 30, 5, 93, 5, 98, 5, 104, 7, \
110, 10, 116, 16, 119, 20, 122, 28, 123, 32, 123, 68, 220, 68, 220, 34, 221, \
22, 223, 17, 227, 13, 231, 8, 236, 4, 242, 2, 246, 0, 260, 0, 283, 1, 300, 5, \
321, 14, 335, 22, 348, 25, 365, 29, 363, 39, 358, 48, 352, 56, 337, 70, \
344, 76, 347, 80)

floor1_rooms = [\
('101', (358, 209), (375, 246, 375, 172, 341, 172, 341, 246)), 
('Pub Lift1', (323, 223), (307, 240, 339, 240, 339, 206, 307, 206)), 
('Priv Lift1', (323, 188), (339, 205, 307, 205, 307, 171, 339, 171)), 
('110', (21.5, 363), (42, 389, 42, 337, 1, 337, 1, 389)), 
('109', (67, 363), (59, 389, 59, 385, 90, 385, 90, 337, 44, 337, 44, 389)), 
('111', (28.5, 276.5), (51, 300, 51, 253, 6, 253, 6, 300)), 
('117B', (88.5, 278.5), (98, 248, 98, 309, 79, 309, 79, 248)), 
('112', (28.5, 227.5), (51, 251, 51, 204, 6, 204, 6, 251)), 
('113', (28.5, 179.5), (6, 156, 51, 156, 51, 203, 6, 203)), 
('117A', (82, 180.5), (85, 169, 79, 169, 79, 192, 85, 192)), 
('117', (65, 235), (77, 302, 77, 168, 53, 168, 53, 302)), 
('114', (28.5, 135), (51, 155, 51, 115, 6, 115, 6, 155)), 
('115', (74, 141.5), (95, 115, 53, 115, 53, 168, 95, 168)), 
('116', (48.5, 70), (87, 113, 87, 27, 10, 27, 10, 113)), 
('118', (108.5, 102), (89, 91, 128, 91, 128, 113, 89, 113)), 
('120', (189.5, 111.5), (178, 128, 178, 132, 216, 132, 216, 91, 163, 91, 163, 112, 149, 112, 149, 128)), 
('122', (131, 207.5), (79, 193, 87, 193, 87, 169, 136, 169, 136, 192, 156, 192, 156, 169, 175, 169, 175, 246, 79, 246)), 
('121', (146, 180), (138, 169, 154, 169, 154, 191, 138, 191)), 
('106A', (112.5, 304.5), (99, 300, 126, 300, 126, 309, 99, 309)), 
('105', (124.5, 278.5), (128, 299, 128, 309, 150, 309, 150, 248, 99, 248, 99, 299)), 
('106B', (163, 304.5), (174, 309, 174, 300, 152, 300, 152, 309)), 
('104', (184, 278.5), (176, 299, 176, 309, 216, 309, 216, 248, 152, 248, 152, 299)), 
('108', (114.5, 361), (138, 385, 138, 337, 91, 337, 91, 385)), 
('107', (198, 361), (256, 337, 140, 337, 140, 385, 256, 385)), 
('Smoking', (280, 341), (300, 353, 300, 329, 260, 329, 260, 353)), 
('123', (245.5, 190.5), (314, 135, 314, 170, 306, 170, 306, 246, 177, 246, 177, 135)), 
('103', (259, 287), (217, 248, 301, 248, 301, 326, 257, 326, 257, 310, 217, 310)), 
('124', (356, 150), (396, 188, 377, 188, 377, 169, 316, 169, 316, 131, 396, 131)), 
('125', (392, 217.5), (397, 226, 407, 226, 407, 189, 377, 189, 377, 246, 397, 246)), 
('126', (436.5, 185.5), (399, 187, 409, 187, 409, 207, 474, 207, 474, 164, 399, 164)), 
('127', (436.5, 231), (409, 209, 409, 229, 399, 229, 399, 253, 486, 253, 486, 239, 474, 239, 474, 209)), 
('MShower', (488.5, 184), (501, 164, 501, 174, 495, 174, 495, 188, 490, 188, 490, 204, 476, 204, 476, 164)), 
('Closet', (502.5, 190), (497, 176, 513, 176, 513, 204, 492, 204, 492, 190, 497, 190)), 
('WShower', (494.5, 230), (476, 237, 476, 206, 513, 206, 513, 254, 488, 254, 488, 237)), 
('130', (638.5, 205), (486, 131, 558, 131, 558, 135, 724, 135, 724, 166, 697, 166, 697, 275, 553, 275, 531, 254, 515, 254, 515, 174, 503, 174, 503, 161, 486, 161)), 
('102', (367.5, 278.5), (308, 242, 339, 242, 339, 248, 342, 248, 342, 246, 397, 246, 397, 276, 393, 276, 393, 309, 300, 309, 300, 248, 308, 248)), 
('128', (441.5, 265.5), (397, 255, 486, 255, 486, 276, 397, 276)), 
('129', (535.5, 293), (510, 309, 486, 309, 486, 255, 530, 255, 552, 277, 561, 277, 561, 325, 510, 325)), 
('133', (628.5, 335), (696, 281, 740, 281, 740, 387, 642, 387, 642, 389, 561, 389, 561, 277, 696, 277)), 
('132', (771, 334), (742, 387, 742, 281, 800, 281, 800, 387)), 
('134', (749.5, 224), (800, 168, 800, 280, 699, 280, 699, 168)), 
('135', (763, 148.5), (726, 131, 726, 166, 800, 166, 800, 131)), 
('Ramona Stair', (368, 323), (340, 360, 335, 363, 331, 365, 326, 366, 304, 366, 304, 312, 396, 312, 396, 288, 400, 288, 404, 288, 409, 290, 413, 292, 418, 297, 421, 302, 422, 309, 421, 318, 417, 325, 411, 330, 405, 332, 397, 333, 344, 333, 340, 334, 336, 336, 335, 338, 332, 342, 331, 347, 332, 351, 334, 354, 336, 357, 341, 359)), 
('University Stair', (155, 77.5), (30, 23, 30, 5, 93, 5, 98, 5, 104, 7, 110, 10, 116, 16, 119, 20, 122, 28, 123, 32, 123, 68, 220, 68, 220, 87, 90, 87, 90, 23)), 
('Plaza Stair', (317.5, 28.5), (282, 37, 295, 40, 312, 49, 323, 56, 337, 70, 352, 56, 358, 48, 363, 39, 365, 29, 348, 25, 335, 22, 321, 14, 300, 5, 283, 1, 260, 0, 246, 0, 242, 2, 236, 4, 231, 8, 227, 13, 223, 17, 221, 22, 220, 34, 260, 34)), 
('Plaza Deck', (303, 81), (220, 34, 260, 34, 282, 37, 295, 40, 312, 49, 323, 56, 337, 70, 350, 83, 365, 94, 377, 100, 386, 104, 386, 128, 220, 128)), 
('106', (131.5, 318.5), (257, 336, 77, 336, 6, 336, 6, 301, 77, 301, 77, 310, 257, 310)), 
('119', (143.5, 133), (146, 110, 162, 110, 162, 91, 130, 91, 130, 115, 95, 115, 95, 128, 114, 128, 114, 151, 157, 151, 157, 153, 112, 153, 112, 130, 97, 130, 97, 168, 175, 168, 175, 131, 146, 131)) 
]
floor1_walls = [ \
(155, 191, 155, 189), 
(155, 177, 155, 169), 
(96, 129, 96, 169), 
(78, 169, 176, 169), 
(176, 247, 176, 129), 
(340, 206, 307, 206), 
(340, 187, 340, 170), 
(340, 210, 340, 201), 
(340, 247, 340, 224), 
(340, 241, 307, 241), 
(376, 246, 376, 170), 
(307, 247, 307, 170), 
(376, 170, 307, 170), 
(315, 129, 315, 170), 
(147, 129, 176, 129), 
(202, 133, 176, 133), 
(398, 129, 315, 129), 
(258, 352, 258, 387), 
(60, 387, 60, 391), 
(0, 337, 0, 391), 
(60, 391, 0, 391), 
(3, 114, 3, 337), 
(258, 387, 60, 387), 
(52, 237, 52, 273), 
(52, 189, 52, 225), 
(52, 140, 52, 177), 
(395, 306, 395, 311), 
(531, 254, 398, 254), 
(475, 178, 475, 238), 
(502, 162, 398, 162), 
(398, 129, 398, 188), 
(383, 188, 376, 188), 
(408, 188, 408, 194), 
(398, 227, 398, 254), 
(408, 227, 398, 227), 
(408, 222, 408, 227), 
(408, 206, 408, 210), 
(408, 208, 475, 208), 
(484, 278, 484, 311), 
(484, 311, 508, 311), 
(508, 327, 508, 311), 
(559, 327, 508, 327), 
(644, 391, 559, 391), 
(644, 389, 644, 391), 
(514, 205, 475, 205), 
(496, 189, 496, 187), 
(559, 129, 484, 129), 
(484, 162, 484, 129), 
(725, 133, 559, 133), 
(559, 129, 559, 133), 
(725, 149, 725, 167), 
(725, 129, 802, 129), 
(802, 389, 802, 129), 
(739, 167, 802, 167), 
(396, 188, 408, 188), 
(0, 337, 9, 337), 
(58, 337, 21, 337), 
(43, 391, 43, 337), 
(105, 337, 75, 337), 
(91, 387, 91, 337), 
(154, 337, 117, 337), 
(139, 387, 139, 337), 
(227, 337, 166, 337), 
(258, 337, 251, 337), 
(258, 328, 302, 328), 
(302, 355, 302, 311), 
(395, 311, 302, 311), 
(484, 278, 395, 278), 
(395, 294, 395, 278), 
(473, 278, 473, 275), 
(473, 256, 473, 254), 
(533, 257, 531, 254), 
(553, 276, 551, 274), 
(698, 276, 553, 276), 
(559, 391, 559, 327), 
(802, 389, 644, 389), 
(741, 314, 741, 389), 
(698, 280, 698, 167), 
(707, 280, 698, 280), 
(802, 280, 731, 280), 
(741, 280, 741, 302), 
(698, 167, 727, 167), 
(725, 137, 725, 129), 
(514, 254, 514, 175), 
(496, 175, 514, 175), 
(502, 175, 502, 162), 
(475, 166, 475, 162), 
(496, 176, 496, 175), 
(491, 189, 496, 189), 
(491, 205, 491, 189), 
(487, 238, 475, 238), 
(487, 240, 487, 238), 
(487, 252, 487, 254), 
(315, 133, 304, 133), 
(256, 133, 280, 133), 
(78, 247, 270, 247), 
(307, 247, 294, 247), 
(214, 133, 232, 133), 
(217, 247, 217, 266), 
(217, 309, 217, 291), 
(217, 309, 172, 309), 
(154, 309, 148, 309), 
(175, 300, 175, 309), 
(151, 300, 175, 300), 
(151, 247, 151, 309), 
(78, 237, 78, 265), 
(78, 286, 78, 309), 
(106, 309, 78, 309), 
(130, 309, 125, 309), 
(99, 309, 99, 247), 
(127, 299, 99, 299), 
(127, 309, 127, 299), 
(155, 191, 137, 191), 
(137, 169, 137, 191), 
(78, 171, 78, 169), 
(78, 190, 78, 218), 
(86, 192, 86, 169), 
(86, 192, 78, 192), 
(52, 301, 3, 301), 
(52, 286, 52, 301), 
(52, 252, 3, 252), 
(52, 203, 3, 203), 
(3, 156, 52, 156), 
(8, 25, 8, 114), 
(63, 114, 3, 114), 
(75, 114, 97, 114), 
(108, 114, 129, 114), 
(129, 114, 129, 89), 
(52, 114, 52, 128), 
(132, 89, 88, 89), 
(88, 25, 88, 89), 
(88, 114, 88, 89), 
(218, 89, 144, 89), 
(147, 111, 147, 129), 
(162, 111, 147, 111), 
(162, 109, 162, 111), 
(162, 96, 162, 89), 
(218, 89, 218, 94), 
(218, 89, 218, 119), 
(8, 25, 88, 25), 
(258, 337, 258, 328), 
(113, 129, 96, 129), 
(302, 355, 258, 355), 
(386, 104, 386, 129), 
(377, 100, 386, 104), 
(365, 94, 377, 100), 
(350, 83, 365, 94), 
(337, 70, 350, 83), 
(337, 70, 323, 56), 
(312, 49, 323, 56), 
(295, 40, 312, 49), 
(282, 37, 295, 40), 
(260, 34, 282, 37), 
(253, 34, 260, 34), 
(386, 128, 386, 104), 
(113, 152, 156, 152), 
(113, 152, 156, 152), 
(113, 152, 113, 129)
]


floor2_ = \
(559, 129, 484, 129, 484, 162, 398, 162, 398, 129, 315, 129, \
315, 133, 176, 133, 176, 129, 96, 129, 96, 133, 3, 133, 3, 339, 0, 339, 0, 391, \
60, 391, 60, 387, 258, 387, 258, 329, 350, 329, 350, 311, 395, 311, 395, 280, \
484, 280, 484, 311, 508, 311, 508, 327, 558, 327, 558, 391, 644, 391, 644, \
367, 802, 367, 802, 129, 725, 129, 725, 133, 559, 133, 559, 129)

floor2_rooms = [\
('238', (774, 195), (748, 188, 755, 188, 755, 205, 758, 205, 758, 222, 800, 222, 800, 168, 748, 168)), 
('237', (763, 148.5), (726, 188, 746, 188, 746, 166, 800, 166, 800, 131, 726, 131)), 
('246', (600, 264), (497, 187, 497, 204, 559, 204, 559, 324, 641, 324, 643, 324, 643, 291, 641, 291, 641, 205, 696, 205, 696, 291, 694, 291, 694, 314, 715, 314, 715, 291, 715, 205, 755, 205, 755, 190, 724, 190, 724, 187)), 
('247', (668.5, 296.5), (694, 279, 643, 279, 643, 314, 694, 314)), 
('202', (285.5, 260), (232, 250, 308, 250, 308, 242, 339, 242, 339, 246, 397, 246, 397, 255, 476, 255, 476, 250, 482, 250, 559, 250, 559, 274, 482, 274, 482, 278, 396, 278, 396, 274, 232, 274)), 
('206', (143, 267), (53, 228, 53, 338, 176, 338, 233, 338, 233, 196, 306, 196, 306, 180, 175, 180, 175, 169, 156, 169, 156, 196, 176, 196, 176, 228)), 
('212', (28.5, 307.5), (51, 277, 6, 277, 6, 338, 51, 338)), 
('245', (521.5, 300.5), (557, 276, 486, 276, 486, 309, 510, 309, 510, 325, 557, 325)), 
('244', (579.5, 357.5), (560, 389, 599, 389, 599, 326, 560, 326)), 
('243', (622, 357.5), (601, 389, 601, 326, 643, 326, 643, 389)), 
('242', (666.5, 340.5), (688, 316, 645, 316, 645, 365, 688, 365)), 
('Barbecue Deck', (780.5, 296.5), (802, 367, 759, 367, 759, 226, 802, 226)), 
('240', (736, 288), (755, 262, 755, 314, 717, 314, 717, 262)), 
('241', (722, 340.5), (755, 316, 689, 316, 689, 365, 755, 365)), 
('239', (736, 233.5), (755, 206, 717, 206, 717, 261, 755, 261)), 
('248', (669, 241.5), (695, 277, 643, 277, 643, 206, 695, 206)), 
('236', (700, 160), (676, 135, 676, 185, 724, 185, 724, 135)), 
('235', (651.5, 160), (675, 135, 635, 135, 635, 145, 628, 145, 628, 185, 675, 185)), 
('234', (606, 160), (626, 143, 633, 143, 633, 135, 572, 135, 572, 143, 579, 143, 579, 185, 626, 185)), 
('233', (552.5, 158), (557, 135, 571, 135, 571, 145, 578, 145, 578, 185, 527, 185, 527, 131, 557, 131)), 
('230', (516.5, 227), (476, 249, 557, 249, 557, 205, 476, 205)), 
('232', (500.5, 158), (476, 164, 486, 164, 486, 131, 525, 131, 525, 185, 476, 185)), 
('229', (485.5, 195), (476, 186, 495, 186, 495, 204, 476, 204)), 
('227', (436.5, 185.5), (474, 207, 409, 207, 409, 187, 399, 187, 399, 164, 474, 164)), 
('228', (436.5, 231), (399, 228, 399, 253, 474, 253, 474, 209, 409, 209, 409, 228)), 
('226', (392, 217.5), (397, 246, 397, 226, 407, 226, 407, 189, 377, 189, 377, 246)), 
('225', (356.5, 150), (377, 169, 316, 169, 316, 131, 397, 131, 397, 188, 377, 188)), 
('224', (270, 223.5), (234, 198, 306, 198, 306, 249, 234, 249)), 
('223', (292, 157), (270, 179, 306, 179, 306, 170, 314, 170, 314, 135, 270, 135)), 
('222', (244.5, 157), (268, 179, 221, 179, 221, 135, 268, 135)), 
('221', (198, 157), (177, 179, 219, 179, 219, 135, 177, 135)), 
('204', (324, 301.5), (299, 327, 349, 327, 349, 284, 341, 284, 341, 276, 299, 276)), 
('205', (265.5, 307), (234, 276, 297, 276, 297, 327, 257, 327, 257, 338, 234, 338)), 
('207', (234, 362.5), (256, 385, 256, 340, 212, 340, 212, 385)), 
('208', (187, 362.5), (210, 340, 164, 340, 164, 385, 210, 385)), 
('209', (138.5, 362.5), (115, 340, 162, 340, 162, 385, 115, 385)), 
('217', (71, 192), (89, 228, 89, 156, 53, 156, 53, 228)), 
('217A', (93, 179.5), (89, 169, 97, 169, 97, 190, 89, 190)), 
('216', (71, 145.5), (89, 156, 89, 168, 95, 168, 95, 135, 53, 135, 53, 156)), 
('215', (28.5, 157), (51, 179, 51, 135, 6, 135, 6, 179)), 
('214', (28.5, 203.5), (51, 227, 6, 227, 6, 180, 51, 180)), 
('213', (28.5, 252), (51, 275, 6, 275, 6, 229, 51, 229)), 
('210', (90.5, 362.5), (114, 340, 67, 340, 67, 385, 114, 385)), 
('211', (33, 364.5), (59, 389, 59, 385, 65, 385, 65, 340, 1, 340, 1, 389)), 
('203', (367.5, 292.5), (393, 309, 350, 309, 350, 282, 342, 282, 342, 276, 393, 276)), 
('220', (132.5, 208.5), (99, 191, 91, 191, 91, 226, 174, 226, 174, 198, 154, 198, 154, 192, 109, 192, 109, 169, 99, 169)), 
('Priv Lift2', (323, 188), (339, 205, 307, 205, 307, 171, 339, 171)), 
('Pub Lift 2', (323, 223), (307, 240, 339, 240, 339, 206, 307, 206)), 
('218', (136, 149.5), (175, 168, 97, 168, 97, 131, 175, 131)), 
('219', (132.5, 180), (154, 191, 111, 191, 111, 169, 154, 169)), 
('201', (358, 209), (375, 246, 375, 172, 341, 172, 341, 246))
]


floor2_walls = [ \
(641, 186, 678, 186), 
(757, 350, 757, 367), 
(634, 133, 634, 144), 
(634, 144, 627, 144), 
(572, 133, 572, 144), 
(572, 144, 579, 144), 
(398, 129, 398, 162), 
(174, 197, 175, 197), 
(175, 197, 175, 227), 
(757, 206, 757, 221), 
(396, 188, 408, 188), 
(727, 189, 725, 189), 
(747, 167, 802, 167), 
(747, 167, 747, 189), 
(755, 189, 739, 189), 
(769, 224, 757, 224), 
(802, 224, 802, 129), 
(802, 129, 725, 129), 
(725, 189, 725, 129), 
(725, 186, 690, 186), 
(676, 133, 676, 186), 
(627, 144, 627, 186), 
(629, 186, 593, 186), 
(579, 144, 579, 186), 
(559, 129, 559, 133), 
(725, 133, 559, 133), 
(484, 162, 484, 129), 
(559, 129, 484, 129), 
(526, 129, 526, 186), 
(540, 186, 581, 186), 
(528, 186, 523, 186), 
(511, 186, 475, 186), 
(496, 190, 496, 186), 
(496, 205, 496, 202), 
(475, 205, 527, 205), 
(558, 205, 539, 205), 
(558, 205, 558, 249), 
(558, 249, 475, 249), 
(662, 206, 642, 206), 
(695, 206, 675, 206), 
(695, 278, 642, 278), 
(642, 291, 642, 206), 
(695, 291, 695, 206), 
(716, 208, 716, 206), 
(757, 206, 716, 206), 
(757, 221, 757, 224), 
(793, 224, 802, 224), 
(757, 262, 716, 262), 
(716, 220, 716, 264), 
(716, 315, 716, 276), 
(757, 315, 703, 315), 
(757, 325, 757, 224), 
(757, 367, 644, 367), 
(689, 367, 689, 315), 
(647, 315, 644, 315), 
(659, 315, 691, 315), 
(600, 325, 600, 391), 
(627, 325, 644, 325), 
(644, 391, 644, 315), 
(615, 325, 575, 325), 
(644, 391, 558, 391), 
(563, 325, 558, 325), 
(558, 391, 558, 314), 
(558, 327, 508, 327), 
(558, 275, 484, 275), 
(558, 302, 558, 275), 
(508, 327, 508, 311), 
(484, 311, 508, 311), 
(484, 275, 484, 311), 
(475, 208, 408, 208), 
(408, 206, 408, 210), 
(408, 222, 408, 227), 
(408, 227, 398, 227), 
(398, 227, 398, 254), 
(408, 188, 408, 194), 
(383, 188, 376, 188), 
(398, 188, 398, 162), 
(398, 162, 484, 162), 
(475, 162, 475, 254), 
(398, 254, 475, 254), 
(484, 280, 395, 280), 
(395, 311, 395, 275), 
(307, 197, 293, 197), 
(278, 197, 233, 197), 
(233, 197, 233, 249), 
(307, 179, 284, 179), 
(233, 249, 278, 249), 
(269, 179, 269, 133), 
(220, 179, 220, 133), 
(155, 191, 110, 191), 
(90, 190, 98, 190), 
(98, 169, 98, 190), 
(52, 133, 52, 165), 
(52, 214, 52, 177), 
(52, 226, 52, 262), 
(52, 274, 52, 276), 
(234, 275, 234, 339), 
(226, 339, 258, 339), 
(211, 387, 211, 339), 
(214, 339, 177, 339), 
(258, 387, 60, 387), 
(3, 133, 3, 339), 
(165, 339, 129, 339), 
(117, 339, 80, 339), 
(68, 339, 59, 339), 
(0, 339, 46, 339), 
(60, 391, 0, 391), 
(0, 339, 0, 391), 
(60, 387, 60, 391), 
(258, 329, 258, 387), 
(350, 329, 258, 329), 
(395, 311, 350, 311), 
(398, 129, 315, 129), 
(176, 133, 315, 133), 
(176, 129, 96, 129), 
(3, 133, 96, 133), 
(66, 387, 66, 339), 
(115, 387, 115, 339), 
(163, 387, 163, 339), 
(234, 275, 276, 275), 
(288, 275, 309, 275), 
(298, 275, 298, 329), 
(341, 283, 350, 283), 
(321, 275, 341, 275), 
(375, 275, 395, 275), 
(315, 129, 315, 170), 
(376, 170, 307, 170), 
(307, 250, 307, 170), 
(376, 245, 376, 170), 
(340, 241, 307, 241), 
(340, 245, 340, 224), 
(340, 210, 340, 201), 
(340, 187, 340, 170), 
(340, 206, 307, 206), 
(293, 250, 307, 250), 
(271, 179, 238, 179), 
(226, 179, 195, 179), 
(176, 129, 176, 179), 
(182, 179, 176, 179), 
(174, 169, 176, 169), 
(162, 169, 90, 169), 
(96, 169, 96, 129), 
(175, 227, 90, 227), 
(90, 190, 90, 227), 
(52, 179, 3, 179), 
(52, 228, 3, 228), 
(52, 276, 3, 276), 
(155, 177, 155, 169), 
(110, 191, 110, 169), 
(155, 189, 155, 197), 
(350, 283, 350, 329), 
(162, 197, 155, 197), 
(341, 275, 341, 283)
]

floor3_ = \
(159, 129, 
96, 129, 
96, 133, 
21, 133,
21, 331,
0, 331,
0, 391,
60, 391,
60, 370,
258, 370,
258, 329,
350, 329,
350, 311,
399, 311,
399, 129, 
315, 129,
315, 133,
176, 133,
176, 129) 

floor3_rooms = [ \
('316', (79.5, 204), (89, 228, 89, 180, 70, 180, 70, 228)), 
('309', (138.5, 345.5), (115, 368, 162, 368, 162, 323, 115, 323)), 
('308', (187.5, 345.5), (164, 323, 164, 368, 211, 368, 211, 323)), 
('307', (234, 345.5), (256, 368, 212, 368, 212, 323, 256, 323)), 
('305', (270.5, 301.5), (244, 276, 297, 276, 297, 327, 260, 327, 260, 321, 244, 321)), 
('324B', (247.5, 211), (251, 219, 251, 203, 244, 203, 244, 219)), 
('324A', (247.5, 240.5), (251, 249, 244, 249, 244, 232, 251, 232)), 
('320', (200, 157), (223, 135, 223, 179, 177, 179, 177, 135)), 
('310', (90.5, 345.5), (114, 368, 114, 323, 67, 323, 67, 368)), 
('312', (45.5, 299), (23, 277, 23, 321, 68, 321, 68, 277)), 
('313', (45.5, 252), (23, 229, 68, 229, 68, 275, 23, 275)), 
('314', (45.5, 203.5), (68, 227, 23, 227, 23, 180, 68, 180)), 
('315', (59, 157), (95, 179, 95, 135, 23, 135, 23, 179)), 
('316B', (95, 215), (99, 226, 99, 204, 91, 204, 91, 226)), 
('316A', (95, 191), (91, 202, 99, 202, 99, 180, 91, 180)), 
('319', (141.5, 209), (97, 169, 109, 169, 109, 192, 154, 192, 154, 198, 174, 198, 174, 226, 101, 226, 101, 179, 97, 179)), 
('311', (29.5, 361), (65, 368, 58, 368, 58, 389, 1, 389, 1, 333, 23, 333, 23, 323, 65, 323)), 
('318', (132.5, 180), (154, 191, 111, 191, 111, 169, 154, 169)), 
('317', (136, 149.5), (175, 168, 97, 168, 97, 131, 175, 131)), 
('323', (290, 207.5), (274, 194, 274, 221, 306, 221, 306, 194)), 
('325', (290, 235.5), (306, 222, 274, 222, 274, 249, 306, 249)), 
('321', (243.5, 157), (263, 179, 224, 179, 224, 135, 263, 135)), 
('322', (293.5, 163.5), (314, 169, 306, 169, 306, 192, 273, 192, 264, 181, 264, 135, 314, 135)), 
('Pub Lift3', (323, 223), (307, 240, 339, 240, 339, 206, 307, 206)), 
('Priv Lift3', (323, 188), (339, 205, 307, 205, 307, 171, 339, 171)), 
('303', (373.5, 292.5), (350, 284, 376, 284, 376, 276, 397, 276, 397, 309, 350, 309)), 
('324', (262, 226), (272, 203, 272, 249, 252, 249, 252, 230, 244, 230, 244, 221, 252, 221, 252, 203)), 
('304', (324, 301.5), (299, 276, 299, 327, 349, 327, 349, 284, 341, 284, 341, 276)), 
('301', (358, 209), (375, 246, 375, 172, 341, 172, 341, 246)), 
('327', (387, 215.5), (397, 246, 377, 246, 377, 185, 397, 185)), 
('326', (356.5, 150), (316, 131, 316, 169, 377, 169, 377, 185, 397, 185, 397, 131)), 
('302', (319.5, 261), (308, 251, 242, 251, 242, 274, 342, 274, 342, 282, 375, 282, 375, 274, 397, 274, 397, 248, 339, 248, 339, 242, 308, 242)), 
('306', (200.5, 284.5), (70, 321, 242, 321, 242, 200, 259, 200, 259, 203, 272, 203, 272, 193, 263, 180, 242, 180, 175, 180, 175, 169, 156, 169, 156, 196, 177, 196, 177, 228, 107, 228, 70, 228, 70, 275, 107, 275, 107, 248, 160, 248, 160, 301, 107, 301, 107, 275, 70, 275))
]

 
floor3_walls = [ \
(341, 275, 341, 283), 
(162, 197, 155, 197), 
(396, 247, 399, 247), 
(399, 129, 399, 311), 
(258, 202, 243, 202), 
(350, 283, 350, 329), 
(251, 231, 243, 231), 
(243, 220, 251, 220), 
(243, 250, 243, 202), 
(155, 197, 155, 190), 
(110, 192, 110, 169), 
(155, 192, 110, 192), 
(155, 177, 155, 169), 
(176, 197, 176, 227), 
(69, 280, 69, 274), 
(21, 276, 69, 276), 
(69, 262, 69, 226), 
(21, 228, 69, 228), 
(21, 179, 75, 179), 
(69, 179, 69, 214), 
(90, 220, 90, 227), 
(90, 204, 90, 202), 
(90, 203, 100, 203), 
(90, 187, 90, 179), 
(90, 227, 176, 227), 
(100, 179, 100, 227), 
(100, 179, 87, 179), 
(96, 179, 96, 129), 
(162, 169, 96, 169), 
(173, 169, 176, 169), 
(182, 179, 176, 179), 
(176, 129, 176, 179), 
(195, 179, 226, 179), 
(224, 133, 224, 179), 
(264, 179, 264, 133), 
(238, 179, 264, 179), 
(273, 207, 273, 193), 
(273, 235, 273, 250), 
(273, 224, 273, 219), 
(273, 193, 307, 193), 
(273, 222, 307, 222), 
(273, 250, 307, 250), 
(384, 247, 376, 247), 
(340, 206, 307, 206), 
(340, 187, 340, 170), 
(340, 210, 340, 201), 
(340, 247, 340, 224), 
(340, 241, 307, 241), 
(376, 247, 376, 170), 
(307, 250, 307, 170), 
(376, 170, 307, 170), 
(315, 129, 315, 170), 
(376, 283, 366, 283), 
(376, 283, 376, 275), 
(399, 275, 376, 275), 
(341, 275, 320, 275), 
(341, 283, 350, 283), 
(298, 275, 298, 329), 
(308, 275, 298, 275), 
(243, 322, 243, 275), 
(243, 275, 284, 275), 
(258, 322, 226, 322), 
(212, 370, 212, 322), 
(214, 322, 177, 322), 
(163, 370, 163, 322), 
(165, 322, 129, 322), 
(84, 322, 117, 322), 
(71, 322, 64, 322), 
(115, 322, 115, 370), 
(66, 322, 66, 370), 
(52, 322, 21, 322), 
(21, 331, 0, 331), 
(21, 331, 21, 133), 
(96, 133, 21, 133), 
(176, 129, 96, 129), 
(315, 133, 176, 133), 
(315, 129, 399, 129), 
(399, 311, 350, 311), 
(350, 329, 258, 329), 
(258, 322, 258, 370), 
(60, 370, 258, 370), 
(60, 370, 60, 391), 
(0, 391, 0, 331), 
(60, 391, 0, 391), 
(307, 250, 307, 242), 
(273, 250, 307, 250), 
(258, 250, 243, 250)
]


##---------------------------------------------------------------------------------------------
## program


def ccord(x, fn, pic):
    return (x + pic * (2-fn))


class Room:
    def __init__(self, cvs, master, floor, name, name_x, name_y, poly):
        self.cvs = cvs
        self.master = master
        self.name = name
        key={'fill':'', 'width':0, 'tags':'element'}
        self.room_id = self.cvs.create_polygon(*poly, **key)
        self.name_id = self.cvs.create_text(name_x, name_y, text=name, tags='element')

        self.cvs.tag_bind(self.room_id, '<Enter>', self.on_enter)
        self.cvs.tag_bind(self.name_id, '<Enter>', self.on_enter)
        self.cvs.tag_bind(self.room_id, '<Leave>', self.on_leave)
        self.cvs.tag_bind(self.name_id, '<Leave>', self.on_leave)

    def on_enter(self, event):
        self.cvs.itemconfigure(self.room_id, fill=self.master.c_active)
        self.master.cvs_entry.insert(Tk.END, self.name)

    def on_leave(self, event):
        self.cvs.itemconfigure(self.room_id, fill='')
        self.master.cvs_entry.delete(0, Tk.END)

class Floor:
    
    def __init__(self, cvs, master, floor_number, floor_color, outline_color,  poly_coord, rooms, walls):
        self.cvs = cvs
        self.master = master
        self.floor_number = floor_number
        self.poly_coord = [ccord(x, self.floor_number, self.cvs.winfo_pixels('1c')) for x in poly_coord] # slide
        self.key={'fill':floor_color, 'outline':outline_color}
        self.draw_poly()
        self.rooms = rooms
        self.walls = walls

    def draw_floor(self, event):
        self.cvs.delete('element')
        self.cvs.delete(self.id)
        self.draw_poly()

        # initialize the list of Room instances and previous visited room
        self.master.room_hash = {}
        self.master.name_prev=''

        for w in self.walls:
            self.add_wall(*w)
        for r in self.rooms:
            name, (nx, ny), poly =r
            poly = [ccord(x, self.floor_number, self.cvs.winfo_pixels('1c')) for x in poly] # slide the floor
            r = Room(self.cvs, self.master, self.floor_number, name,
                     ccord(nx, self.floor_number, self.cvs.winfo_pixels('1c')),
                     ccord(ny, self.floor_number, self.cvs.winfo_pixels('1c')), poly)
            self.master.room_hash[r.name]=r.room_id

            
    def draw_poly(self):
        self.id = self.cvs.create_polygon(*self.poly_coord, **self.key)
        self.cvs.tag_bind(self.id, '<1>', self.draw_floor)
        
            
    def add_wall(self, *coord):
        key={'tags':'element'}
        coord = [ccord(x, self.floor_number, self.cvs.winfo_pixels('1c')) for x in coord]
        self.cvs.create_line(*coord, **key)

class Floor3(Floor):

    def __init__(self, cvs, master, floor_number, floor_color, outline_color,
                   poly_coord, rooms, walls ,  vault_rect, downward):
        Floor.__init__(self, cvs, master, floor_number, floor_color, outline_color,
                   poly_coord, rooms, walls)
        self.vault_rect = vault_rect
        self.downward = downward

    def draw_floor(self, event):
        Floor.draw_floor(self, event)
        x1, y1, x2, y2 = self.vault_rect
        vault = self.cvs.create_rectangle(x1, y1, x2, y2, **self.downward.key)
        self.cvs.tag_bind(vault, '<1>',  self.downward.draw_floor)

        
class Demo(A.Demo):
    """ floor """

    # colors
    bg1 =  '#a9c1da'
    outline1 = '#77889a'
    bg2 =  '#9ab0c6'
    outline2 =  '#687786'
    bg3 =  '#8ba0b3'
    outline3 = '#596673'
    c_offices =  'Black'
    c_active = '#c4d1df'
    
    def __init__(self, cmain):
        A.Demo.__init__(self, cmain, __file__)
        self.ini_frame()

    def ini_demo_called(self):
        """ This method should be defined"""
        self.ini_demo_called_0()
        self.ini_frame()


    def ini_frame(self):
        
        self.demo_main_frame.master.title("Floorplan Canvas Demonstration")
        self.demo_main_frame.master.minsize(100,100)
        self.demo_main_frame.master.geometry('+20+20')
        
        A.Label(self.demo_frame, text=
        "This window contains a canvas widget "
        "showing the floorplan of Digital Equipment Corporation's Western Research Laboratory.  "
        "It has three levels.  "
        "At any given time one of the levels is active, meaning that you can see its room structure.  "
        "To activate a level, click the left mouse button anywhere on it.  "
        "As the mouse moves over the active level, "
        "the room under the mouse lights up and its room number appears in the \"Room:\" entry.  "
        "You can also type a room number in the entry and the room will light up."
        , width=100,  wraplength='20c')

        self.room_hash=dict() # hash of rooms on the floor
        self.name_prev= ''
        fa = Tk.Frame(self.demo_frame)
        fa.pack(fill=Tk.BOTH, expand=1)
        self.cvs = Tk.Canvas(fa, width=900, height=500, scrollregion=(-100, 50,  900,  500),
                                   relief=Tk.SUNKEN, borderwidth=2)  
        self.cvs.grid(row=0, column=0, sticky= Tk.N+Tk.E+Tk.W+Tk.S)
        
        xscroll = Tk.Scrollbar(fa, orient=Tk.HORIZONTAL, command=self.cvs.xview)
        xscroll.grid(row=1, column=0, sticky=Tk.E+Tk.W)

        yscroll = Tk.Scrollbar(fa, orient=Tk.VERTICAL, command=self.cvs.yview)
        yscroll.grid(row=0, column=1, sticky=Tk.N+Tk.S)
        
        self.cvs.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        fa.grid_rowconfigure(0, weight=1, minsize=0)     
        fa.grid_columnconfigure(0, weight=1, minsize=0)  

##
        self.room_name=Tk.StringVar()
        self.cvs.create_text(600, 100, anchor=Tk.E, text='Room: ')
        self.cvs_entry=Tk.Entry(self.cvs, width=10, relief=Tk.SUNKEN, textvariable=self.room_name)
        self.cvs.create_window(600, 100, window=self.cvs_entry, anchor=Tk.W, tags='entry')
        
        floor1 = Floor(self.cvs, self, 0, self.bg1, self.outline1, floor1_, floor1_rooms, floor1_walls)
        floor2 = Floor(self.cvs, self, 1, self.bg2, self.outline2, floor2_, floor2_rooms, floor2_walls)
        floor3 = Floor3(self.cvs, self, 2, self.bg3, self.outline3,
                             floor3_, floor3_rooms, floor3_walls, (107, 248, 159, 300), floor2)
        floor3.draw_floor(0)


        self.cvs.bind('<Button2-Motion>', self.on_motion)
        self.cvs.bind('<2>', self.on_press2)
        self.cvs_entry.bind('<KeyPress-Return>', self.find_room)


    def on_press2(self, event):
        self.cvs.scan_mark(event.x, event.y)

    def on_motion(self, event):
        self.cvs.scan_dragto(event.x, event.y)

    def find_room(self, event):
        name = self.room_name.get()
        self.cvs.itemconfigure(self.room_hash[name], fill=self.c_active)
        if self.name_prev:
            self.cvs.itemconfigure(self.room_hash[self.name_prev], fill='')
        self.name_prev=name




##----------------------------------------------------------------------------
def demo(*av):
    """ function called by `index.py'"""
    d = Demo(False)
    d.demo_window.focus_set()

if __name__ == '__main__':
    d = Demo(True)
    d.demo_main_frame.mainloop()


