#!/usr/bin/python

from math import sqrt

class QuadraticLaw:
    def getTime(self, d):
        for i in xrange(int(sqrt(d)) + 1, 0, -1):
            if i + i*i <= d:
                return int(i)
        return 0


class IdentifyingWood:
    def check(self, s, t):
        last = -1
        for i in range(len(t)):
            f = False
            for j in range(last + 1, len(s)):
                if t[i] == s[j]:
                    f = True
                    last = j
                    break
            if not f:
                return 'Nope.'
        return "Yep, it's wood."


class LonglongestPathTree:
    def bfs(self, edges, s):
        if not edges[s]:
            return -1, 0
        q = [s]
        visited = {}
        lens = [0 for _ in xrange(len(edges) + 2)]
        maxv = -1
        maxl = 0
        while q:
            e = q.pop()
            for x in edges[e]:
                if x not in visited:
                    q.append(x)
                    lens[x] = lens[e] + edges[e][x]
                    if lens[x] > maxl:
                        maxl = lens[x]
                        maxv = x
                visited[e] = 1
        return maxv, maxl
    
    def longest(self, e, s):
        maxv, _ = self.bfs(e, s)
        if maxv == -1:
            return 0
        maxv, maxl = self.bfs(e, maxv)
        return maxl

    def getLength(self, a, b, l):
        e = {}
        for i in range(len(a)):
            e.setdefault(a[i], {})[b[i]] = l[i]
            e.setdefault(b[i], {})[a[i]] = l[i]

        maxx = 0
        a = list(a)
        b = list(b)
        l = list(l)

        for i in xrange(len(a)):
            del e[a[i]][b[i]]
            del e[b[i]][a[i]]
            
            x = self.longest(e, a[i]) + self.longest(e, b[i]) + l[i]
            if x > maxx:
                maxx = x

            e[a[i]][b[i]] = l[i]
            e[b[i]][a[i]] = l[i]

        return maxx






#print LonglongestPathTree().getLength((0,2,0), (1, 0, 3), (2, 4, 8))
#print LonglongestPathTree().getLength(( 0,1,0,3,0,6,7,7,8,9,11  ), ( 1,2,3,4,5,5,5,8,9,10,9   ), (100,1000,100,1000,1,10,10,10,10,100,100   ))

print LonglongestPathTree().getLength(( 
601,399,1709,498,1585,4,660,49,1274,1898,1679,146,468,1432,22,1630,1558,345,1678,993,1964,1988,1642,1214,703,1838,1340,1989,954,76,473,458,948,802,658,1546,621,1951,660,77,130,213,1359,128,1012,759,1465,1912,1130,1944,1555,625,1257,558,312,640,1473,1270,73,1027,1881,1401,466,564,1677,1921,332,1284,1527,1169,480,930,73,
858,1573,1624,1837,64,1699,725,70,1386,1314,781,1752,1051,142,810,311,186,1879,1945,1903,814,1285,630,112,1795,370,1923,358,756,21,954,45,896,1111,1018,298,371,613,135,450,693,1736,385,1751,432,10,574,1984,1464,653,464,126,672,915,618,1520,735,170,1914,849,1382,1628,1147,1618,1654,1266,1898,408,666,563,1977,231,945,1114,
1125,647,1320,48,145,1088,1238,890,671,920,1973,685,436,325,765,624,689,1310,1488,1224,1771,1183,1808,871,4,1247,1358,1587,1687,939,855,646,285,1147,244,786,470,1390,1123,314,1008,994,664,1128,1774,1533,1305,1634,1116,1081,800,284,1628,1313,504,214,1005,641,1629,177,1710,1073,413,1186,782,998,1888,876,934,810,543,1115,
303,1677,437,1929,692,22,531,536,1711,885,110,814,1649,846,1419,1204,1974,555,206,1975,257,1399,255,849,704,724,613,388,1469,1540,572,261,989,1138,632,650,974,369,159,779,1084,533,757,1090,1613,1366,1513,81,524,873,1873,1077,124,1706,439,910,130,1007,566,1032,508,273,64,687,153,1233,1153,1882,1816,1581,1590,1986,1214,478,
1265,1046,425,641,701,605,475,1194,291,792,813,139,412,108,1211,1216,319,497,945,737,856,1734,960,380,750,1124,1326,492,1054,415,1178,1685,961,521,684,1222,1692,1064,1975,327,624,1949,957,1235,1423,1989,1054,1527,289,1735,1212,332,1210,609,1602,1015,1467,1460,1378,1208,1474,241,599,1600,1682,1241,1519,1788,783,1676,221,
882,694,1765,1793,1572,779,1339,1842,1681,1891,605,39,368,1857,1159,1576,1976,1859,794,1991,659,1405,513,119,125,1863,1863,882,928,703,1691,341,1603,1725,1022,467,922,354,265,328,1780,1634,283,1493,567,1168,647,679,1162,1304,1249,1174,499,1202,703,307,29,882,412,1303,1092,1167,422,304,1140,1084,519,95,1536,756,933,205,606,
956,1219,225,566,813,672,1907,1067,949,1133,906,136,1090,511,401,209,1286,955,1105,992,1898,735,1508,381,1460,630,1013,1113,93,1384,528,1142,1430,1208,654,789,1672,1201,870,507,1486,27,1753,586,1570,458,1624,1923,42,1299,1806,1617,1474,374,1597,329,834,1473,520,678,906,1611,249,846,879,955,1621,1385,265,465,1184,1193,948,
1224,1550,317,757,1908,1957,1855,1635,53,1979,1302,1954,567,1459,1336,258,1211,1610,606,12,124,625,200,664,76,629,226,1627,166,1107,1585,218,1496,1205,802,1581,641,537,1862,1965,1713,607,1907,389,262,1289,30,1648,723,661,731,1061,1228,83,906,1171,298,572,1941,68,469,681,599,1733,1894,1301,1619,1994,1246,1720,1844,1049,
169,593,695,1074,567,1981,1990,1682,186,874,655,1942,1834,1043,197,861,943,1110,1671,1912,995,901,777,1096,669,1073,689,1821,1603,1294,755,491,609,46,1483,1020,38,1497,1139,1661,1430,1711,677,262,1216,88,1508,70,1697,677,1736,489,768,1587,652,100,221,103,1477,321,1010,768,1510,978,218,1141,924,1684,1047,695,1899,146,1131,
1156,942,1846,846,598,1129,1057,430,1418,1066,396,890,700,121,1578,1579,521,1425,1881,146,616,1013,1945,1117,270,1692,85,532,309,1952,859,86,577,98,1938,671,581,1331,254,1780,827,1278,55,1450,1488,1035,593,418,672,1086,929,1907,1274,553,395,282,1738,696,1979,1319,1442,1975,1368,953,364,746,1391,538,718,1253,529,1592,1920,
532,425,644,82,537,1259,1644,1188,336,1014,498,1348,1247,361,1648,1808,1733,1211,837,674,82,1325,535,23,111,1026,330,1211,1697,397,80,131,1472,927,848,485,622,1671,495,995,406,747,124,704,503,88,326,1067,675,962,699,130,217,1132,509,1867,607,1647,67,1677,327,685,1476,1513,278,213,1859,1591,1311,1163,123,1124,1802,1538,598,
861,626,1575,1564,844,938,1241,554,521,537,1378,729,848,289,1057,1633,1644,1247,1525,1907,1442,1024,1233,116,1303,856,1362,730,11,898,535,1627,476,283,1821,1492,540,1763,119,1110,1268,74,156,338,1124,1789,87,1446,773,1036,1020,1391,1344,1450,1164,1563,895,1692,272,157,1694,551,934,574,83,1749,106,1832,132,749,1923,1050,983,
507,95,1761,1837,1716,1993,481,484,1142,882,1968,1087,1153,395,234,1239,52,1722,448,1865,1421,1358,1925,277,1777,1843,1160,890,1738,409,1236,458,120,325,1531,1013,907,1833,203,1809,1337,512,922,1985,891,1916,1431,761,1498,440,338,1050,1296,230,1996,1959,269,1683,394,1740,1910,1809,794,1355,635,1655,443,225,1019,1753,1692,
626,1086,1501,1627,30,1067,1646,943,98,451,1964,580,521,1393,133,132,1360,1260,507,777,1295,1600,705,1059,843,905,609,1902,94,1118,1572,700,33,1704,1382,778,819,58,327,853,60,1939,1769,1897,1271,1922,336,1622,1828,946,937,1730,1006,287,1807,654,1189,631,1604,1616,541,590,237,1153,896,595,931,1623,609,1716,517,474,1039,1263,
752,460,1361,159,833,276,1069,1210,1324,1826,1893,1890,227,429,84,837,52,1817,1915,857,157,623,856,1272,358,478,605,1374,1484,1648,1377,365,272,636,1417,1287,154,260,1978,1116,1668,454,167,1487,229,1261,121,1925,701,1872,1778,1609,1953,696,1957,1791,1295,1400,1916,1513,295,1846,1051,1951,370,1666,695,169,1547,654,1724,1138,
52,434,1745,628,1429,137,67,1115,861,31,1916,1868,61,170,1363,1626,1777,949,1238,1597,989,615,1211,319,1810,930,1753,488,836,1526,1047,192,1972,1332,1695,1940,1206,1921,826,792,1861,1272,1036,209,1231,1083,760,1655,1707,1541,199,1195,52,1825,1282,1950,728,153,1041,1776,1175,129,417,1525,113,363,1404,348,832,759,80,691,
1621,1071,438,1908,1942,1613,1202,1853,1981,852,1829,1872,1168,1809,691,822,732,1473,1615,478,367,1858,355,806,1975,852,1093,1721,1362,89,1850,146,348,589,1052,767,748,359,228,1061,324,1944,968,324,1734,1480,1335,1448,1194,150,1757,219,100,157,1232,1403,915,811,1582,1402,1343,84,419,1076,1154,1274,318,356,1272,310,1789,170,
1488,819,726,1569,200,31,1794,797,1129,966,1837,1599,520,428,1432,510,1329,125,1224,469,164,152,42,773,1698,827,1518,1899,568,693,825,1104,892,521,1213,1240,403,1707,1253,448,1877,6,859,1473,597,1621,800,1105,882,386,1076,1969,1735,543,1928,1440,206,159,109,944,1795,99,1021,661,1950,305,592,285,1432,285,182,535,1557,115,
1253,78,218,981,584,102,1030,700,814,1957,316,870,1101,1075,1697,56,849,905,1260,1242,907,1743,866,995,1106,802,774,254,1436,1423,557,1669,1704,1018,1131,1414,538,144,1098,1208,1006,1960,1135,1028,494,383,89,1660,355,1633,0,824,1365,781,593,552,881,1018,880,930,421,401,1572,52,1144,200,1932,1907,1270,591,1232,1157,1686,
1354,1501,1875,1521,1968,793,516,1707,220,1591,961,1512,1284,3,1267,1467,103,1067,1162,426,1679,464,1749,1518,147,1302,1538,1778,11,408,191,1732,521,302,1441,16,1645,598,887,820,206,1834,1935,1273,1447,45,260,15,1473,728,1373,1360,1565,1750,539,1823,1277,1269,72,1689,1670,1750,952,622,1142,397,161,548,73,1263,1016,
1239,1432,1408,79,170,1218,387,784,1998,186,1773,319,1900,571,1559,979,792,454,877,1068,486,451,1622,1780,99,1566,1652,1095,1169,1380,1498,1388,1976,1656,320,1818,452,672,646,1522,566,469,360,1696,988,1759,507,1996,1,189,1477,723,220,757,130,256,429,297,60,66,1389,1850,938,1616,1342,593,568,285,1420,1300,1953,1604,600,
1803,325,1437,1698,798,849,861,1290,1297,982,852,1936,1274,1142,285,1813,1834,582,1689,73,1641,794,1327,1514,1007,609,1673,203,1005,105,1656,1239,1052,394,575,647,869,18,1215,783,1230,893,512,1445,961,602,60,321,1736,1323,479,4,1866,605,1439,620,1393,1747,1645,1066,794,909,1458,196,680,318,1716,1992,1602,1630,1007,727,
1646,1357,571,1338,455,221,570,435,1995,1666,1486,1552,912,625,470,431,846,16,1889,408,1528,1211,83,1521,971,830,367,99,1505,1201,1486,616,329,1956,687,1481,1846,65,771,306,176,331,1655,466,1134,933,303,1615,197,342,84,168,476,602,591,1409,1270,1160,1712,777,378,1586,1312,52,1634,1487,773,1565,1465,327,1226,605,1406,1025,
1187,203,588,357,1486,1357,1446,1005,334,1115,160,1120,845,993,1270,256,1374,861,1467,806,1870,1473,1984,1644,1318,1554,844,479,1814,252,1540,1523,110,422,399,146,396,1264,1206,1274,1364,1991,1255,1423,1452,73,1997,774,1742,52,1023,1777,242,1978,1443,134,1221,596,377,1995,178,841,872,925,901,1607,1766,1831,656,1182,799,
260,150,514,1744,1620,848,1605,1597,857,861,349,9,1848,274,1852,646,1282,625,1808,598,566,1264,1301,1341,1887,1538,496,1772,887,788,1222,711,1611,1316,9,685,825,796,1228,1171,1147,684,955,802,1981,1506,864,1978,1466,1663,1934,955,211,498,675,550,1815,14,1500,808,1679,1864,824,1341,1119,1071,1775,1591,1595,1820,1206,1463,
1092,324,75,1250,735,829,885,425,186,653,1825,1494,1304,599,1118,882,1135,753,522,1369,1907,66,604,1206,864,1467,13,761,1906,476,1485,1049,44,1102,546,533,13,541,1986,1407,520,190,1243,814,283,1401,1947,22,751,452,776,1963,787,1134,223,1267,300,1842,1011,625,1563,350,921,280,1370,566,1716,62,720,579,867,1473,316,162,
51,444,264,1099,373,838,1096,799,383,919,1251,1020,31,1228,126,1920,1680,754,833,1754,1349,1130,1126,1352,1725,849,1604,70,878,571,818,1075,1598,1997,224,1396,258,1959,1053,1489,1926,1899,1759,1524,218,35,188,104,1287,1767,260,1974,1244,676,24,308,1782,244,947,622,685,128,233,13,1904,829,862,1347,1539,785,1923,1581,407,
899,1556,1780,1264,1823,561,1006,625,682,1177,1283,1473,634,572,1504,760,1867,384,918,995,1768,1544,346,959,537,1655,1674,989,1702,1858,1645,1942,663,677,1975
),

(
    1539,239,1001,445,1094,200,1089,94,1957,73,1424,502,277,1381,1638,1274,1392,1647,1108,1066,1962,576,175,900,814,1886,1279,1209,985,1449,1640,1990,670,1835,485,958,1367,1082,463,556,1812,1737,792,376,1717,646,545,1085,271,967,1760,262,1833,831,1619,794,1265,1218,1914,1482,691,1700,449,1109,1386,1030,638,1708,98,1254,1237,1453,
    1863,509,1918,1263,1517,1055,562,1393,459,1321,1277,1272,1339,1991,1027,586,1541,185,1695,875,458,54,379,74,774,1686,1457,594,1252,225,649,1690,787,1114,1378,1382,1060,683,1046,1734,915,301,1715,1305,1994,1454,1379,702,1211,666,1797,214,1532,781,1293,1754,20,816,1516,1177,846,374,578,845,573,839,1807,181,1813,1179,739,1323,
    1694,214,671,1065,1274,1460,1605,1374,790,293,1234,860,1246,999,486,295,1413,1225,1715,291,146,382,1202,992,1142,600,505,686,1799,425,31,1718,650,665,1942,1275,1652,21,1937,1503,792,105,1507,466,1894,1005,449,226,1846,416,1274,563,281,1856,1425,1067,1490,1468,1930,251,1757,1685,602,1562,1658,879,797,1394,1450,21,1521,736,584,
    296,1943,294,480,1264,83,1194,1545,203,1625,1145,268,1247,1690,729,1491,733,1494,941,1559,1512,1898,895,1006,803,433,1151,1574,790,1917,727,1247,1202,757,932,762,901,938,1309,390,1922,137,812,1844,700,1871,1139,1913,1180,1397,1811,1119,123,188,1044,383,455,67,1229,677,1988,850,1107,805,970,441,328,1384,1619,950,654,1339,583,
    886,1919,745,657,1608,871,194,903,825,1054,110,897,822,1514,866,1143,62,628,1192,1199,1434,1720,452,1542,24,856,1809,1570,58,244,843,1845,1414,903,1615,1461,111,43,86,482,1097,426,980,392,742,1297,207,1509,596,1587,1688,542,975,646,1337,593,1436,1179,834,1657,1796,1822,347,353,1747,1460,1359,1483,1529,1730,44,1122,1049,110,
    811,1679,1073,226,1462,59,1660,1147,1958,687,320,857,1172,1144,149,874,1514,1291,561,414,213,904,231,635,491,1667,1250,1618,1117,1146,1982,1243,1786,298,775,602,248,387,295,380,1198,303,243,890,611,405,422,1261,1472,1411,1361,640,1956,1837,1606,1726,256,1307,402,694,16,1545,777,110,1939,91,1950,110,16,1721,884,1636,897,1311,
    509,1790,86,97,593,500,1482,212,138,1196,1058,1507,428,1190,911,1673,1596,96,648,517,1913,763,1656,549,200,488,1999,62,240,105,1153,64,1607,1811,852,1410,110,81,1023,1970,996,1871,1741,66,1444,461,1220,954,19,256,1096,543,1878,535,1462,1222,647,804,1245,1710,221,1645,101,1622,543,1165,1597,1760,708,901,150,1550,740,1426,1233,
    484,1258,642,308,1008,307,1477,1894,108,1736,158,1904,1202,238,1930,1512,1200,737,1600,691,1337,976,1670,535,1926,122,303,599,1504,1202,1436,273,1560,828,785,1774,548,741,339,688,1805,1176,1396,1780,1301,734,1602,18,200,1412,110,1336,646,543,1079,1508,1033,129,1368,1579,730,1704,1181,193,1056,1809,892,596,495,1631,1797,114,
    204,247,335,933,1775,1928,1885,1779,117,232,1609,187,674,1185,235,26,1475,1634,1033,1561,751,1650,233,619,2,1859,1735,782,906,1640,1293,520,474,212,118,1726,1382,1974,366,1048,1839,822,506,1022,213,1677,817,1971,687,1705,1749,41,342,1821,241,732,785,1634,1655,1160,946,92,815,83,1327,1901,1650,560,1883,866,1247,642,896,1462,
    1208,1370,1659,1966,1716,599,742,1558,200,44,1270,1308,1147,1983,1658,857,504,438,792,1946,1203,1173,44,1017,1161,1770,814,672,1435,1344,201,34,182,1592,892,672,1443,1798,81,36,1154,361,1147,195,1634,1346,667,1925,1592,204,530,1094,1869,1577,141,98,1703,722,1665,641,900,17,522,1026,150,1780,1515,938,905,1114,1920,892,691,1218,
    1837,1933,1496,453,1265,923,558,1372,974,717,779,518,424,834,1109,1727,645,1126,953,583,367,1771,352,1016,794,1682,673,1040,780,487,636,772,357,744,469,904,566,1351,765,1804,23,172,1218,1478,1452,66,1955,158,1618,1802,614,1569,1319,1084,1317,1376,1356,938,1020,1679,594,1628,788,867,1343,1369,1830,1280,1104,716,471,1391,316,
    1484,1273,1155,1009,958,1836,495,846,464,1019,464,1785,404,8,1045,1202,685,1131,833,1375,1592,315,1473,259,1445,1884,189,1473,515,398,971,707,1446,213,314,1155,237,835,40,362,1048,1851,541,1626,1188,712,597,1764,1554,1383,1808,764,594,1613,675,1253,667,1371,69,713,868,888,198,1004,1682,1570,955,1553,319,14,1456,189,1925,1097,
    204,289,914,290,31,57,454,799,134,1029,1081,98,1134,1020,700,1232,306,476,577,1093,561,1990,921,569,992,493,987,708,277,1911,368,303,587,1891,1359,1529,1597,326,1745,946,888,104,333,1451,1149,1283,216,1150,1852,112,540,779,780,64,1831,108,940,961,277,1952,1422,1473,1142,1895,973,1734,1535,183,1951,742,855,1615,1926,1415,951,
    267,654,332,87,25,175,1773,1333,1499,1841,1847,1571,349,1042,1328,1674,1134,166,1001,1135,497,617,936,1565,273,1867,1739,109,391,790,221,159,1091,1663,1952,1309,715,1858,691,1975,19,849,100,964,851,505,1970,684,387,1956,887,1361,107,31,1099,1082,262,1115,1363,616,1882,1792,1662,334,263,358,1929,1882,803,246,1570,1667,676,769,
    125,295,1105,1536,163,1088,1537,20,98,1418,1064,633,1135,1122,840,1697,523,1716,207,1459,793,1201,284,1512,1137,403,1304,1121,871,962,714,1681,218,231,1065,1117,264,1618,1278,1313,1081,1882,372,975,331,1465,1202,1676,511,1171,322,1502,1366,1543,797,1170,569,394,637,76,1361,1247,867,867,1393,1410,1256,358,1753,535,1202,133,1887,
    1477,621,1423,1173,1233,1274,1037,652,1391,1131,1994,1284,1404,1217,1194,881,447,1903,1148,137,1662,104,1974,182,1686,1551,395,1200,792,1660,947,737,427,1322,846,1013,773,1956,1223,108,1290,522,95,1736,1378,1335,558,146,1580,1381,1619,1486,1277,287,603,583,1228,145,511,1827,171,526,27,1780,1975,430,1215,1441,625,1315,619,90,
    654,936,1593,1660,31,428,782,706,1112,1072,1057,880,275,180,622,429,1387,1481,1664,394,1736,1377,629,302,1067,672,620,1282,403,477,340,1750,1986,942,1247,1813,486,700,489,1860,1089,1000,73,410,1519,627,86,1368,1092,1378,589,1816,182,1115,1370,819,1268,476,581,1047,255,184,27,84,719,885,1117,940,371,1404,1280,1166,303,1294,238,
    773,62,534,325,425,1643,1787,1714,1783,1329,883,106,1239,131,1370,477,751,755,1026,1748,5,253,535,277,794,1583,791,1078,1193,574,1419,695,1078,462,861,675,1746,1862,1625,1918,400,1780,1358,238,1804,1824,1496,448,705,200,284,1729,70,1316,361,1873,1801,1013,698,702,1158,1336,1569,1228,1239,1272,1808,1065,37,544,1957,214,31,1477,
    1957,1658,518,1352,1574,263,984,670,1624,43,1660,94,581,1554,701,916,1218,1565,607,1480,1153,1912,1898,335,1002,307,1663,1712,1779,670,67,1184,1534,768,1431,1293,1456,890,1924,801,1773,846,418,63,428,825,823,1537,83,1145,138,131,1800,1358,1816,1534,1427,1080,571,1380,358,1660,67,1205,71,472,1127,1692,1999,1905,1159,1756,377,934,
    1500,756,1837,1218,7,585,1567,1511,132,1758,343,1194,1762,174,766,575,1299,783,79,599,1136,1549,127,1345,1805,1484,1238,1731,496,668,1948,1981,62,1330,620,375,32,584,1023,865,1325,1658,313,1497,309,1920,1837,1470,407,1587,337,612,1702,1026,1943,491,678,178,1298,1719,1409,735,215,882,1486,151,319,1766,388,556,277,47,495,684,1924,
    1920,292,552,715,1594,155,1783,1919,1762,1908,1132,169,29,1990,667,202,428,1589,1256,140,785,999,1619,1172,842,1131,1725,598,1253,565,151,810,423,990,785,1191,1771,1295,17,97,127,1548,1455,730,926,639,1134,742,1651,73,1290,29,476,781,902,1197,791,377,814,1070,178,610,1100,1409,822,694,1281,757,507,110,412,493,411,339,1639,1634,
    1302,1116,1538,809,1816,466,864,1532,1395,1834,559,1601,1472,546,1772,922,1698,610,551,1147,1495,1816,1471,721,1980,1882,1450,991,995,30,547,1907,1239,1995,13,508,1880,1784,1451,1306,86,1942,59,814,1813,662,1227,1817,837,1236,87,1934,1996,266,1967,1943,357,1857,1031,555,1947,1881,28,973,277,1038,179,541,227,1935,874,894,1031,
    647,1718,1532,1849,1370,1379,541,1574,169,232,1359,323,250,1243,847,220,110,1081,30,86,286,143,1103,395,1693,675,222,1290,1462,29,263,1486,972,540,1063,284,770,245,1340,1990,673,375,1568,1781,1675,951,641,20,594,374,99,347,169,737,848,1736,1285,1819,813,1530,697,1937,73,833,1425,1896,165,885,442,1446,1211,210,1528,1920,1145,
    1927,744,740,173,1431,928,500,1073,1982,473,1274,1108,785,1827,1840,670,1713,108,1398,1364,1065,889,1382,1969,964,1723,232,1411,807,709,1246,906,279,309,589,758,1436,1892,1938,399,173,765,1359,1774,1260,148,1898,762,738,1352,527,1802,910,1082,110,682,1701,1359,1353,1334,986,1979,1034,606,326,292,13,434,1653,156,1591,1987,1619,
    344,605,1062,1206,1857,1052,385,1161,1089,1954,1886,1584,1874,594,1931,236,281,969,690,1428,1119,164,1557,1230,1842,1660,23,795,1930,1134,1952,783,1226,1734,83,1758,52,1236,158,1003,298,1721,351,562,1648,336,1876,1160,1152,1734,1055,446,521,1821,651,963,1588,1886,1350,562,1717,1433,675,1058,457,1867,537,821,529,393,324,1975,
    848,1099,1405,169,567,874,106,997,811,558,525,1920,765,270,765,219,108,498,483,269,1301,1370,710,622,1493,1909,602,444,1034,299,674,1276,1170,965,87,974,1612,35,206,620,1270,501,1736,772,1299,1390,856,917,369,906,592,1418,225,481,1629,1425,1879,277,958,1412,935,1597,1243,1067,839,1381,516,1378,288,1597,1168,1234,977,490,643,815,
    935,1248,612,1391,1337,608,303,208,1686,1809,1479,1022,562,110,552,986,1961,424,863,324,1309,1755,1227,45,1416,1359,145,604,1292,80,1528,1595,766,452,432,1253,1632,1032,1637,1854,403,211,1572,1285,913,50,854,310,779,1728,743,1848,908,1013,182,1658,1065,730,1280,438,1262,1636,834,1438,1779,1836,759,562,1436,1151,226,1288,1207,
    1324,70,1614,203,764,420,779,179,456
),
(
        21742,5971,18282,30977,26516,30469,18341,26522,26157,21323,1246,11020,22207,19493,18662,10359,563,24034,22939,7633,16383,3640,16815,22418,9474,28564,5803,28337,6575,28335,24627,8912,7022,7778,1163,9396,11583,30139,24154,25847,15265,13392,24494,15105,30642,24787,26177,30772,28055,5607,9467,15207,23070,4402,18103,6294,
        930,14516,11850,26839,6704,2647,30657,22160,25319,10695,7915,31208,12965,131,28440,6523,31712,9269,8223,25426,29649,30527,17574,12818,4824,14230,28061,12915,29724,28627,9996,31988,22642,32391,12815,30670,20608,10191,8222,5414,21026,25897,13202,16774,15628,26502,10597,5774,4785,32673,20538,9703,25956,24718,4253,28793,
        17085,28822,19083,24030,7487,7234,11317,18454,31031,24502,26113,28540,24807,31296,24530,27384,25572,49,21385,26743,9661,16108,28876,20888,16349,10044,28166,10408,31411,12779,10926,12753,8720,29328,18125,15502,30928,19624,21434,8546,4028,32488,552,18378,943,30930,29027,18544,26360,11911,983,32673,23040,24284,23762,9217,
        5933,32687,27531,13694,30213,17532,10082,22658,10647,29483,24937,29037,15894,31532,20260,5186,6600,710,12941,7328,1310,24236,17243,501,32293,10194,15748,15342,23325,25470,14593,19250,102,29090,11985,14927,11684,13673,20288,10996,9755,11280,3433,17250,14427,26103,1018,4125,26914,5624,5943,11751,17790,10999,30786,20462,
        8242,10170,28057,30277,15963,11515,1248,26769,14163,27068,4577,18693,3030,26075,7889,21392,14435,23270,12756,7508,18149,3888,3012,26715,9107,26405,17454,24453,14613,8410,26270,20165,6120,28137,29981,11149,11523,24443,29687,391,19387,22694,25282,6022,3812,31482,18075,24764,21817,16726,10675,3629,23806,15616,13323,21603,
        17123,10485,16763,14692,26668,18302,6393,32481,1039,15876,10520,31920,25693,25381,28111,32637,8549,13064,25468,32700,18710,24045,11048,17633,17763,9480,17421,18644,492,31119,32341,28575,5338,4626,2853,26474,28426,27147,19930,17578,22383,24502,21139,11925,13745,25634,3567,12249,28698,29064,18968,32653,24755,15325,25856,
        22120,9642,20387,17386,9265,20727,4868,8237,14710,15167,23841,4404,14721,32249,6056,30666,26760,22735,7844,11924,10788,1607,21146,9183,17412,17314,4305,16541,14563,4101,1521,16553,20407,26326,3792,24659,6956,31081,7048,792,5456,11228,18637,14257,9104,22847,9085,15696,5859,8952,19065,28198,31813,20326,25268,13096,20839,
        31685,4489,25875,29093,9554,29010,16045,20280,19887,13366,17486,19629,16008,26946,17568,19093,12407,6075,22179,15743,22821,9395,30964,24611,9395,14043,13902,21984,7768,3224,29521,20841,19531,30809,18818,5051,739,30503,5012,22354,29436,5502,3814,31644,30622,5723,13900,1198,26329,4246,14866,17206,27123,30322,14654,14512,
        8390,15219,8214,3037,5219,3183,20450,8561,15611,19944,29683,11532,7936,21657,10212,20076,17287,3151,21280,3809,4081,250,23972,21249,16586,32260,8711,5276,3057,14305,16567,30963,11769,13288,14469,5924,26320,25185,26724,745,10654,7903,24173,28546,1008,2768,6183,32496,22,30290,6150,4452,1737,19272,29745,10487,1042,11949,
        17032,13723,21351,19497,1510,23890,14102,32738,163,5278,24295,21141,4190,6968,16892,31717,30457,12548,20477,24307,13540,5957,15730,13614,22687,12814,28528,23405,26490,24057,19064,30011,17312,19994,26780,23153,13139,1590,31459,779,28025,17713,23023,25908,20312,29638,2525,31139,8094,27515,13677,23082,676,10707,25699,
        11916,1011,17349,28973,23440,22792,11629,453,10323,16724,10754,2009,19938,10119,30728,3114,9480,26638,3526,18738,26213,24794,31227,22793,12480,11876,15565,31369,18847,14830,11522,12721,19476,32011,15730,18247,14809,7777,14012,27585,8863,19374,14649,358,21924,29961,6958,20913,20868,19819,30534,12790,26193,13421,32575,
        23367,15845,27987,26339,31129,15991,18250,31546,13859,31597,6894,14846,16647,10353,16655,32079,7732,17095,26293,4008,14731,25822,25185,15378,1601,30757,28310,11927,11652,14623,28056,14586,4193,16826,6772,20389,8421,3549,19264,21219,22146,11840,10404,30799,16821,7552,32410,26765,742,27507,2673,25911,10384,12985,27160,
        2842,14497,3219,4249,1187,26916,30456,25572,16532,19485,24806,26574,251,29364,20727,6745,22117,19350,23092,25910,23375,16537,21293,18568,17373,22431,842,8939,5583,23228,14940,15029,7344,19355,1655,27772,28240,9757,31748,8920,4981,13892,17426,31593,10446,1360,25837,15644,3112,8743,30962,939,27108,18682,18337,17507,
        16041,11814,29940,4138,8534,28760,15087,14016,26939,30197,24953,12101,1160,14777,26730,27132,4869,19102,6117,28494,6404,767,27368,28690,24213,15101,2081,11019,20216,31266,15620,19378,27736,27716,12058,9782,11190,7596,14236,29890,19747,17016,7488,31230,1074,3390,8275,11480,1197,22770,3336,20868,18311,10762,18448,9153,
        7186,19167,2410,30303,22898,1879,14717,27646,17490,19393,9316,11544,31957,11008,30601,16194,2255,4076,15733,25006,20022,7669,19430,4853,4563,1290,22562,9235,20029,19641,9612,31923,30472,23191,629,29870,31802,14306,1844,26318,8702,23141,19321,24791,157,29852,1502,5320,16553,4377,18879,28510,26492,32038,22348,30682,
        18401,18092,12764,23812,27408,20819,28805,21360,1504,18155,31977,10496,20024,26379,13394,12714,17606,31223,7938,29051,18164,27335,12740,10204,32024,19654,19911,8213,30955,20505,29356,27407,6205,27041,22238,26206,32743,12834,23074,13438,17152,16548,1647,2653,2644,1049,4863,30234,20497,24641,7590,781,964,4555,3683,
        24327,10884,7613,22837,25819,20333,20501,4655,12317,22609,3504,1999,7721,4777,32108,22412,24679,3282,19594,12462,974,3958,4694,14690,4519,19272,5897,18958,11668,3828,494,29410,21712,6485,12996,32688,8888,23529,19044,28157,16011,16771,9891,2392,22126,19776,21882,8682,19379,9660,17252,4431,29786,24710,10504,420,5592,
        8657,31768,10977,32024,25708,26489,31337,22464,32244,3748,22752,12981,13128,8268,573,16865,28989,31809,9248,21812,32147,28820,13925,7912,13352,20988,16889,12042,9324,29560,2540,18486,8981,16694,19144,29090,9236,692,1058,27229,28871,2085,110,25049,3696,18198,3864,6568,26854,10833,9424,21635,5514,6401,22053,13968,17021,
        31000,24661,31461,9744,12526,13411,8776,636,27690,14443,32568,4564,10214,13107,17202,28215,18958,5634,28973,19018,18441,6325,22887,3557,8348,23567,611,11021,11531,1617,9010,16163,3457,3594,4851,21594,13489,10033,20886,22383,22206,1649,3557,5524,16216,28356,19652,22189,21289,15683,5559,26558,16495,26429,18598,10660,
        8938,7814,221,30724,7928,4113,10583,31874,14335,28865,9788,16947,26123,19581,14248,7508,11960,19331,31150,15164,17747,25086,9629,28303,30268,7642,30849,2997,24974,1751,25325,27018,18690,17628,26104,23127,29969,143,16774,12546,30041,12834,22473,9857,16450,21103,27143,13204,30177,8776,4765,12980,18973,31752,8260,24134,
        23056,25454,13971,32533,28848,18348,22469,24319,32430,11194,15293,21487,18846,10480,6215,30475,5721,32724,16033,23598,21151,11057,12858,23960,513,10601,7353,20452,29182,28683,17217,12859,31085,15784,24819,11976,18203,15843,2741,32619,948,13256,50,2738,19175,7775,3618,19717,16325,2944,26060,25120,16490,3304,3529,17095,
        31968,909,20490,2740,30016,13615,18717,23253,8986,24624,31915,11188,21015,16805,4934,9271,27613,16813,9569,18569,15155,14850,14240,5464,27238,2765,19539,23361,16619,29119,11837,28296,25669,22365,22681,32525,8234,1691,8287,11387,31201,685,707,10947,4846,28442,15614,2761,7921,15890,4434,31580,28876,6401,23880,5740,25348,
        14180,25917,3703,8042,6108,31004,20549,2554,20352,22125,27861,21251,25464,27535,24471,29832,24776,24641,1244,7910,9833,1896,21642,22712,5534,7692,13588,22008,7301,31651,31401,19047,20204,6034,26284,15150,359,2033,15205,5061,6815,23950,14326,532,3821,309,4240,24024,14888,30255,14054,8009,3003,9737,1762,10490,14586,6551,
        11159,26880,27062,17207,20600,5462,4878,15962,29383,1920,29833,10305,26448,31599,27490,30213,26710,13733,4131,27610,16334,21657,21109,6548,25035,20829,1847,107,2874,29566,7373,17915,14543,15404,27067,6287,2623,3226,18802,10398,26032,2984,31593,23446,28525,3776,30832,7129,10719,2557,12866,27141,20921,19347,29017,4985,
        19058,1643,17670,12821,12024,28685,14784,22848,23203,30147,18877,5168,32359,19707,15295,6502,5711,25326,25649,22391,21286,28543,31858,16146,19575,12134,1137,28223,3769,2445,25210,8421,22979,9146,13647,2703,9094,10863,3195,32111,13050,20495,31459,676,26457,18241,14238,18360,32652,15513,16646,1389,30178,4982,13839,17337,
        17416,27174,23000,7951,9014,10577,30080,29408,7334,8852,3131,3426,32330,620,5541,20624,1982,6486,12886,25714,25468,16436,3766,24222,16463,23539,26642,767,7946,17515,26608,469,10361,4742,18848,22269,8088,6565,32276,11891,17411,4159,16882,29205,14510,11211,23014,25769,17110,13281,26941,28194,30007,20636,5808,32031,7040,
        6210,29565,8629,31236,8231,22717,17774,13746,5326,12017,9361,30791,7506,21470,27812,9410,3588,4763,9264,12312,11862,25064,16324,29226,5624,23745,2108,756,25920,10547,13891,30727,23759,16751,26391,5689,6258,21277,20109,19355,28998,10482,19028,1451,19232,21125,14973,14283,20779,32350,17211,9714,26067,14928,23528,18338,
        18914,3594,20297,22298,16105,9192,4371,24780,10466,29711,3246,26385,29459,9656,20792,28188,15414,6860,16077,1068,3542,22962,6406,6662,8956,18788,8895,16291,523,29641,10014,6438,28137,16959,5073,8209,29279,26742,2198,1207,4035,29061,1,17397,18900,9015,30074,17693,7653,11174,11397,5171,9278,19724,32070,3164,24767,31701,
        19012,1683,1734,8953,877,24734,13395,648,23130,28736,26730,23687,3029,14001,14521,25594,25240,26699,2683,8770,22360,7302,21148,18089,29186,14886,8478,5180,20549,29619,31675,25049,30032,26666,19404,24712,18141,15346,25449,7182,23406,15889,24018,27072,32214,28064,24333,14742,2556,29564,30417,32128,1756,25663,10915,6909,
        8654,24175,27455,6889,28427,22773,31033,2966,4973,13776,31972,18719,15222,27914,21875,8185,916,25579,25438,32203,13731,17518,21000,9344,32692,26865,9374,5018,2061,12336,2626,7113,625,19828,15721,20668,10913,26888,29313,19767,18466,9453,6616,32102,8001,22990,30905,25457,29525,8246,24024,2640,32324,31233,29935,6881,328,
        12305,32170,18231,21235,14402,27073,53,3697,14239,9827,10588,18446,29910,5339,16098,27383,20201,30318,8708,9285,3111,20354,32669,32567,5467,1542,1270,5823,28995,16141,22240,65,5187,16316,32512,21399,22619,21863,17259,29784,12631,2295,7283,90,28997,8591,15552,1909,12588,14959,24482,28810,12795,28696,20901,12228,18880,
        26800,26470,12830,12570,15273,22182,8742,17649,31902,9629,27136,4196,28029,9360,5805,13059,7147,9638,142,30527,28132,26360,23843,11550,24994,25319,7705,7476,1217,31410,16772,10190,26272,12104,30569,25712,2570,23642,16511,21890,6678,10677,27190,1094,26187,9935,3065,6413,27144,17567,27056,17323,25379,8626,24458,2088,
        15313,23676,15097,17336,19398,24556,9470,32237,13469,24131,422,23084,23929,28197,26837,15710,20973,32240,7234,31719,2073,4430,7875,9180,21014,32006,20683,14192,32405,5400,13872,27568,27842,264,18738,16241,5999,10874,32442,32390,23406,31231,24543,1334,32062,22063,23726,22509,12779,6392,15403,25393,12079,28469,19859,
        30680,1757,22146,16100,22392,20863,11599,15519,25888,27710,2356,16077,20037,19971,18308,10048,16383,14300,3109,5403,31862,17569,8863,4501,25750,7127,30066,31225,18955,19412,4013,19185,7529,3876,23740,12549,19626,300,6786,607,26078,1549,12712,1489,21022,27084,26676,11033,15554,31407,8797,6243,31444,8938,9629,12559,1732,
        17786,4617,31157,25692,25170,1502,32102,247,17845,8028,6197,25582,18147,20695,19190,17236,23031,15115,31814,20707,30992,432,19148,21301,10415,20046,21694,24376,7008,30035,6310,17884,14493,29027,21350,2574,2799,10479,32633,29418,22870,12809,22909,3628,28651,2166,3566,14056,23492,27141,29749,29820,7704,19744,31457,17858,
        6819,9633,10548,11402,17740,27623,23009,3399,21254,6696,4884,14088,29172,5128,8115,10154,19664,11371,19939,24652,23949,15752,30415,24068,21307,1856,13221,2768,3884,18349,25568))
