# PDF Export

## Page 1

EWR Cotton Client Interface Manual
Files Received From EWR
Updated: 08/20/2025
©Copyright 1996-2025, EWR, Inc.

## Page 2

SECTION 1 Table of Contents
SECTION 2 OVERVIEW ............................................................................................ 2-1
SECTION 3 FILE TYPE HD (DETAIL FILES) ........................................................ 3-1
HD –Default Delivery of Detail Data Information (Non-Block) ............................................................... 3-1
HD07 - Cancel Receipts Delivery File .................................................................................................... 3-10
HD13 - Warehouse Bale Relocation File ............................................................................................... 3-12
HD21, 30, 31 - Shipping Orders Instructions & Receipts ...................................................................... 3-14
HD23 - Shipping Order Update ............................................................................................................. 3-17
HD24 - Warehouse Invoice ................................................................................................................... 3-19
HD25 – Phytosanitary Warehouse XML Delivery ................................................................................. 3-22
HD25 – Phytosanitary Forwarder XML Delivery ................................................................................... 3-24
HD- Delivery of Block Receipt Detail Data Information ....................................................................... 3-26
HD43 - Warehouse Loan Status Delivery ............................................................................................. 3-30
HD57 -Delivery Receipts via CMA Loan Redemption ........................................................................... 3-31
HD64 - Warehouse Profile Requested ................................................................................................. 3-33
HD66 - Delivery of Reconciliation Detail .............................................................................................. 3-36
HD67 - EWR ASCII Text Message Received from EWR ......................................................................... 3-39
HD68 - Holder Information Requested ................................................................................................ 3-40
HD86 - Shipping Order Release Request (Received by Banks Only) .................................................... 3-42
HD87 - Bank Draft (Inbound only) (Received by Banks Only) .............................................................. 3-44
HD91 - Bank Draft (Outbound Only) (Received by Banks Only) ....................................................... 3-45
HD92 - Collateral Release Request (Received by Banks Only) ............................................................. 3-46
HD97 – Batch 23 Compliance Detail ..................................................................................................... 3-48
HD98 - Delivery of Custom Report Detail ............................................................................................. 3-50
ii

## Page 3

SECTION 4 FILE TYPE HA (SUCCESSFUL ACKNOWLEDGEMENT FILES) .. 4-1
HA – Default Successful Acknowledgments ........................................................................................... 4-2
HA18 – BMAS Receipted and Non-Receipted Bales Acknowledgment .................................................. 4-4
HA25/26 – Phytosanitary Holder Acknowledgment .............................................................................. 4-6
HA81 - Collateral Holder Acknowledgment ........................................................................................... 4-8
SECTION 5 FILE TYPE HE (ERROR ACKNOWLEDGEMENT FILES) ............. 5-1
SECTION 6 FILE TYPE HS (SUMMARY FILES) ................................................... 6-1
HS78 - Block Receipt Summary .............................................................................................................. 6-1
HS82 - Receipts Held Summary .............................................................................................................. 6-3
HS83 - Summary of Receipts Issued (Received by Warehouse Users Only) ....................................... 6-5
HS89 - Bank Collateral Summaries (Banks Only) .................................................................................... 6-7
iii

## Page 4

SECTION 2 OVERVIEW
The following document provides detailed information of files created by the EWR, Inc. host computer.
These files will be located on the EWR, Inc. FTP site.
On the FTP site the files may be located under 1 of 2 main directories called:
• Download
• OldMail
Under both of those directories are 2 more directories, called:
• NotZip
• Zip
The NOTZIP directory will contain uncompressed files, with the extension DAT or XML.
The ZIP directory will contain compressed files (PKZIP) with a ZIP extension. That file will contain a single
non-compressed file of DAT or XML.
File names follow this pattern:
HSBB.NNNN.YYYYMMDD.HHMMSS.UUUUUU.dat or .zip, where:
H H holder
S Type of file: D=detail, A=Acknowledgment, E=Error, S=Summary
BB 2-digit batch type
NNNN Batch number
YYYYMMDDD Date
HHMMSS Time
UUUUUU Unique number
Example:
HD21.0333.20020515.152019.041254.DAT for uncompressed
HD21.0333.20020515.152019.041254.ZIP for compressed (zip)
The files can be retrieved by user for a specific holder. The holder has a single FTP password. After the
file is successfully downloaded from the DOWNLOAD directory, it will be moved to the OLDMAIL
directory. After a period of days (normally 21), the file(s) will be deleted from the EWR, Inc. FTP site.
2-1

## Page 5

SECTION 3 FILE TYPE HD (DETAIL FILES)
HD –Default Delivery of Detail Data Information (Non-Block)
This file is the default or standard delivery file created from several batch types: (01, 02, 03, 04, 06, 08,
22, 32, 35, 38, 39, 42, 44, 45, 50, 51, 52, 54, 56, 60, 62, 65; and 63).
This batch is a download of detailed receipt information contained in the host computer. It is produced
when users send to the host, batch type that is delivering receipts or updating receipts (in certain cases).
Normally, the recipient of the batch will be the entity who is the current holder or subholder of the
receipts.
This file can be in 2 formats: Long or Short. The default is the Long format unless the holder has
contacted EWR, Inc. support staff and requested that EWR send short records. This setting is saved in
the holder profile. A Short record download will contain receipt information only, required data and
optional data. A Long record download will contain the classing data.
HD54 is received when CCC updates the bale information.
HD56 is received when CCC releases a bale from loan.
Note: In January 2014, a certificated issue batch (Type 02) will have the tenderable field changed to
allow for 3 options:
• Blank = Tenderable
• NT = Non Tenderable
• SD = Tenderable with Smith Doxey classing
3-1

## Page 6

Default Detail Delivery File Layout
Short Record Size = 271 Long Record Size = 345
HEADER LAYOUT
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID AN 7 2-8 Holder ID – Person/Company making
request
3 Batch Number N 4 9-12 Batch number , holder supplied
4 Batch Type N 2 13-14 Originating batch type
5 Request A 1 15 Single character
Flag/Action If field 4 is batch type 65 then the
Code following table applies:
A All Receipts
C Crop Year
D Draft Number
G Gin Code
I Invoice Number
L Loan Number
O Purchase Order Number
P Previous Holder ID
R Grower Reference Number
S Subholder
T EWR Container ID
W Warehouse Code
Z Shipping Order Number
If field 4 is batch type 03 or 04:
U=Warehouse is updating Locator ID
If field 4 is 34,35,38: C=Container created
D=Container Dissolved
If field 4 is 62 or 63: U=Holder is updating
warehouse fields on receipt
If field 4 is 50 and Field 18 is “C”, then the
field is the “Certificated Type” that
entered on the batch 50 header field.
3-2

## Page 7

6 Request Field AN 11 16-26 Text comment regarding the batch
/ Activity Field or
If field 4 is 34,35,38 then the field is the
EWR Container ID processed in the batch
if field 4 is batch type 65 the following
table applies:
Draft Number AN 10
Gin Code N 5
Invoice Number AN 10
Loan Number N 5
Purchase Order AN 10
Previous Holder AN 7
Grower Reference N 11
Subholder AN 7
Warehouse Code N 6
S/O Number AN 10
EWR Container ID N 8
7 Holder A 1 27 Empty unless batch type 65 Then the
Selection following rules applie
Holder Selection
S=detail data for receipts which the
Holder ID is designated as the subholder;
B=detail data for receipts which the
Holder ID is designated as either the
current holder or subholder;
Blank = detail data for receipts which
Holder ID is designated as the current
holder.
8 Batch Date N 8 28-35 Holder supplied batch date; MMDDYYYY
9 Batch Time N 6 36-41 Holder supplied batch time; HHMMSS
10 Draft Number AN 10 42-51 Bank Draft Number - if delivered via bank
draft, otherwise zero or empty.
11 Draft Amount N 10 52-61 Draft Amount - if delivered via bank draft,
otherwise zero or empty.
12 Long/Short A 1 62 N = Short Record (no classing data)
Record default;
Y = Long Record (with classing data)
13 From Holder AN 7 63-69
14 Holder Type A 15 70-84 Output of holder selection type; i.e.,
Holder; Subholder; Both. This is only filled
on batch types 65 and 60.
15 Holder Name A 40 85-124 Name of the holder on file with EWR.
16 Criteria Type A 15 125-139 This is only applicable to batch types 60
and 65.
3-3

## Page 8

17 Criteria Name A 40 140-179 Criteria description. This is only applicable
to batch types 60 and 65
18 Certificated A 1 180 Blank = Regular Batch
Batch C = Certificated Batch
19 Block Receipts A 1 181 Blank = No
N = No
Y = Yes
20 Detail Source A 1 182 If field 4 is 62 or 63: U=Holder is updating
warehouse fields on receipt and receiver
is NOT the holder of receipts
21 Transaction ID N 9 183-191 Reserved for EWR use.
22 Receipt Count A 6 192-197
23 Filler A 74/14 198- Short Record – 74; Long Record – 148
8 271/345 Reserved for EWR, Inc. use
3-4

## Page 9

DETAIL LAYOUT
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Warehouse N 6 2-7 Warehouse code of the receipt
3 Electronic N 7 8-14 Electronic Receipt Number
Receipt Number
4 Crop Year N 4 15-18 Crop year of the receipt
5 Issue Date N 8 19-26 Date entered by the warehouse, not
assigned by EWR – Storage date of the bale
– MMDDYYYY
6 Tare Weight N 2 27-28 Represents pounds subtracted from gross
weight to compensate for bagging and ties
on the bale
7 Net Weight N 3 29-31 Gross weight of bale minus tare weight –
User enters appropriate amount
8 Bagging/Ties A 2 32-33 Bagging in 32 / Ties in 33
9 Bagging A 1 34 Bag condition – User defined. Examples
Condition are:
A = Bale is completely covered
B = Bale may have minor tears and an
exposed sample opening
C = Exposed cotton in addition to sample
opening
10 Compression A 1 35 Compression Code, valid entries are 1-7:
Code 1 = Flat
2 = Modified Flat
3 = Standard Density
4 = Gin Standard
5 = Gin Universal Density
6 = Warehouse Universal Density
7 = Gin Universal Density (1995)
11 Receiving Fee N 4 36-39 9999 (2 decimal); Warehouse defined
charge, example 0250-$2.50 (US currency)
12 Storage Fee N 4 40-43 9999 (2 decimal); Warehouse defined
charge, example 0250-$2.50 – If Storage
Charge Frequency is Daily, the entry will
display as cents/day.
e.g., 0950=$9.50 per day(US currency)
13 Storage Charge A 1 44 D=Daily; C=Calendar Months; S=Actual
Frequency Months (same day); F=Actual Months
(following day); M=Monthly (legacy
support)
See Appendix J – Files Sent To EWR
14 Receiving Paid A 1 45 Y=receiving paid or waived
N = not paid or waived
3-5

## Page 10

15 Loading Paid A 1 46 Y= Paid; N=Not paid or waived
16 Classing Paid A 1 47 Y = Paid; N = Not Paid
17 Compression A 1 48 Y = Paid; N = Not Paid
Paid
18 Reconcentrated A 1 49 R = Bale is reconcentrated
Space = Not reconcentrated
19 Previous N 6 50-55 Code of previous warehouse - Entered only
Warehouse if the bale is reconcentrated
20 Previous Receipt N 7 56-62 Warehouse receipt number from previous
Number warehouse, entered for reconcentrated
cotton only.
21 Gin Code N 5 63-67 USDA assigned code which identifies the
Number site where the cotton was ginned
22 Gin Tag Number N 7 68-74 Sequential tag number assigned by the gin
23 Storage Paid N 8 75-82 Storage paid through date; MMDDYYYY.
Through Last date that storage charges against the
bale were paid to the warehouse
24 State Code AN 2 83-84 USDA assigned State Code
25 County Code N 3 85-87 USDA assigned County Code
26 Farm Number N 5 88-92 Farm Serial number used for identifying
specific areas of production
27 Loan Number N 5 93-97 FSA/CCC assigned Loan Number
28 CCC Loan Type A 1 98 A = Form A; G = Form G; Blank = no loan
29 CCC Loan Date N 8 99-106 Loan Date. This field is initially supplied by
the sender of the loan batch. Later it is
updated by CCC when the loan is accepted,
rejected or updated by CCC.
30 Mark AN 8 107-114 If the receipt is under shipment, then this
field is the shipper mark. Otherwise it is
the mark from the batch header upload.
31 Purchase Order AN 10 115-124 Purchase Order Number assigned by seller
Number
32 Invoice Number AN 10 125-134 Invoice Number assigned by seller
33 Grower N 11 135-145
Reference
Number
34 Grower AN 9 146-154 Optional field on non-world cotton
ID/Container ID EWR Container ID if receipt part of a world
container lot
35 Received From AN 30 155-184 Received from name
3-6

## Page 11

36 Licensing A 2 185-186 US = USA Federal Licensing
Authority NL = Not Licensed
US Postal State Code = State Licensing
IC = ICE Licensed (World)
37 Locator ID AN 8 187-194 Warehouse bale location
38 Electronic A 1 195 O=Open; C=Cancel; D=Deactivated; V=Void
Receipt Status
39 Electronic A 1 196 E = Electronic
Receipt Flag P = Paper
40 Receipt Type A 1 197 R = USA Regular
C = Certificated #2 (USA)
D = USA Decertificated
G = Block Negotiable
O = Block Non-Negotiable
T = World Container
W = World Certificated
X = World Decertificated
41 Paper Receipt N 7 198-204 Paper number assigned by warehouse (if
Number any)
42 Producer Name AN 34 205-238 Producer Name (May be truncated) on
/ world cotton. On world cotton the first 12
World Gin Tag characters will be the world gin tag
43 EAD Eligible A 1 239 Y = Yes
N = No or Blank
44 Gin Charges N 4 240-243 Used to enter gin fees when applicable
45 User Defined AN 12 244-255
Field
46 Warehouse A 1 256 Y = Warehouse & Producer are the same
Depositor entity
N = Warehouse & Producer not the same
47 Graded Deposit A 1 257 Y = Graded at the request of the depositor;
N = No or Blank
48 EAD Subholder A 1 258 Y = Yes
N = No or blank
49 CCC Document N 8 259-266 This date is supplied by CCC and is in
Received Date reference to a loan document type
50 Current Holder A 1 267 M = Merchant
Type W = Warehouse
G = Gin
Z = Coop
P = Producer
C = Government
B = Bank
51 Loan Transfer A 1 268 Y = Yes. This bale was transferred while
under loan.
3-7

## Page 12

52 CCC Storage A 1 269 Does the 75-day storage limit apply?
Limitation
53 Is Stored Outside A 1 270 Y=Yes Issue Date is date moved outside;
N=No, Bale is inside;
Blank=unknown
54 EWR Definition A 1 271 Reference to the EWR Definition for a
ID cotton receipt.
55 Type Class A 1 272 A = AMS Smith-Doxey; O = Other Classing;
N = No Class available; C = Certified
56 Date Class N 8 273-280 Classing office assigned – Date Classed.
57 Delivery Point N 2 281-282 World Cotton Only
58 Classing Point N 2 283-284 Assigned by EWR, Inc.
59 Origination Code A 3 285-287 Country 3 letter ISO code where cotton
was grown
60 Filler A 1 288
61 Color Grade N 2 289-290 Classing office assigned
62 Staple N 2 291-292 Classing office assigned
63 Micronaire N 2 293-294 Classing office assigned
64 Strength N 3 295-297 Classing office assigned
65 World A 1 298 T = Tenderable
Tenderable N = Non-Tenderable
66 Leaf Grade N 1 299 Classing office assigned
67 Extraneous N 2 300-301 Classing office assigned
Matter
68 Remarks N 2 302-303 Classing office assigned
69 HVI Color N 2 304-305 Classing office assigned
70 Color Quadrant N 1 306 Classing office assigned
71 HVI RD AN 3 307-309 Classing office assigned
72 HVI + B AN 3 310-312 Classing office assigned
73 Trash % N 2 313-314 Classing office assigned
74 Length N 3 315-317 Classing office assigned
75 Uniformity N 3 318-320
76 Upland/Pima A 1 321 Growth type; 1 = Upland; 2 = Pima
77 Classing Type N 1 322 Reserved for EWR, Inc.
78 Filler N 5 323-327 Reserved for EWR, Inc.
79 Lot Number N 6 328-333 Lot number assigned by ICE
80 Weight Date N 8 334-341 Weight date assigned by Warehouse;
MMDDYYYY
81 USDA Tenderable AN 2 342-343 Is cert receipt tenderable on provider
system? Blank=Tenderable, NT=Non-
Tenderable, SD=Tenderable w Smith-Doxey
classing
3-8

## Page 13

82 Rain Grown AN 1 344 R = Rain grown
N = Not rain grown
U = Unknown
83 Trust Protocol A 1 345 Data provided by US Cotton Trust Protocol
Flag
TRAILER LAYOUT
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T = Trailer Record
2 Holder ID AN 7 2-8 The same as entered in the header record
3 Batch Number N 4 9-12 The same as entered in the header record
4 Record Count N 9 13-21 Control total record count of the number of
detail records in the batch
5 Filler A 9 22-30 Reserved for EWR, Inc. use
6 Hash Total N 15 31-45 Electronic Receipt number hash total
7 Filler A 226 46- Blank 226 = short; 300 = long
- 271-345 Reserved for EWR, Inc. use
300
3-9

## Page 14

HD07 - Cancel Receipts Delivery File
Batch Type 07 is a listing of receipts cancelled by a warehouse and sent to the current subholder of the
receipts.
This is created when the warehouse sends up 07 or 36 to cancel receipts and they may include
container/seal and Shipper Order Number/Mark.
HEADER LAYOUT FOR HD07 Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H = Header Record
2 Holder ID AN 7 2-8 Holder
3 Batch Number N 4 9-12 Batch number , holder supplied
4 Type N 2 13-14 07=Cancel receipts
5 Filler A 1 15 Reserved for EWR, Inc. use
6 Request Field AN 10 16-26 The word “CONTAINER”
7 Filler A 1 27 Reserved for EWR, Inc. use
8 Date N 8 28-35 Date created
9 Time N 6 36-41 Time created
10 Filler A 21 42-62 Reserved for EWR, Inc. use
11 From Holder AN 7 63-69 Blank
12 From Name A 33 70-102 Blank
13 Receipt Count A 6 103-108 Blank
14 Filler A 2 109-110 Reserved for EWR, Inc. use
15 Transaction ID N 9 111-119 Reserved for EWR, Inc. use
16 Filler A 1 120 Reserved for EWR, Inc. use
3-10

## Page 15

DETAIL LAYOUT FOR HD07
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Warehouse N 6 2-7 Warehouse code of the receipt
Code
3 Electronic N 7 8-14 Electronic receipt number
Receipt
Number
4 Crop Year N 4 15-18 Crop year of the receipt
5 Mark A 8 19-26 Shipper Mark
6 Order Number A 10 27-36 Shipper’s order number (Note 1)
7 Container A 25 37-61
8 Seal A 25 62-86
9 Requested N 8 87-94 Optional – Supplied by Warehouse (Note 1)
Load Date
10 Filler N 8 95-102 Optional – Supplied by Warehouse (Note 1)
11 Shipped Date N 8 103-110 Optional – Supplied by Warehouse (Note 1)
12 Filler A 10 111-120 Reserved for EWR, Inc. use
TRAILER LAYOUT FOR HD07
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T = Trailer record
2 Holder ID AN 7 2-8
3 Batch Number N 4 9-12
4 Record Count N 9 13-21 Control total record count of the number of detail
records in the batch
5 Filler A 9 22-30 Reserved for EWR, Inc. use
6 Hash Total N 15 31-45 Electronic Receipt number hash total
7 Filler A 74 46-120 Reserved for EWR, Inc use
3-11

## Page 16

HD13 - Warehouse Bale Relocation File
This batch is a download of receipt information that has been relocated in the warehouse. It is
produced when warehouses send Batch Type 13 to the host computer. The recipient of the batch will
be the current holder or subholder of the receipt when the change was made.
HEADER LAYOUT FOR HD13 Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H = Header Record
2 Holder ID AN 7 2-8 Holder ID who sent the batch.
3 Batch Number N 4 9-12 Batch number, holder supplied
4 Batch Type N 2 13-14 13
5 Activity AN 11 15-25
6 Action Code AN 1 26
7 Filler A 1 27 Reserved for EWR, Inc. use
8 Batch Date N 8 28-35 Date batch was created / updated; MMDDYYYY
9 Batch Time N 6 36-41 Holder supplied batch time; HHMMSS
10 Filler AN 61 42-102 Reserved for EWR, Inc. use
11 Receipt Count N 6 103- Number of receipts in file
108
12 Filler AN 12 80-120 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD13
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Warehouse N 6 2-7 Warehouse code of the receipt
3 Electronic Receipt N 7 8-14 Receipt Number
Number
4 Crop Year N 4 15-18 Crop year of the receipt
5 Locator ID A 8 19-26 Used to identify exact location of a bale in a
warehouse
6 Is Stored Outside N 1 27 Is receipt stored outside – Y/N
7 Stored Inside Date N 8 28-35 Date moved inside
8 Stored Outside N 8 36-43 Date moved outside
Date
9 Filler A 77 44-120 Reserved for EWR, Inc. use
3-12

## Page 17

TRAILER LAYOUT FOR HD13
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer
2 Holder ID AN 7 2-8 Holder ID who sent the batch
3 Batch Number N 4 9-12 Batch number
4 Record Count N 9 13-21 Number of receipts
5 Filler A 9 22-30 Reserved for EWR, Inc. use
6 Filler A 15 31-45 Reserved for EWR, Inc. use
7 Filler A 75 46-120 Reserved for EWR, Inc. use
3-13

## Page 18

HD21, 30, 31 - Shipping Orders Instructions & Receipts
Batch Type 21, 30 and 31 received from the host, is a batch which contains a shipping, staging or sample
order instructions and a list of warehouse receipts on an order. This detail file is different than the full
detail data downloads of receipt information generated by most batch types, this file contains only the
warehouse number, receipt number, crop year, and net weight (if entered by the shipper.)
On shipping orders a bank lien will be downloaded at the beginning of the instruction list if the bales
being shipped are held as collateral by a bank.
There are some in the industry that are using the “Text Line” field to deliver special instructions to the
warehouse. The codes that are currently being used are in the document “Files Sent to Host" (Appendix
B). EWR, Inc. does not use these codes within the host application. They are recorded in this manual for
documentation purposes only.
HEADER LAYOUT Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H = Header Record
2 Warehouse AN 7 2-8 Holder ID of warehouse which store the cotton
Holder ID
3 Batch Number N 4 9-12 Batch number, holder supplied
4 Batch Type N 2 13-14 21 = Shipping Order 30=Sample, 31=Staging
5 Batch Date N 8 15-22 Holder supplied batch date; MMDDYYYY
6 Batch Time N 6 23-28 Time batch was created; HHMMSS
7 Warehouse N 6 29-34 Code which identifies the warehouse where
Code bales are stored
8 Shipping Order AN 10 35-44 Shipper’s Order Number
Number
9 Shipper’s Mark AN 8 45-52 Shipper’s Mark
10 Balance Flag A 1 53 Y = Yes, net weights are included in the batch;
N = No, net weights are not included in the batch
from the host
11 Shipper Holder AN 7 54-60 Holder ID of Shipper, input when the Batch Type
ID 21 was sent to the Host
12 Requested Load N 8 61-68 Shipper’s requested loading date for the
Date shipment
13 Shipper Name AN 30 69-98 Name of Shipper; (May be truncated)
14 Reserved A 3 99-101 Reserved for future EWR, Inc. use.
15 Decert Action A 1 102 Blank,
Y=Has been decertificated
T = Certificated Transfer (All receipts are cert)
16 Bale count N 6 103-108 Bale Count
17 Staging Order A 1 109 Y = Yes; N = No – Batch 21 only
Sent
3-14

## Page 19

18 Block Receipts A 1 110 Y=Yes; N=No -Receipts are block receipts
19 Window Days N 2 111-112 Days before or after to reschedule
20 Shipping Order N 8 113-120 Unique number assigned by EWR, Inc
ID Batch 21 only
DETAIL LAYOUT – RECORD 1 (SO Instructions – Maximum of 99 Detail Records)
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Detail Type A 1 2 I = Shipping Instructions
3 Record Number N 2 3-4 Record Number (1-99)
4 Text Line AN 76 5-80 76 Character Text Line
5 Filler A 40 81-120 Reserved for EWR, Inc. use
DETAIL LAYOUT – RECORD 2 (SO Receipt List)
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Detail Type A 1 2 O = Shipping Order Receipts
3 Electronic Receipt N 7 3-9 Electronic Receipt Number for each bale to be
Number shipped – Input by the shipper when the Batch
Type 21 was sent to the Host
4 Net Weight N 3 10-12 Net weight of bale, only if Balance = Y in the
header
5 Crop Year N 4 13-16 Crop year of the receipt; YYYY
6 Gin Code N 5 17-21 may be blank, if a world receipt
7 Gin Tag N 7 22-28 may be blank, if a world receipt
8 Locator ID AN 8 29-36 Used to identify exact location of a bale in a
warehouse
9 IsUSDATenderable A 1 37 If Bale is certificated , then is the receipt
tenderable Y or N. If non-cert bale then field will
be blank.
A decert bale SHOULD be N.
10 Receipt Type A 1 38 R = Regular
C= Certificated #2
D = Decertificate #2 USA receipt
W = World Single Certificated
T = World Container
X= World Decertificated Receipt
11 World Tenderable A 1 39 T = Tenderable under ICE world contract
N = Non-Tenderable under ICE world contract
12 World Gin Tag AN 12 40-51 may be blank, if a non-world receipt
13 Filler AN 69 52- Reserved for EWR, Inc. use
120
3-15

## Page 20

TRAILER LAYOUT
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T = Trailer Record
2 Holder ID AN 7 2-8 The same as entered in the header record
(Warehouse Holder ID)
3 Batch Number N 4 9-12 The same as entered in the header record
4 Record Count N 9 13-21 Control total record count of detail records in the
batch
5 Total Weight N 9 22-30 Total net weight of bales in the shipping order
6 Hash Total N 15 31-45 Electronic receipt number hash total
7 Filler A 75 46- Reserved for EWR, Inc. use
120
3-16

## Page 21

HD23 - Shipping Order Update
This batch is a download of shipment information that has processed/updated when a batch 23 is
received. The recipient of the batch should verify the date field in the detail record against their records
for verification.
The shipper will receive the warehouse schedule date in the detail date field, while the warehouse will
receive the requested load date.
HEADER LAYOUT FOR HD23
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header record
2 Holder ID AN 7 2-8 Receiving holder ID
3 Batch Number N 4 9-12 Batch number, holder supplied
4 Type N 2 13-14 23= shipment update
5 Filler A 13 15-27 Reserved for EWR, Inc. use
8 Date N 8 28-35 Date created
9 Time N 6 36-41 Time created
10 Filler A 21 42-62 Reserved for EWR, Inc. use
11 From Holder ID AN 7 63-69 From EWR holder number
12 From Name A 40 70-109 From holder name
13 Filler A 11 110- Reserved for EWR, Inc. use
120
DETAIL LAYOUT FOR HD23
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail record
2 Warehouse N 6 2-7 Warehouse code for the order
Code
3 Action A 1 8-8 Reserved for EWR use
4 Bales N 5 9-13 Number of bales (Supplied by sender of 23)
5 Mark A 8 14-21
6 Order Number A 10 22-31 Shippers order number
7 Date N 8 32-39 Requested load date or Schedule date
8 Shipper Holder AN 7 40-46 Merchant holder number
ID
9 EWR ID N 8 47-54 EWR shipping order ID (Optional)
10 Window Days N 8 55-62 Days before or after to reschedule
11 Filler N 58 63-120 Reserved for EWR use
NOTE: Field 7 is the requested load date if the warehouse is receiving the 23 and the schedule date if
the merchant is receiving the file.
3-17

## Page 22

TRAILER LAYOUT FOR HD23
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer record
2 Holder ID AN 7 2-8
3 Batch Number N 4 9-12
4 Record Count N 9 13-21 Control total record count of the number of
detail records in the batch
5 Filler A 99 22-120
3-18

## Page 23

HD24 - Warehouse Invoice
The batch 24 will be provided to the shipper (merchant) in XML format. All of the data will be under a
node called “WarehouseInvoice”. This data is “passed” thru by EWR, Inc. If it is incomplete or wrong,
the warehouse should be contacted.
All files created by EWR will follow the usual filename convention (prefixed with HD24) with an .XML
(period XML) extension and will be stored in the usual holders NOTZIP FTP mailbox. There will be a
zipped (compressed) copy of this file with the .zip extension in the ZIP FTP Mailbox. For example:
HD24.1234.20080801.101022.83838A.XML
Example of a file received. NOTE: There may be more fields included than shown.
<?xml version="1.0" encoding="utf-8" ?>
<WarehouseInvoice ">
<Originator>
<Address>
<AddressType>Shipping</AddressType>
<Address1>P O Box 1</Address1>
<Address2 />
<City>Memphis</City>
<State>TN</State>
<CountryCode>US</CountryCode>
<PostalCode>79336</PostalCode>
</Address>
<PhoneNumber>
<PhoneNumberType>Main</PhoneNumberType>
<PhoneNumber>901-396-3243</PhoneNumber>
</PhoneNumber>
<Name>Tom Test warehouse</Name>
<Code>767070</Code>
</Originator>
<RemitTo>
<Address>
<AddressType>Billing</AddressType>
<Address1>P.O. Box 2827</Address1>
<City>Memphis</City>
<State>TN</State>
<CountryCode>US</CountryCode>
<PostalCode>79408-2827</PostalCode>
</Address>
<PhoneNumber>
<PhoneNumberType>Main</PhoneNumberType>
<PhoneNumber>800-111-8011</PhoneNumber>
</PhoneNumber>
<Name>Toms Test warehouse</Name>
3-19

## Page 24

<Instructions>Payable upon receipt of invoice. </Instructions>
</RemitTo>
<BillTo>
<Address>
<AddressType>Billing</AddressType>
<Address1>BOX 443</Address1>
<Address2 />
<City>MEMPHIS</City>
<State>TN</State>
<CountryCode>US</CountryCode>
<PostalCode>381010443</PostalCode>
</Address>
<Name>The shipper name</Name>
<AccountNumber>705</AccountNumber>
<Instructions>Payable upon receipt of invoice</Instructions>
</BillTo>
<Number>68193</Number>
<Date>2008-04-09</Date>
<Gross>1965.34</Gross>
<Tax>0</Tax>
<Total>1965.34</Total>
<Shipment>
<Charge>
<Item>
<Description>Compression</Description>
<Quantity>88</Quantity>
<UnitCost>9.25</UnitCost>
<Total>814</Total>
</Item>
</Charge>
<Charge>
<StorageRecap>
<StopDate>2008-04-08</StopDate>
<TotalDays>5762</TotalDays>
<Quantity>88</Quantity>
<Rate>0.07</Rate>
<Total>403.34</Total>
</StorageRecap>
<Item>
<Description>Storage</Description>
<Quantity>88</Quantity>
<UnitCost>4.583409</UnitCost>
<Total>403.34</Total>
</Item>
</Charge>
<Charge>
3-20

## Page 25

<Item>
<Description>Receiving</Description>
<Quantity>88</Quantity>
<UnitCost>3.25</UnitCost>
<Total>286</Total>
</Item>
</Charge>
<Charge>
<Item>
<Description>Loading Other</Description>
<Quantity>88</Quantity>
<UnitCost>5.25</UnitCost>
<Total>462</Total>
</Item>
</Charge>
<Number>247181</Number>
<Date>2008-04-08</Date>
<Mark>CRNZ</Mark>
</Shipment>
<FilePath>C:\FileImports\WebServices\1.8733.xml</FilePath>
</WarehouseInvoice>
3-21

## Page 26

HD25 – Phytosanitary Warehouse XML Delivery
The batch 25 will be provided to the warehouse in XML format. All of the data will be under a node
called “PhytosanitaryRequests”. This data is “passed” thru by EWR, Inc. If it is incomplete or wrong, the
merchant or shipper should be contacted.
All files created by EWR will follow the usual filename convention (prefixed with HD25) with an .XML
(period XML) extension and will be stored in the usual holders NOTZIP FTP mailbox. There will be a
zipped (compressed) copy of this file with the .zip extension in the ZIP FTP Mailbox. For example:
HD25.1234.20080801.101022.83838A.XML
Example of a file received. NOTE: There may be more fields included than shown.
<?xml version="1.0" encoding="us-ascii"?>
<PhytosanitaryRequests xmlns="EWRInc">
<ContractNumber>S04935.A01</ContractNumber>
<Exporter>
<Line1>COTTON LLC</Line1>
<Line2>55 GOODLETT FARMS PARKWAY</Line2>
<Line3>PO BOX 54</Line3>
<Line4>CORDOVA, TN 38446 US</Line4>
<AgentSignature>Amy</AgentSignature>
<AgentSignatureDate>2018-05-26</AgentSignatureDate>
<EWRShipperHolderID>M999999 </EWRShipperHolderID>
</Exporter>
<Applicant>
<Line1>INTERNATIONAL LOGISTIC</Line1>
<Line2>75 GOODLETT FARMS PARKWAY</Line2>
<Line3 />
<Line4>CORDOVA, TN 38016 US</Line4>
<PhoneNumber>(9999) 284-5000</PhoneNumber>
<EWRFreightForwarderHolderID>F000001</EWRFreightForwarderHolderID>
</Applicant>
<ForeignConsignee>
<Line1>LAX Los Angeles</Line1>
<Line2>US</Line2>
</ForeignConsignee>
<DateOfDeparture>2019-05-26</DateOfDeparture>
<PortOfExport>LAX Los Angeles US</PortOfExport>
<ConveyanceMeans>Ocean Vessel</ConveyanceMeans>
<PortOfEntry>SRG SEMARANG ID</PortOfEntry>
<Warehouse>
<EWRTrackingNumber>34739</EWRTrackingNumber>
<AcceptsElectronicPhytosanitary>true</AcceptsElectronicPhytosanitary>
<Line1>COMPRESS #6</Line1>
<Line2>2590 CR 95</Line2>
<Line3>PLAINVIEW, TX 79072 US</Line3>
<Code>911525</Code>
<EWRAction>NEW</EWRAction>
<ProduceQuantity>86</ProduceQuantity>
<QuantityAndName>
<Line1>100 Bales Cotton</Line1>
<Line2>Gossypium SPP</Line2>
</QuantityAndName>
3-22

## Page 27

<NumberAndDescription>
<Line1>100 Bales</Line1>
</NumberAndDescription>
<CertifiedOrigin>
<Line1>USA</Line1>
<Line2>ONCE INSPECTED PLEASE EMAIL APPLICANT</Line2>
<Line3>Team@group.com</Line3>
</CertifiedOrigin>
<Shipment>
<Mark>28B142</Mark>
<OrderNumber>1758290</OrderNumber>
<Bales>86</Bales>
</Shipment>
<Shipment>
<Mark>8B42</Mark>
<OrderNumber>58290</OrderNumber>
<Bales>14</Bales>
</Shipment>
</Warehouse>
</PhytosanitaryRequests>
3-23

## Page 28

HD25 – Phytosanitary Forwarder XML Delivery
The batch 25 will be provided to the forwarder in XML format. All of the data will be under a node
called “PhytosanitaryRequests”. This data is “passed” thru by EWR, Inc. If it is incomplete or wrong, the
merchant or shipper should be contacted.
All files created by EWR will follow the usual filename convention (prefixed with HD25) with an .XML
(period XML) extension and will be stored in the usual holders NOTZIP FTP mailbox. There will be a
zipped (compressed) copy of this file with the .zip extension in the ZIP FTP Mailbox. For example:
HD25.1234.20080801.101022.83838A.XML
Example of a file received. NOTE: There may be more fields included than shown.
<?xml version="1.0" encoding="us-ascii"?>
<PhytosanitaryRequests xmlns="EWRInc">
<ContractNumber>S05261.A04</ContractNumber>
<Exporter>
<Line1>ABC Merchant</Line1>
<Line2>255 GOOD FARMS PARKWAY</Line2>
<Line3>PO BOX 54</Line3>
<Line4>CORDOVA, TN 38016 US</Line4>
<AgentSignature>TOm</AgentSignature>
<AgentSignatureDate>2018-04-24</AgentSignatureDate>
<EWRShipperHolderID>M381180 </EWRShipperHolderID>
</Exporter>
<Applicant>
<Line1>BIG LOGISTIC</Line1>
<Line2>75 FARMS PARKWAY</Line2>
<Line3 />
<Line4>CORDOVA, TN 38016 US</Line4>
<PhoneNumber>(999) 999-5000</PhoneNumber>
<EWRFreightForwarderHolderID>F000001</EWRFreightForwarderHolderID>
</Applicant>
<ForeignConsignee>
<Line1>SAV Savannah</Line1>
<Line2>US</Line2>
</ForeignConsignee>
<DateOfDeparture>2018-06-03</DateOfDeparture>
<PortOfExport>SAV Savannah US</PortOfExport>
<ConveyanceMeans>Ocean Vessel</ConveyanceMeans>
<PortOfEntry>QCT PORT QASIM PK</PortOfEntry>
<trailer RecordCount="1" />
<Warehouse>
<EWRTrackingNumber>396</EWRTrackingNumber>
<AcceptsElectronicPhytosanitary>false</AcceptsElectronicPhytosanitary>
<Line1>DISTRIBUTION CENTER</Line1>
<Line2>101 South Street</Line2>
<Line3>WEST MEMPHIS, AR 72301 US</Line3>
<Code>167035</Code>
<EWRAction>NEW</EWRAction>
<ProduceQuantity>88</ProduceQuantity>
<QuantityAndName>
<Line1>88 Bales Cotton</Line1>
<Line2>Gossypium SPP</Line2>
3-24

## Page 29

</QuantityAndName>
<NumberAndDescription>
<Line1>88 Bales</Line1>
</NumberAndDescription>
<CertifiedOrigin>
<Line1>USA</Line1>
<Line2>ONCE INSPECTED PLEASE EMAIL APPLICANT</Line2>
<Line3>Email group.com</Line3>
</CertifiedOrigin>
<Shipment>
<Mark>6Y353</Mark>
<OrderNumber>1759522</OrderNumber>
<Bales>88</Bales>
</Shipment>
</Warehouse>
</PhytosanitaryRequests>
3-25

## Page 30

HD- Delivery of Block Receipt Detail Data Information
Created from Batch Types 08, 09, 10, 14, 15, 22, 50 & 51, 60 when a Disposition Holder is entered.
Received by the Disposition Holder.
Note: Batch Types 09 & 14, without a Disposition Holder, will not produce a “Delivery” of detail due to
the fact that the entire batch rejects if one error is detected in the original batch sent to the host.
HEADER LAYOUT FOR HD Block Record Size = 271
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H = Header Record
2 Holder ID AN 7 2-8 Holder ID - user receiving download
3 Batch Number N 4 9-12 Batch assigned by sender
4 Batch Type N 2 13-14 41 = Detail Block Receipt Data received
5 Request Flag A 1 15 Blank
6 Request Field AN 11 16-26 Batch 50 only = Action Code; Batch 15 change
Holder ID of person making change otherwise
blank
7 Holder Selection A 1 27 Blank
8 Batch Date N 8 28-35 Holder supplied batch date; MMDDYYYY
9 Batch Time N 6 36-41 Holder supplied batch time; HHMMSS
10 Draft Number AN 10 42-51 Bank Draft Number - if delivered via bank draft
11 Draft Amount N 10 52-61 Draft Amount - if delivered via bank draft
12 Filler A 1 62 Reserved for EWR, Inc. use
13 From Holder AN 7 63-69 Holder who transferred the data.
14 Filler A 1 70 Reserved for EWR, Inc. use
15 Originating Batch N 2 71-72 Batch type initiating this download (08, 09, 14,
Type 15, 50, 51, 52)
16 Holder Type A 15 73-87 Output of holder selection type
17 Holder Name A 40 88-127 Name of holder
18 Criteria Type A 15 128-142 Selection Criteria
19 Criteria A 37 143-179
Description
20 Filler A 1 180 Reserved for EWR, Inc. use
21 Block Receipts A 1 181 Always Y
22 Filler A 1 182 Reserved for EWR, Inc. use
23 EWR Transaction N 9 183-191 Assigned by EWR, Inc.
24 Receipt Count N 6 192-197
25 Filler A 74 198-271 Reserved for EWR, Inc. use
3-26

## Page 31

DETAIL LAYOUT FOR HD Block
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Detail Type A 1 2 R = Regular Block
3 Warehouse Code N 6 3-8 Warehouse Code of the Block
4 Electronic Receipt N 7 9-15 Electronic Block Number
Number
5 Crop Year N 4 16-19 Crop Year of the Block
6 Issue Date N 8 20-27 Date entered by the warehouse, not assigned
by EWR. Storage date of the bale -
MMDDYYYY
7 Receiving Fee N 4 28-31 9999 (2 decimal places); Warehouse defined
charge
Example 0250 = $2.50 - Charge is per bale
(US currency)
8 Storage Fee N 4 32-35 9999 (2 decimal places); Warehouse defined
charge
Example 0250 - $2.50. If storage Charge
Frequency is daily, the entry will display as
cents/day, e.g. 0950 =9.50 cents per day -
Charge is per bale. (US currency)
9 Storage Charge A 1 36 D=Daily; C=Calendar Months; S=Actual
Frequency Months (same day); F=Actual Months
(following day); M=Monthly (legacy support)
See Appendix J – Files Sent To EWR
10 Receiving Paid A 1 37 Y = Receiving paid or waived
N = not paid or waived
11 Loading Paid A 1 38 Y = Paid N = Not Paid
12 Classing Paid A 1 39 Y = Paid N = Not Paid
13 Storage Paid N 8 40-47 Storage paid through date; MMDDYYYY
Through Last date that storage charges against the bale
were paid
14 Mark AN 8 48-55 Shipper assigned mark
15 Purchase Order AN 10 56-65 Purchase Order Number assigned by seller
Number
16 Invoice Number AN 10 66-75 Invoice Number assigned by seller
17 Received From AN 30 76-105 Received from name
18 Licensing AN 2 106-107 Federal Licensing US
Authority Not Licensed NL
State Licensing Postal State Code
(GA is Georgia)
19 Locator ID AN 8 108-115 Used to identify exact location of a bale in a
warehouse
3-27

## Page 32

20 Electronic Receipt A 1 116 O = Open
Status C = Cancel
21 Electronic Receipt A 1 117 E = Electronic
Flag P = Paper
22 Receipt Type A 1 118 G = Negotiable O = Non-Negotiable
23 Paper Receipt N 7 119-125 Paper Receipt Number assigned by warehouse
Number (if any)
24 User Defined AN 12 126-137 12 bytes used to enter any optional
Field information
25 Warehouse/ A 1 138 Y = Warehouse & Producer are the same
Depositor entity
N = Warehouse & Producer not the same
26 Graded/Deposit A 1 139 Y = Graded at the request of the depositor
N = Not graded at request of the depositor
27 Bale Count N 5 140-144 Number of bales in block
28 Lot ID AN 12 145-156 Lot identifier from the depositor. Often
equivalent to the Mark
29 Total Net Weight N 6 157-162 Total Net Weight of bales in block
30 Total Tare Weight N 4 163-166 Total Tare Weight of bales in block
31 Control Number A/AN 10 167-176 A 10-character field used for control number
32 Draft Number A/N 10 177-186 Bank Draft Number assigned by seller
33 Holder Type A 1 187 M = Merchant
W = Warehouse
G = Gin
Z = Coop
P = Producer
C = Government
B = Bank
34 Filler A 84 188-271 Reserved for EWR, Inc. use
3-28

## Page 33

DETAIL- BALE DATA This record is not used for non-negotiable block receipts. For negotiable block
receipts, there will be one record for each bale in the block receipt.
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Detail Type A 1 2 B = Bale
3 Warehouse N 6 3-8 Warehouse Code of the Block
Code
4 Block Receipt N 7 9-15 Electronic Block Number
Number
5 Crop Year N 4 16-19 Crop year in which the cotton was grown: YYYY
6 Tag ID N 7 20-26 The tag number that is assigned by warehouse to
identify each bale in the entire block
7 Net Weight N 3 27-29 Gross weight of bale minus tare weight. User
enters appropriate amount
8 Tare Weight N 2 30-31 Represents the number pounds subtracted from
the gross weight to compensate for bagging and
ties on the bale
9 Gin Code N 5 32-36 USDA assigned code which identifies the site
where the cotton was ginned
10 Gin Tag N 7 37-43 Tag number assigned by gin
11 Filler 228 44-271 Reserved for EWR, Inc. use
TRAILER LAYOUT FOR HD Block
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T = Trailer Record
2 Holder ID AN 7 2-8 The same as entered in the header record
3 Batch N 4 9-12 The same as entered in the header record
Number
4 Record Count N 9 13-21 Control total record count of the number of
detail records in the batch
5 Filler A 9 22-30 Reserved for EWR, Inc. use
6 Hash Total N 15 31-45 Electronic Block number hash total
7 Filler 75 46-271 Reserved for EWR, Inc. use
3-29

## Page 34

HD43 - Warehouse Loan Status Delivery
This batch is a download of receipt information that has been placed under loan or redeemed by CCC for
a specific warehouse. It is produced when CCC sends a “CL” file (put under loan) or a “CR” file when it is
released. The recipient of the batch will be the issuing warehouse that has chosen to receive this file
(Holder Preferences). The warehouse will also be billed on a per receipt basis according to the latest
tariff.
HEADER LAYOUT FOR HD43 Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header record
2 Holder ID AN 7 2-8 Warehouse holder ID
3 Batch Number N 4 9-12 Batch number assigned by EWR
4 Batch Type N 2 13-14 43
5 Activity AN 11 15-25 CL or CR
6 Filler AN 1 26 Reserved for EWR Inc. use
7 Filler A 1 27 Reserved for EWR Inc. use
8 Batch Date N 8 28-35 Holder supplied batch date; MMDDYYYY
9 Batch Time N 6 36-41 Holder supplied batch time; HHMMSS
10 Filler AN 61 42-102 Reserved for EWR Inc. use
11 Receipt Count N 6 103-108 Number of receipts in file
12 Filler AN 12 80-120 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD43
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail record
2 Warehouse N 6 2-7 Warehouse code of the receipt
3 Receipt Number N 7 8-14 Electronic Receipt Number
4 Crop Year N 4 15-18 Crop year of the receipt
5 Status A 1 19 L=Under loan, R=Redeem
6 Loan Type A 1 20 A=Form-A, G=Form-G
7 Filler A 100 21-120 Reserved for EWR Inc. use
TRAILER LAYOUT FOR HD43
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer
2 Holder ID AN 7 2-8 Warehouse holder ID
3 Batch Number N 4 9-12 Batch number assigned by EWR
4 Record Count N 9 13-21 Number of receipts
5 Filler A 9 22-120 Reserved for EWR Inc. use
3-30

## Page 35

HD57 -Delivery Receipts via CMA Loan Redemption
Received by the CMA only
Batch Type 57, received from the host, is a batch which contains receipts that are to be redeemed by
the CMA. The header contains Redemption Date and E-mail address of redeemer. The detail contains
warehouse number, receipt number, crop year and redeemer’s calculated redemption amount.
HEADER LAYOUT FOR HD57 Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H = Header Record
2 Holder ID AN 7 2-8 Holder ID - CMA receiving the download
3 Batch Number N 4 9-12 Batch number assigned
4 Batch Type N 2 13-14 57 = CMA Loan Redemption
5 Batch Date N 8 15-22 Holder supplied batch date: MMDDYYYY
6 Batch Time N 6 23-28 Holder supplied batch time: HHMMSS
7 From Holder AN 7 29-35 Holder Redeeming Bales/Receipts
8 Redemption N 8 36-43 Date of redemption: MMDDYYYY
Date
9 Redeemer’s AN 45 44-88 E-mail address of redeemer
E-mail
10 Filler A 14 89-102 Reserved for EWR, Inc. use
11 Receipt Count N 6 103-
108
12 Filler A 12 109- Reserved for EWR, Inc. use
120
DETAIL LAYOUT FOR HD57
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Warehouse A 6 2-7 Warehouse Code of the receipt
Code
3 Electronic N 7 8-14 Electronic Receipt Number
Receipt
Number
4 Crop Year N 4 15-18 Crop Year of the receipt: YYYY
5 Redemption N 5 19-23 Redeemer’s calculated redemption amount
Amount 99999 (2decimal) 35025=$350.25
6 Reconcentrated A 1 24 Y = is reconcentrated loan
Loan N = Not reconcentrated loan
7 Previous N 6 25-30 Code of previous warehouse. Entered only if the
Warehouse bale is reconcentrated
3-31

## Page 36

8 Previous N 7 31-37 Warehouse receipt number from previous
Receipt warehouse. Entered only if the bale is
Number reconcentrated
9 Gin Code N 5 38-42 USDA assigned code which identifies the site
where the cotton was ginned
10 Gin Tag N 7 43-49 Sequential tag number assigned by the gin.
Number
11 Issue Date N 8 50-57 Date entered by the warehouse, not assigned by
EWR. Storage date of the bale-MMDDYYYY
12 Filler A 63 58- Reserved for EWR, Inc. use
120
TRAILER LAYOUT FOR HD57
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 Must be the same as enter in the header record
3 Batch N 4 9-12 The same as entered in the header record
Number
4 Record Count N 9 13-21 Control total record count of detail records in the
batch
5 Total Weight N 9 22-30 Total net weight of bales
6 Hash Total N 15 31-45 Electronic receipt number has total
7 Filler A 75 46-120 Reserved for EWR, Inc. use
3-32

## Page 37

HD64 - Warehouse Profile Requested
This file is generated from the original Batch Type 64 (Warehouse Profile - Request). This batch is a text
file and contains general (public) information about a specific warehouse. Any user on the system can
request warehouse information for any warehouse that uses EWR, Inc. as its provider.
HEADER LAYOUT FOR HD64 Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID AN 7 2-8 Holder ID of requestor
3 Batch Number N 4 9-12 Batch number , holder supplied
4 Batch Type N 2 13-14 64=Request Warehouse Profile
5 Batch Date N 8 15-22 Holder supplied batch date; MMDDYYYY
6 Batch Time N 6 23-28 Holder supplied batch time; HHMMSS
7 Filler A 92 29-120 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD64 (Record 1)
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Record Number N 2 2-3 01=First Record
3 Warehouse N 6 4-9 Warehouse Code
Code
4 Effective Date N 8 10-17 Effective date MMDDYYYY
5 Type Code A 1 18 F=Federal, S=State, O=Other
6 Name AN 40 19-58 Warehouse Name (trade name)
7 City AN 40 59-98 Warehouse Location (city)
8 State A 2 99-100 Warehouse Location (state)
9 Receiving Rate N 4 101-104
10 Storage Rate N 5 105-109
11 Compression N 4 110-113
Rate
12 Loading Rate N 4 114-117
13 Storage Charge A 1 118 D=Daily; C=Calendar Months; S=Actual Months
Frequency (same day); F=Actual Months (following day);
M=Monthly (legacy support)
See Appendix J – Files Sent To EWR
14 Filler A 2 119-120 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD64 (Record 2)
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Record Number N 2 2-3 02=Second Record
3-33

## Page 38

3 Warehouse N 6 4-9 Warehouse Code
Code
4 Effective Date N 8 10-17 Effective date; MMDDYYYY
5 City-Issued AN 40 18-57 City in which receipt is issued
6 State-Issued A 2 58-59 State in which receipt is issued
7 Signature A 40 60-99 Name of person signing receipt
8 License Number AN 6 100-105 Warehouse License Number
9 Fire Insurance A 1 106 Y=Has Fire Insurance, N=None
10 Open Yard A 1 107 Open Yard Endorsement
Endorsement Y=yes, N= no
11 Open Yard A 1 108 Open Yard disclaimer
Disclaimer Y=yes, N=no
12 Receiving A 1 109 Y=receiving fees include new ties; N= no
Includes Ties
13 Compression A 1 110 N=no compression facilities, compression is
Facilities not available;
Y=Compression service available
14 Claims/Liens A 1 111 The warehouse will have claims or liens on
bales other than normal tariff charges
Y=yes, N=no
15 Incorporated A 1 112 I = Incorporated; N = No Incorporated
Type U or Empty = Unknown
16 Incorporated A 2 113-114 US State abbreviation
State
17 Filler A 6 115-120 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD64 (Record 3)
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Record Number N 2 2-3 03 = Record Number
3 Legal Name A 80 4-83
4 EWR Warehouse A 9 84-92 Reserved for EWR, Inc. use
Profile ID
5 Filler A 28 193-120 Reserved for EWR, Inc. use
3-34

## Page 39

DETAIL LAYOUT FOR HD64 (Record 4)
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Record Number N 2 2-3 04 = Record Number
3 Legal City A 80 4-83 Legal entity name text line
4 Filler A 36 84-119 Reserved for EWR, Inc. use
5 Filler A 1 120 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD64 (Record 5)
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail record
2 Record Number N 2 2-3 05 = Record Number
3 Legal State A 80 4-83 Legal State – US Abbreviation
4 Filler A 37 84-120 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD64 (Record 6-37)
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Record Number N 2 2-3 Record Numbers = 06 through 37
3 Terms & AN 80 4-83 No longer used. This field will be filled with
Condition the following text: “Please go to
www.ewrinc.com\cotton to see terms.”
4 Filler A 37 84-120 Reserved for EWR, Inc. use
TRAILER LAYOUT FOR HD64
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T = Trailer Record
2 Holder ID AN 7 2-8 The same as enter in the header record
3 Batch Number N 4 9-12 The same as enter in the header record
4 Record Count N 9 13-21 Control total record count of detail records in
the batch
5 Filler A 99 22-120 Reserved for EWR, Inc. use
3-35

## Page 40

HD66 - Delivery of Reconciliation Detail
This batch is a download of all open receipt information contained in the host computer for a specific
holder. It is normally produced when a warehouse sends to the host, Batch Type 66. The recipient of
the batch will be the holder that sent the request.
HEADER LAYOUT FOR HD66 Record Size = 271
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H = Header Record
2 Holder ID AN 7 2-8 Holder ID who sent the batch
3 Batch Number N 4 9-12 Batch number , holder supplied
4 Batch Type N 2 13-14 66
5 Activity AN 11 15-25
6 Action Code AN 1 26
7 Filler A 1 27 Reserved for EWR Inc., use
8 Batch Date N 8 28-35 Holder supplied batch time;MMDDYYYY
9 Batch Time N 6 36-41 Holder supplied batch time; HHMMSS
10 Filler AN 8 42-49 Reserved for EWR Inc. use
11 Filler AN 53 50-102 Reserved for EWR Inc. use
12 Receipt Count N 6 103-108 Number of receipts in file
13 Filler AN 163 109-271 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD66
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Warehouse N 6 2-7 Warehouse code of the receipt
3 Electronic Receipt N 7 8-14 Receipt Number
Number
4 Crop Year N 4 15-18 Crop year of the receipt
5 Tare Weight N 4 19-22 Tare weight of bale or block
6 Net Weight N 6 23-28 Net weight of bale or block
7 Receiving Fee N 4 29-32 9999 (2 decimal); (US currency)
8 Storage Fee N 4 33-36 9999 (2 decimal); (US currency)
9 Storage Charge A 1 37 D=Daily; C=Calendar Months; S=Actual Months
Freq. (same day); F=Actual Months (following day);
M=Monthly (legacy support)
See Appendix J – Files Sent To EWR
10 Receiving Paid A 1 38 Y=Paid; N=Not paid
11 Loading Paid A 1 39 Y=Paid; N=Not paid
12 Classing Paid A 1 40 Y=Paid; N=Not paid
13 Compression Paid A 1 41 Y=Paid; N=Not paid
3-36

## Page 41

14 Reconcentrated A 1 42 R=Bale is reconcentrated
Space = Not reconcentrated
15 Previous N 6 43-48 Code of previous warehouse – Entered only if
Warehouse the bale is reconcentrated.
16 Previous Receipt N 7 49-55 Warehouse receipt number from previous
Number warehouse, entered for reconcentrated cotton
only
17 Gin Code Number N 5 56-60 USDA assigned code where the cotton was
ginned
18 Gin Tag Number N 7 61-67 Sequential tag number assigned by the gin
19 Storage Paid N 8 68-75 Storage paid through date; MMDDYYYY. Last
Through date that storage charges against the bale
were paid to the warehouse
20 Mark AN 8 76-83 Shipper assigned mark
21 Locator ID AN 8 84-91 Warehouse bale location
22 Electronic Receipt A 1 92 O=Open; C=Cancel; D=Deactivated; V=Void
Status
23 Electronic Receipt A 1 93 E=Electronic
Flag P = Paper
24 Receipt Type A 1 94 See Appendix D – Receipt Types in “Files Sent
to EWR” document.
25 Current Holder A 1 95 M = Merchant
Type W = Warehouse
G = Gin
Z = Coop
P = Producer
C = Government
B = Bank
26 Loan Transfer A 1 96 Y = Yes. This bale was transferred while under
loan (Reconcentrated Loan Transfer)
27 Filler N 5 97-101
28 Weight Date N 8 102-109 Weight date assigned by warehouse;
MMDDYYYY
29 Tenderable AN 2 110-111 AMS assigned
30 Rain Grown AN 1 112 R = Rain grown; N = Not rain grown; Unknown
31 Under S/O A 1 113 Y = Under open shipping order
32 Block Receipt A 1 114 Is this receipt a block receipt
33 Block Bales N 5 115-119 Number of bales on block
34 Is Stored Outside A 1 120 Y/N
35 EWR Container ID N 8 121-128 EWR unique number assigned to each
container
36 Filler AN 12 129-140
37 World A 1 141 T= Tenderable
Tenderable N = Non-Tenderable
3-37

## Page 42

38 Lot # N 6 142-147 Replaces field #27
39 World Gin Tag AN 12 148-159
40 Type Bagging A 1 160
41 Type of Ties A 1 161
42 Bagging A 1 162 Bag condition – User defined. Examples are:
Condition A = Bale is completely covered
B = Bale may have minor tears and an exposed
sample opening
C = Exposed cotton in addition to sample
opening
43 Compression A 1 163
Code
44 Filler 108 164-271
TRAILER LAYOUT FOR HD66
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 Holder ID who sent the batch
3 Batch Number N 4 9-12 The same as enter in the header record.
4 Record Count N 9 13-21 Number of receipts
5 Filler A 9 22-30 Reserved for EWR, Inc. use
6 Filler A 15 31-45 Reserved for EWR, Inc. use
7 Filler A 226 46-271 Reserved for EWR Inc. use
3-38

## Page 43

HD67 - EWR ASCII Text Message Received from EWR
HD67 is used to inform users of special events, such as if the database was temporarily unavailable
during a time of maintenance.
HEADER LAYOUT FOR HD67 Record Size = 85
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H-Header Record
2 Holder ID AN 7 2-8 Holder ID of participant receiving the message
from EWR
3 Batch Number N 4 9-12 Batch number assigned - Cannot be duplicated
within the same day
4 Batch Type N 2 13-14 67=ASCII Text Message from EWR, Inc. Host
Computer
5 Batch Date N 8 15-22 Holder supplied batch date; MMDDYYYY
6 Batch Time N 6 23-28 Holder supplied batch time; HHMMSS
7 Date Entered AN 8 29-36 Date EWR created the message
8 Filler A 49 37-85 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD67 (Maximum of 32 lines) Records 1-32
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Record N 2 2-3 Record number
Number
3 Text Line AN 80 4-83 80 character text line
4 Filler A 2 84-85 Reserved for EWR, Inc. use
TRAILER LAYOUT FOR HD67
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 The same as entered in the header record
3 Batch Number N 4 9-12 The same as entered in the header record
4 Record Count N 9 13-21 Control total record count of detail records in
the batch
5 Filler A 64 22-85 Reserved for EWR, Inc. use
3-39

## Page 44

HD68 - Holder Information Requested
Batch Type 68 is generated by a Batch Type 60 request for holder information on receipts. That is, Batch
Type 60 will allow a user who is either the Current Holder or Current Subholder to request Holder ID’s
for all entities which occupy these three fields in the Host computer. (Created by a Batch Type 60 when
Holder Type = A)
HEADER LAYOUT FOR HD68 Record Size =120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H-Header Record
2 Holder ID AN 7 2-8 Holder ID of requestor
3 Batch Number N 4 9-12 Batch number assigned
4 Batch Type N 2 13-14 68=Holder Information Request
5 Batch Date N 8 15-22 Holder supplied batch date; MMDDYYYY
6 Batch Time N 6 23-28 Holder supplied batch time; HHMMSS
7 Filler A 74 29-102 Reserved for EWR, Inc. use
8 Receipt Count N 6 103-108
9 Filler A 12 109-120 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD68
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Warehouse N 6 2-7 Warehouse Code of the Receipt
Code
3 Electronic N 7 8-14 Electronic Receipt Number
Receipt
Number
4 Crop Year N 4 15-18 Crop year of the Receipt
5 Current Holder AN 7 19-25 Holder ID of the current Holder of the
ID electronic receipt(s)
6 Subholder ID AN 7 26-32 Holder ID of the current Subholder of the
electronic receipt(s)
7 Previous AN 7 33-39 Holder ID of the previous Holder of the
Holder ID electronic receipt(s)
8 Electronic A 1 40 O=Open C=Cancel D=Deactivated V=Void
Receipt Status
9 Electronic A 1 41 E=Electronic
Receipt Flag P=Paper
10 Receipt Type A 1 42 See Appendix D – Receipt Types in “Files Sent
to EWR” document.
11 Filler A 78 43-120 Reserved for EWR, Inc. use
3-40

## Page 45

TRAILER LAYOUT FOR HD68
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 The same as entered in the header record
3 Batch Number N 4 9-12 The same as entered in the header record
4 Record Count N 9 13-21 Control total record count of the number of
detail records in the batch
5 Filler A 9 22-30 Reserved for EWR, Inc. use
6 Hash Total N 15 31-45 Electronic Receipt number hash total
7 Filler A 75 46-120 Reserved for EWR, Inc. use
3-41

## Page 46

HD86 - Shipping Order Release Request (Received by Banks Only)
A Batch Type 86 is an acknowledgment sent to the bank as a result of a Batch Type 21, Shipping Order
Receipt. The bank will only receive the Batch Type 86 if it is the Current Holder of all receipts on the
shipping order. This acknowledgment serves as the subholder’s (shipper) request to have the bank
release certain receipts for shipment.
The EWR PC Software utilizes the Batch Type 86 in two (2) ways:
• As a Batch Type 21 (Shipping Order) download , i.e., “Delivery” of the receipts in the shipping
order
• As a Shipping Order Release Request
Using the EWR, Inc. EWRPlus software, the bank can view the actual receipts contained in a shipping
order through the “Delivery” menu option. Using the Shipping Order Release Request (found under the
Receive Option in the PC software), the bank can easily take action on the shipping order, such as
release or return to seller
HEADER LAYOUT FOR HD86 Record Size = 60
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID of AN 7 2-8 Holder ID of Bank Holding the Receipts as
Bank Collateral
3 Batch N 4 9-12 Batch Number assigned by Host
Number
4 Batch Type N 2 13-14 86=Shipping Orders Held by Bank
5 Batch Date N 8 15-22 Date batch was created; MMDDYYYY
6 Batch Time N 6 23-28 Time batch was created; HHMMSS
7 Warehouse N 6 29-34 Warehouse code of facility where cotton is
Code stored
8 Shipping AN 10 35-44 S/O Number - This data is received in a batch
Order type 21 sent to host
Numbers
9 Shipper’s AN 8 45-52 Shipper's mark sent to host in a batch type 21
Mark
10 Holder ID of AN 7 53-59 Holder ID of shipper
Shipper
11 Block A 1 60 Blank =Regular Receipts
Receipts Y =Block Receipts
3-42

## Page 47

DETAIL LAYOUT FOR HD86
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Electronic N 7 2-8 Electronic Receipt Number
Receipt
Number
3 Net Weight N 3 9-11 Net weight of bale
4 Crop Year N 4 12-15 YYYY
5 Filler A 45 16-60 Reserved for EWR, Inc. use
TRAILER LAYOUT FOR HD86
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 Must be the same as entered in batch header
3 Batch Number N 4 9-12 Must be the same as entered in batch header
4 Record Count N 9 13-21 Control total record count of the detail records in the
batch
5 Total Weight N 9 22-30 Total net weight of bales in the batch if entered in
the original batch from the shipper
6 Hash Total N 15 31-45 Electronic receipt number hash total
7 Filler A 15 46-60 Reserved for EWR, Inc. use
3-43

## Page 48

HD87 - Bank Draft (Inbound only) (Received by Banks Only)
A Batch Type 87 is received by a bank as a result of a Batch Type 51 (Deliver Receipts Via Bank Draft).
This allows the bank to take the necessary action on the draft without re-keying any data. The actions
are:
• Regular Release
• Return to Seller
• Hold as Collateral (should not be used, before contacting EWR, Inc)
When action is taken by the bank, a Batch Type 71 is created.
FILE LAYOUT FOR HD87 (HEADER RECORD ONLY) Record Size = 150
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Bank Holder ID AN 7 2-8 Holder ID of Purchaser’s Bank
3 Batch Number N 4 9-12 Batch number assigned by user’s PC sending the
request or batch type 51
4 Batch Type N 2 13-14 Type=87 Bank Draft
5 Batch Date N 8 15-22 Date batch was created; MMDDYYYY
6 Batch Time N 6 23-28 Time batch was created: HHMMSS
7 Purchaser’s AN 7 29-35 Holder ID of Purchaser, input by creator of
Holder ID batch type 51
8 Purchaser AN 20 36-55 Purchaser Name from the holder control file in
Name the host
9 Seller Name AN 20 56-75 Seller Name
10 Holder ID of AN 7 76-82 Holder ID of Seller, or the holder who created
Seller the batch type 51
11 Draft Number AN 10 83-92 Bank Draft Number entered in batch type 51 by
seller
12 Draft Amount N 10 93-102 Draft Amount entered in batch type 51 by seller
99999999V99, must be at least $1.00
13 Presenting Bank AN 24 103-126 Presenting Bank Name - The bank on which the
Name draft is drawn
14 Block Receipts A 1 127 Blank=Regular Receipt Batch
Y=Block Receipt Batch
15 Receipt Count N 6 128-133 Count of receipts in Draft
16 Draft Control N 10 134-143 Host assigned number to flag the receipts in the
Number draft
17 Filler A 7 144-150 Reserved for EWR, Inc. use
3-44

## Page 49

HD91 - Bank Draft (Outbound Only) (Received by Banks Only)
A HD91 is received by the bank as a result of a Batch Type 51 (Deliver Receipts Via Bank Draft), when the
draft is made up of bales which the bank currently holds as collateral. This allows the bank to take the
necessary action on the draft without re-keying any data. The actions are:
• Regular Release
• Return to Seller
Unlike an Inbound draft, Outbound drafts cannot be held as collateral.
When the bank takes action on the outbound draft, a Batch Type 71 is created
HEADER RECORD ONLY Record Size = 150
Field Field Name Type Size Pos Descriptions
1 Record Type A 1 1 H=Header Record
2 Bank Holder ID AN 7 2-8 Holder ID of Purchaser’s Bank
3 Batch Number N 4 9-12 Batch number assigned by user sending the
request or Batch Type 51
4 Batch Type N 2 13-14 Type=91 Bank Draft - OUTBOUND DRAFTS
5 Batch Date N 8 15-22 Date batch was created; MMDDYYYY
6 Batch Time N 6 23-28 Time batch was created: HHMMSS
7 Purchaser’s AN 7 29-35 Holder ID of the buyer (Purchaser), input by
Holder ID creator of Batch Type 51
8 Purchaser’s Name A 20 36-55 Purchaser name of the holder.
9 Seller’s Name A 20 56-75 Seller name of the holder
10 Holder ID of Seller AN 7 76-82 Holder ID of Seller, or the holder who created
the Batch Type 51
11 Draft Number N 10 83-92 Bank draft number in Batch Type 51 by seller
12 Draft Amount N 10 93-102 Draft amount entered in Batch Type 51 by
seller 99999999V99
13 Presenting Bank AN 24 103-126 Presenting Bank Name - The bank on which
Name the draft is drawn
14 Block Receipts A 1 127 Blank=Regular Receipt Batch
Y=Block Receipt Batch
15 Receipt Count N 6 128-133 Count of receipts in Draft
16 Draft Control N 10 134-143 EWR assigned number to flag the receipts in
Number the draft
17 Purchaser’s AN 7 144-150 The Holder ID of the Purchaser’s bank. Can
Bank’s Holder ID be the same Bank ID as that of the seller
3-45

## Page 50

HD92 - Collateral Release Request (Received by Banks Only)
A Batch Type 92 is received by a bank as a result of a Batch Type 22 (Bank Release of Collateral.) The
bank will only receive the Batch Type 92 if it is the Current Holder of all receipts in the request. This file
serves as the subholder’s request to have the bank release holdership of certain receipts to another
party or to them. (Subholder becomes Holder).
The Batch Type 92 displays two (2) ways in the EWRPlus software,
• As a Batch Type 22 (Bank Release of Collateral) download , i.e., “Delivery” of the receipts to be
released, and
• As a Collateral Release Request.
Through the Delivery of receipts, the bank can view the actual receipts contained in the bank release of
collateral. Using the Collateral Release Request (found under the Receive Option in the EWRPlus
software), the bank can easily take action on the request, such as release or return to subholder.
HEADER LAYOUT FOR HD92 Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID of AN 7 2-8 Holder ID of Bank Holding the Receipts as
Bank Collateral
3 Batch N 4 9-12 Batch Number assigned by Host
Number
4 Batch Type N 2 13-14 92=Collateral Release Request
5 Batch Date N 8 15-22 Date batch was created; MMDDYYYY
6 Batch Time N 6 23-28 Time batch was created; HHMMSS
7 Release AN 10 29-38 A collateral release number assigned by the
Number Host to cross reference acknowledgments
8 Holder ID of AN 7 39-45 Holder ID of Merchant requesting the release of
Requestor / collateral
Subhoder
9 Tracking AN 10 46-55 An optional entry to be entered by the
Code/Number subholder/merchant for referencing collateral
release requests, entered in Batch Type 22
10 To Holder ID AN 7 56-62 Holder ID of the party which is to receive
Holdership. This could be the same holder ID of
the From Holder ID
11 Block Receipts A 1 63 Y=Block Receipts Batch
Blank=Regular Receipts Batch
12 Filler A 57 64-120 Reserved for EWR, Inc. use
3-46

## Page 51

DETAIL LAYOUT FOR HD92
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Warehouse N 6 2-7 Warehouse Code of the Receipt
Code
3 Electronic N 7 8-14 Electronic Receipt Number
Receipt
Number
4 Crop Year N 4 15-18 YYYY
5 Filler A 102 19-120 Reserved for EWR, Inc. use
TRAILER LAYOUT FOR HD92
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 Must be the same as entered in batch header
3 Batch Number N 4 9-12 Must be the same as entered in batch header
4 Record Count N 9 13-21 Control total record count of the detail records
in the batch
5 Hash Total N 15 22-36 Electronic receipt number hash total
6 Filler A 84 37-120 Reserved for EWR, Inc. use
3-47

## Page 52

HD97 – Batch 23 Compliance Detail
“Early warning” copies of this file are available for a fee (See current Tariff document). The HD97 file is
generated nightly (after midnight) and lists any Shipping/Staging Orders (with a request date) OR Batch
23 files that have not been responded to by a Batch 23. The Shipping/Staging Order/Batch 23 must have
been received by the provider within the past two business days.
“Early warning” indicates that the recipient has not responded but still has time to respond to remain in
compliance. All recipients will receive an “out of compliance” file, free of charge, once two business
days have elapsed.
HEADER LAYOUT FOR HD97 Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H = Header Record
2 Holder ID AN 7 2-8
3 Batch Number N 4 9-12 Batch number, holder supplied
4 Batch Type N 2 13-14 97
5 Filler AN 13 15-27 Reserved for EWR Inc. use
6 Batch Date N 8 28-35 Holder supplied batch time; MMDDYYYY
7 Batch Time N 6 36-41 Holder supplied batch time; HHMMSS
8 Early Warning A 1 42-43 Y=Early Warning report. Field will be blank for
out of compliance reports (free option).
9 Filler AN 79 44-120 Reserved for EWR Inc. use
DETAIL LAYOUT FOR HD97
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Warehouse ID N 6 2-7
3 Shipper ID AN 7 8-14 Shipper ID on the shipping order
4 Mark N 8 15-22
5 Order Number N 10 23-32
6 Received Date N 8 33-40 Date 21 / 31 / 23 file received by EWR
7 Batch Type N 2 41-42 21 / 23 / 31 = Batch Type indicator
8 Requested Date N 8 43-50 Shipper Requested Date from 31 / 21 / 23
9 Scheduled Date N 8 51-58 Warehouse Scheduled Date (if on file)
3-48

## Page 53

TRAILER LAYOUT FOR HD97
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 Holder ID who sent the batch
3 Batch Number N 4 9-12 The same as enter in the header record.
4 Record Count N 9 13-21 Number of receipts
5 Filler A 9 22-30 Reserved for EWR, Inc. use
6 Filler A 15 31-45 Reserved for EWR, Inc. use
7 Filler A 75 46-120 Reserved for EWR Inc. use
3-49

## Page 54

HD98 - Delivery of Custom Report Detail
This file is created by the provider system and is not the result of a request batch. It contains all open
receipts for a specific holder or subholder. It is normally produced at the end of a month or year, upon
request by a holder. There is a fee for each report.
HEADER LAYOUT FOR HD98 Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H = Header Record
2 Holder ID AN 7 2-8 Holder ID who sent the batch
3 Batch Number N 4 9-12 Batch number, holder supplied
4 Batch Type N 2 13-14 66
5 Activity AN 11 15-25
6 Action Code AN 1 26 W=Warehouse Reconciliation
H = Holder only receipts in 98 file
S = Subholder only and not on shipping order
X = Subholder including receipts under order
7 Filler A 1 27 Reserved for EWR Inc., use
8 Batch Date N 8 28-35 Holder supplied batch time; MMDDYYYY
9 Batch Time N 6 36-41 Holder supplied batch time; HHMMSS
10 Filler AN 8 42-49 Reserved for EWR Inc. use
11 Filler AN 53 50-102 Reserved for EWR Inc. use
12 Receipt Count N 6 103-108 Number of receipts in file
13 Filler AN 12 109-120 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HD98
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Warehouse N 6 2-7 Warehouse code of the receipt
3 Electronic Receipt N 7 8-14 Receipt Number
Number
4 Crop Year N 4 15-18 Crop year of the receipt
5 Tare Weight N 4 19-22 Tare weight of bale or block
6 Net Weight N 6 23-28 Net weight of bale or block
7 Receiving Fee N 4 29-32 9999 (2 decimal); (US currency)
8 Storage Fee N 4 33-36 9999 (2 decimal); (US currency)
9 Storage Charge A 1 37 D=Daily; C=Calendar Months; S=Actual Months
Freq. (same day); F=Actual Months (following day);
M=Monthly (legacy support)
See Appendix J – Files Sent To EWR
10 Receiving Paid A 1 38 Y=Paid; N=Not paid
11 Loading Paid A 1 39 Y=Paid; N=Not paid
3-50

## Page 55

12 Classing Paid A 1 40 Y=Paid; N=Not paid
13 Compression Paid A 1 41 Y=Paid; N=Not paid
14 Reconcentrated A 1 42 R=Bale is reconcentrated
Space = Not reconcentrated
15 Previous N 6 43-48 Code of previous warehouse – Entered only if
Warehouse the bale is reconcentrated.
16 Previous Receipt N 7 49-55 Warehouse receipt number from previous
Number warehouse, entered for reconcentrated cotton
only
17 Gin Code Number N 5 56-60 USDA assigned code where the cotton was
ginned
18 Gin Tag Number N 7 61-67 Sequential tag number assigned by the gin
19 Storage Paid N 8 68-75 Storage paid through date; MMDDYYYY. Last
Through date that storage charges against the bale
were paid to the warehouse
20 Mark AN 8 76-83 Shipper assigned mark
21 Locator ID AN 8 84-91 Warehouse bale location
22 Electronic Receipt A 1 92 O=Open; C=Cancel; D=Deactivated; V=Void
Status
23 Electronic Receipt A 1 93 E=Electronic
Flag P = Paper
24 Receipt Type A 1 94 See Appendix D – Receipt Types in “Files Sent
to EWR” document.
25 Current Holder A 1 95 M = Merchant
Type W = Warehouse
G = Gin
Z = Coop
P = Producer
C = Government
B = Bank
26 Loan Transfer A 1 96 Y = Yes. This bale was transferred while under
loan (Reconcentrated Loan Transfer)
27 Lot Number N 5 97-101 ICE Lot number entered by warehouse
28 Filler N 8 102-109
29 USDA Tenderable A 2 110-111 AMS assigned
30 Rain Grown A 1 112 R = Rain grown; N = Not rain grown
31 Under S/O A 1 113 Y = Under open shipping order
32 Block Receipt A 1 114 Is this receipt a block receipt
33 Block Bales N 5 115-119 Number of bales on block
34 Is Stored Outside A 1 120 Y/N
3-51

## Page 56

TRAILER LAYOUT FOR HD98
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 Holder ID who sent the batch
3 Batch Number N 4 9-12 The same as enter in the header record.
4 Record Count N 9 13-21 Number of receipts
5 Filler A 9 22-30 Reserved for EWR, Inc. use
6 Filler A 15 31-45 Reserved for EWR, Inc. use
7 Filler A 75 46-120 Reserved for EWR Inc. use
3-52

## Page 57

SECTION 4 FILE TYPE HA (SUCCESSFUL ACKNOWLEDGEMENT FILES)
This section explains how the EWR, Inc. host system handles successful acknowledgement files.
Successful acknowledgements are batches that completed with NO errors. There are 4 basic layouts for
acknowledgement files:
• Type 85 (The standard, default layout)
• Type 81 Collateral acknowledgement layout
• Type 18 BMAS acknowledgement layout
• Type 25/26 Phytosanitary acknowledgement layout
When the host generates acknowledgements, it consists of the following types lines:
• Batch Header (H)
• Acknowledgment (AC)
• Batch Trailer (T)
Acknowledgment s are received by all users who create and transmit batches to the host and in some
cases by the users whose Holder IDs are involved in the transactions.
4-1

## Page 58

HA – Default Successful Acknowledgments
This type of acknowledgment is also known as Type 85.
This acknowledgment is sent to users to inform them of the status of batches which involve their Holder
ID. This type of acknowledgment is received by the holder who creates a batch, and a similar
acknowledgment is generated and sent to any user, if any, whose Holder ID was included in the batch.
For example, if a producer transfers holdership of his/her bales to a merchant, both users would receive
a Holder Acknowledgment. Holder acknowledgments tell the user who sent the batch (From Holder),
who the batch was sent to (To Holder), when it was sent, the number of receipts in the batch, and the
type of batch.
The batch number segment of the file name is the initiating batch type; for instance, if the file name
starts with HA21, then the sending batch was a type 21 batch (Shipping order). Excluding bank releases,
in that instance a bank release of shipping order is HA70, while a draft is HA71.
HEADER LAYOUT Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID AN 7 2-8 Holder ID who will receiving
acknowledgement
3 Batch Number N 4 9-12 Batch number of sending holder
4 Batch Type N 2 13-14 85
5 Batch Date N 8 15-22 Holder supplied batch date; MMDDYYYY
6 Batch Time N 6 23-28 Holder supplied batch time; HHMMSS
7 Filler A 1 29 Reserved for EWR Inc. use
8 EWR ID N 9 30-38 Internal ID assigned by EWR, Inc
9 Original Batch N 4 39-42 Valid only on bank release batches (70-72)
Number
10 Original Batch N 2 43-44 Valid only on bank release batches (70-72)
Type
11 Sender A 1 45 Holder initiated the batch (Y/N)
DETAIL LAYOUT Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 2 1-2 AC=Acknowledgments
2 Orig. Transmission N 6 3-8 Transmission Number
Number
3 Date Acknowledged N 8 9-16 Date Host Completed Batch Processing
Request
4 Time Acknowledged N 6 17-22 Time Host Completed Batch Processing
Request
5 Original Batch Type N 2 23-24 Batch Type (sent from PC to host)
6 Original Batch Number N 4 25-28 Batch Number (sent from PC to host)
4-2

## Page 59

7 From Holder ID AN 7 29-35 Holder ID who sent batch
8 From User ID AN 6 36-41 User ID who sent batch
9 Name of From Holder AN 20 42-61 Name of From Holder - stored in the host
control file, input by the host
10 To Holder ID AN 7 62-68 To Holder ID
11 Name of To Holder AN 20 69-88 Name of To Holder - stored in the host
control file, input by the host
12 Activity ID AN 10 89-98 Identifying characters such as SO number,
Mark, Draft #, CCC Collateral Release Code,
EWR Container ID
13 Total Detail Records N 8 99-106 Total detail records in batch sent to host
Sent
14 Total Detail Processed N 8 107-114 Total detail records that processed in the
batch
15 Action Flag A 1 115 If field 5 is 34,35,38: C=Container created
D=Container Dissolved
Otherwise:
B=Block Receipts (HA71 B= Pending
Release)
R=Regular or Release if HA70 or HA71
C=Bank holds collateral (buyer becomes
subholder)
T=Returned to seller or Rejected by Bank;
S=Sent to CCC for Loan Approval – Batch 53
A=Approved by CCC for loan – Batch 53
N=No Download (Batch 50 only)
L=Loan Option Delivery (Batch 63 only)
U=Warehouse updating Locator ID (Batch
03 & 04 only)
16 Bale Count A 5 116-120 Number of bales/receipts (not records) in
the batch
TRAILER LAYOUT
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer
2 Holder ID AN 7 2-8 Holder ID receiving acknowledgement
3 Batch Number N 4 9-12 Batch number assigned
4 Record Count N 9 13-21 Number of receipts
5 Filler A 9 22-120 Reserved for EWR Inc., use
4-3

## Page 60

HA18 – BMAS Receipted and Non-Receipted Bales Acknowledgment
This acknowledgment is sent to users to inform them of the status of batches which involve their Holder
ID. The HA18 provides the final BMAS in the last field “BMAS Bale Count”. Also, the individual numbers
used to calculate the final BMAS number are provided in this acknowledgement file.
HEADER LAYOUT Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID AN 7 2-8 Holder ID who will receiving
acknowledgement
3 Batch Number N 4 9-12 Batch number of sending holder
4 Batch Type N 2 13-14 18
5 Batch Date N 8 15-22 Holder supplied batch date; MMDDYYYY
6 Batch Time N 6 23-28 Holder supplied batch time; HHMMSS
7 Filler A 1 29 Reserved for EWR Inc. use
8 Filler N 9 30-38 Reserved for EWR Inc. use
9 Filler N 4 39-42 Reserved for EWR Inc. use
10 Filler N 2 43-44 Reserved for EWR Inc. use
11 Filler A 1 45 Reserved for EWR Inc. use
DETAIL LAYOUT Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 2 1-2 AC=Acknowledgments
2 Filler N 6 3-8 Transmission Number
3 Date Acknowledged N 8 9-16 Date Host Completed Batch Processing
Request
4 Time Acknowledged N 6 17-22 Time Host Completed Batch Processing
Request
5 Original Batch Type N 2 23-24 Batch Type (sent from PC to host)
6 Original Batch Number N 4 25-28 Batch Number (sent from PC to host)
7 From Holder ID AN 7 29-35 Holder ID who sent batch
8 From User ID AN 6 36-41 User ID who sent batch
9 Name of From Holder AN 20 42-61 Name of From Holder - stored in the host
control file, input by the host
10 Flow Reporting Date N 8 62-69 Sent by Warehouse in Batch 18 Header
11 Total Bales Not Picked N 5 70-74 Sent by Warehouse when submitting flow
Up report
12 Total Bales Shipped N 5 75-79 Sent by Warehouse when submitting flow
report
13 Total Previously N 5 80-84 Calculated when 18 is processed.
Reported Bales Previously reported bale within past 12
months
4-4

## Page 61

14 Bales In Error N 5 85-89 Bales that resulted in an error code
15 Effective Capacity N 6 90-95 Current warehouse effective capacity as
recorded on the provider system
16 Filler A 3 96-98
17 Total Details Rec Sent N 8 99-106 (Same position as default HA)
18 Total Detail Rec Process N 8 107-114 (Same position as default HA)
19 Filler N 1 115
20 BMAS Bale Count N 5 116-120 Final BMAS – Calculated when 18 is
processed. (Total Shipped + Total Not
Picked Up) – (Previously Reported + Bales
In Error)
TRAILER LAYOUT
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer
2 Holder ID AN 7 2-8 Holder ID receiving acknowledgement
3 Batch Number N 4 9-12 Batch number assigned
4 Record Count N 9 13-21 Number of receipts
5 Filler A 9 22-120 Reserved for EWR Inc., use
Calculating Flow Percentage:
To calculate the warehouse flow percentage, divide the BMAS Bale Count (Field 20) by the Effective
Capacity (Field 15), then multiply by 100.
Example:
Effective Capacity = 50,000
BMAS Bale Count = 2,250
2250 / 50000 = 0.045
0.045 x 100 = 4.5%
4-5

## Page 62

HA25/26 – Phytosanitary Holder Acknowledgment
Batch Type 25 is an acknowledgment sent to users to inform them of the status of batches which
involved their Holder ID. This acknowledgment is received by the merchant. A summary of the
acknowledgment is as follows:
Batch Type 25 AC to the Merchant:
• “From Holder” will be the merchant (buyer’s) Holder ID.
• “EWR Tracking Number” is the unique EWR assigned number assigned to each phytosanitary
request. This number should be saved by the merchant and referenced when sending any
updates or cancels for phyto request.
Batch Type 26 AC to the Merchant:
• “From Holder” will be the warehouses Holder ID.
• “EWR Tracking Number” is the unique EWR assigned number assigned to each phytosanitary
request.
HEADER LAYOUT Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID AN 7 2-8 Holder ID who will receiving
acknowledgement
3 Batch Number N 4 9-12 Batch number of sending holder
4 Batch Type N 2 13-14 25/26
5 Batch Date N 8 15-22 Holder supplied batch date; MMDDYYYY
6 Batch Time N 6 23-28 Holder supplied batch time; HHMMSS
7 From User AN 6 29-34 User ID that sent batch
8 EWR Trans ID N 9 35-43 EWR Transaction ID
9 Records Sent N 8 44-51 Total detail records sent to host
10 Records Process N 8 52-59 Total detail records processed
11 Sender A 1 60 Holder initiated the batch (Y/N)
11 Filler A 1 61-120 Reserved for EWR, Inc. use
DETAIL LAYOUT Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 2 1-2 AC=Acknowledgments
2 Filler N 6 3-8 Reserved for EWR, Inc. use
3 Date N 8 9-16 Date Host Completed Batch Processing
Acknowledged Request
4 Time N 6 17-22 Time Host Completed Batch Processing
Acknowledged Request
5 From Holder AN 7 23-29 Holder ID who sent batch (sent from PC to
ID host)
4-6

## Page 63

6 Name of From AN 17 30-46 Name of From Holder – stored in the host
Holder control file, input by the host
7 Forwarder AN 7 47-53 Holder ID of Freight Forwarder
Holder ID
8 Forwarder AN 17 54-70 Name of Forwarder
Name
9 EWR Tracking N 8 71-78 Unique tracking number assigned by EWR to
Number each phyto request (per whse)
10 Total Marks N 2 79-80 Total number of marks on phyto
11 Bale Count N 5 81-85 Number of bales/receipts (not records) in the
batch.
12 Warehouse ID N 8 86-91 Warehouse inspecting phyto
13 Warehouse AN 17 92-108
Name
14 Activity ID A 10 109-118
15 Filler AN 2 119-120 Reserved for EWR, Inc. use
TRAILER LAYOUT FOR HA81
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer
2 Holder ID AN 7 2-8 Holder ID receiving acknowledgement
3 Batch Number N 4 9-12 Batch number assigned
4 Record Count N 9 13-21 Number of receipts
5 Filler A 9 22-120 Reserved for EWR Inc., use
4-7

## Page 64

HA81 - Collateral Holder Acknowledgment
(This acknowledgment is received by collateralized merchants and their banks)
Holders can designate if they want a Bank to automatically receive holdership of ALL receipts
transferred to their Holder ID number. For example, if a merchant uses warehouse receipts for
collateral, anytime another user sends receipts to the merchants Holder ID number, the host will
process the batch and immediately change holdership to the Bank’s Holder ID number and move the
merchant (buyer) to the subholder field.
Batch Type 81 is an acknowledgment sent to users to inform them of the status of batches which
involved their Holder ID. This acknowledgment is received by the merchant and by the bank who holds
the receipts as collateral. A summary of the acknowledgment is as follows:
Batch Type 81 AC to the Merchant:
• “From Holder” will be the Holder who delivered/transferred holdership to the merchant.
• “To Holder” will be the merchant (buyer’s) Holder ID.
• “Collateral Holder” will be the bank’s Holder ID.
Batch Type 81 AC to the Bank:
• “From Holder” will be the Holder who delivered/transferred holdership to the merchant.
• “To Holder” will be the bank’s Holder ID.
• “Collateral Holder” will be the merchant (buyer’s) Holder ID.
HEADER LAYOUT FOR HA81 Record Size = 120
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID AN 7 2-8 Holder ID who will receiving
acknowledgement
3 Batch Number N 4 9-12 Batch number of sending holder
4 Batch Type N 2 13-14 81
5 Batch Date N 8 15-22 Holder supplied batch date; MMDDYYYY
6 Batch Time N 6 23-28 Holder supplied batch time; HHMMSS
7 Filler A 1 29-120 Reserved for EWR Inc. use
DETAIL LAYOUT FOR HA81 Record Size = 120
Field Field Name Ty Size Pos Description
pe
1 Record Type A 2 1-2 AC=Acknowledgments
2 Originating N 6 3-8 Transmission Number
Transmission
Number
3 Date N 8 9-16 Date Host Completed Batch Processing
Acknowledged Request
4-8

## Page 65

4 Time N 6 17-22 Time Host Completed Batch Processing
Acknowledged Request
5 Original Batch N 2 23-24 Batch Type (sent from PC to host)
Type
6 Original Batch N 4 25-28 Batch number (sent from PC to host)
Number
7 From Holder ID AN 7 29-35 Holder ID who sent batch (sent from PC to
host)
8 From User ID AN 6 36-41 User ID who sent batch (sent from PC to host)
9 Name of From AN 17 42-58 Name of From Holder – stored in the host
Holder control file, input by the host
10 To Holder ID AN 7 59-65 Holder ID of Bank which became the holder of
the receipts *the To Holder ID will change
from the Bank’s ID to the Subholder ID to
accomomodate the IBM Mail Handling
System. This change is necessary to ensure
that the bank and the merchant receive an AC
11 Name of To AN 17 66-82 Name of Bank [To Holder] – stored in the host
Holder control file, input by the host.
12 Collateral / AN 7 83-89 Holder ID of Merchant who is the subholder of
Subholder ID the receipts *the Subholder ID will change
from the Merchant’s ID to the Subholder ID to
accommodate the host system. This change is
necessary to ensure that the bank and the
merchant receive an AC
13 Activity ID AN 10 90-99 Identifying characters such as SO number,
Mark, Draft #, etc.
14 Total Detail N 8 100-107 Total detail records in batch sent to host
Records Sent
15 Total Detail N 8 108-115 Total detail records that processed in the
Processed batch
16 Bale Count A 5 116-120 Number of bales/receipts (not records) in the
batch.
4-9

## Page 66

TRAILER LAYOUT FOR HA81
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer
2 Holder ID AN 7 2-8 Holder ID receiving acknowledgement
3 Batch Number N 4 9-12 Batch number assigned
4 Record Count N 9 13-21 Number of receipts
5 Filler A 9 22-120 Reserved for EWR Inc., use
4-10

## Page 67

SECTION 5 FILE TYPE HE (ERROR ACKNOWLEDGEMENT FILES)
This section contains information regarding batch processing and rejections, i.e., what causes a batch to
reject, and what type of acknowledgments the user will receive.
Errors: How Processing is affected and expected acknowledgments
Errors are caused by any number of mistakes including invalid entries, or lack of required information.
The EWR host does not verify information, it only checks to ensure that the entries are within the
parameters of the field specifications.
When batches which contain errors are transmitted to the host, errors will be identified and
acknowledged to the user. The acknowledgments generated vary by batch.
The following batches do not process any of the data if one error is detected by the host. The host
REJECTS the entire batch and no receipts are updated.
BATCH TYPES: 05, 06, 19, 20, 21, 24, 30, 31, 34, 37, 38, 51, 55, 65, 70, 71, and 72
All other batch types will continue processing if errors are detected by the host. However, there is an
exception: If the first 11 records in the batch are in error, the host will REJECT the entire batch. For
example, if there are 20 records in a batch and records 1,3,5,7,9,11,13,15,17, and 19 have errors, the
host will process 10 records and reject 10.
On the other hand, if the first consecutive 11 (1-11) receipts are in error, the host will reject the entire
batch. The reason for the entire batch rejecting is that if the first 11 bales are in error, it is very possible
that the batch contains many additional errors, therefore the host rejects the batch instead of
downloading an error message for all receipts in the batch.
When the host generates and HE file it consists of the following 4 lines (minimum):
• Batch Header (H) – Same layout has HA85
• Acknowledgments (AC) – Same Layout as HA85
• Error(s) line; There are 3 types ET , EB or ED, see the layout below for specifics
• Batch Trailer (T) – Same Layout as HA85
5-1

## Page 68

To determine what processed and what failed, the following steps should be taken:
Examine the following fields of the AC line:
14 Total Detail N 8 99-106 Total detail records in batch sent to host
Records Sent
15 Total Detail N 8 107-114 Total detail records that processed in the
Processed batch
16 Action Flag A 1 115 E
17 Bale Count A 5 116-120 Number of bales/receipts (not records) in the
batch.
The above 4 fields should reflect, the total detail sent (or that the host was able to examine), the total
detail lines processed and the bales updated. Notice this is bales and not receipts updated, this is due to
block receipts may contain more than 1 bale.
Also remember if the 1st eleven lines are in error, the batch will not process any further, thus the total
sent may be 11, processed 0.
Examine the ET, EB and ED lines
There should be a single ET line, if the entire transmission file is corrupt.
There should be a single EB line, if the batch is not formatted correctly.
There may be multiple ED lines for each receipt in error.
ET DETAIL [Error in Transmission]
Field Field Name Type Size Pos Description
1 Record Type A 2 1-2 ET=Error in Transmission file, Header or
Trailer
2 Originating N 6 3-8 Transmission Number (sent form PC to the
Transmission Number Host)
3 Date Error Occurred N 8 9-16 Date Error Occurred
4 Time Error Occurred N 6 17-22 Time Error Occurred
5 Error Code N 3 23-25 Application Assigned Code, Created by the
Host
*6 Error Data AN 8 26-33 Specific Field in Error
7 Additional Information A 32 34-65 Can be used to provide additional
information about the error
8 Filler A 55 66-120 Reserved for EWR, Inc. use
*(Format is dependent on value of each Error Code)
5-2

## Page 69

EB and ED DETAIL [EB = Error in Batch] [ED = Error in Detail]
Field Field Name Type Size Pos Description
1 Record Type A 2 1-2 EB=Error in Batch Header or Batch Trailer
ED=Error in Batch Detail
2 Originating N 6 3-8 Transmission Number (sent from PC to Host)
Transmission
Number
3 Date Error N 8 9-16 Date Error Occurred at Host
Occurred
4 Time Error N 6 17-22 Time Error Occurred at Host
Occurred
5 Error Code N 3 23-25 Application Assigned Code determined by the
host
6 Original Batch N 2 26-27 Batch Type (sent from PC to host)
Type
7 Original Batch N 4 28-31 Batch number sent from PC to host
Number
8 Originating Holder AN 7 32-38 Holder who sent batch to host
ID
9 Originating User ID AN 6 39-44 User ID who sent Batch
10 Error Data AN 40 45-84 Can be used to provide additional info about
error; otherwise blanks (format is dependent
on Error Code) – Normally will contain
warehouse code, receipt number and crop
year
11 Error Message AN 32 85- EWR Host error message
116
12 Filler A 4 117- Reserved for EWR, Inc. use
120
5-3

## Page 70

SECTION 6 FILE TYPE HS (SUMMARY FILES)
HS78 - Block Receipt Summary
A HS78 file provides the holder and subholder of a block receipt with the number of block receipts
(negotiable and non-negotiable) and total number of bales (negotiable and non-negotiable) they hold by
warehouse.
HEADER LAYOUT FOR HS78 Record Size = 100
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID AN 7 2-8 Holder ID who will receive summaries
3 Batch Number N 4 9-12 Batch Number generated by Host
4 Batch Type N 2 13-14 78=Block Receipts summary for holder
5 Batch Date N 8 15-22 Date batch was created at host; MMDDYYYY
6 Batch Time N 6 23-28 Time batch was created at host; HHMMSS
7 Filler A 72 29-100 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HS78
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D = Detail Record
2 Holder ID AN 7 2-8 Holder ID = Holder of block receipts
3 Warehouse Code N 6 9-14 Warehouse code where block receipts are
held
4 Crop Year N 4 15-18 Crop Year of receipts held
5 Up to Date N 8 19-26 Totals calculated as of date; MMDDYYYY
6 Up to Date N 6 27-32 Totals calculated as of time; HHMMSS
7 Current Holder N 8 33-40 Current Holder count of negotiable block
Negotiable Count receipts
8 Current Holder N 8 41-48 Current Holder count of negotiable bales
Negotiable Bale
Count
9 Subholder N 8 49-56 Subholder count of negotiable block receipts
Negotiable Count
10 Subholder N 8 57-64 Subholder count of negotiable bales
Negotiable Bale
Count
11 Current Holder N 8 65-72 Current count of non-negotiable receipts
Non-Negotiable
Count
6-1

## Page 71

12 Current Holder N 8 73-80 Current count of non-negotiable bales
Non-Negotiable
Bale Count
13 Subholder Non- N 8 81-88 Subholder count of non-negotiable receipts
Negotiable Count
14 Subholder Non- N 8 89-96 Subholder count of non-negotiable bales
Negotiable Bale
Count
15 Filler A 4 97-100 Reserved for EWR, Inc. use
TRAILER LAYOUT FOR HS78
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T = Trailer Record
2 Holder ID AN 7 2-8 The same as entered in the header record
3 Batch Number N 4 9-12 The same as entered in the header record
4 Record Count N 9 13-21 Control total record count of detail records in
the batch
5 Filler A 79 22- Reserved for EWR, Inc. use
100
6-2

## Page 72

HS82 - Receipts Held Summary
HS82 is a summary of receipts held or subheld; which is generated each night and delivered to the
holder’s mailbox. The information contained in the summary is calculated through the previous day’s
activity.
Received by all Users who have requested that their holder profile be flagged so that this information is
given to them on a daily basis
NOTE: Receipts on this page refer to regular receipts (negotiable and non-negotiable)
Block receipts are NOT included in these totals.
For all users, specifically warehouses, summaries do not include receipts which are canceled.
Receipts transferred to the warehouse in a shipping order will be included in a warehouse holder
summary until the receipts are canceled.
HEADER LAYOUT FOR HS82 Record Size = 100
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID AN 7 2-8 Holder ID who will receive summaries
3 Batch Number N 4 9-12 Batch Number generated by Host
4 Batch Type N 2 13-14 82=Receipts held summary for
holder/subholder
5 Batch Date N 8 15-22 Date batch was created at host; MMDDYYYY
6 Batch Time N 6 23-28 Time batch was created at host; HHMMSS
7 Filler A 72 29-100 Reserved for EWR, Inc. use
6-3

## Page 73

DETAIL LAYOUT FOR HS82
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Holder ID AN 7 2-8 Holder ID of receipts held
3 Warehouse Code N 6 9-14 Warehouse Code that identifies the storage
location
4 Crop Year N 4 15-18 Crop Year of receipts held
5 Up to Date N 8 19-26 Totals calculated as of date (MMDDYYYY)
6 Up to Time N 6 27-32 Totals calculated as of time (HHMMSS)
7 Current Holder N 8 33-40 Total number of receipts held as of 12:00
Balance midnight of the previous day (this total does
not include canceled receipts)
8 Subholder Balance N 8 41-48 Total number of receipts held as subholder -
(no CCC or Whse) This total excludes receipts held by
warehouses and CCC
9 Subholder Balance N 8 49-56 Total number of receipts in Price Support Loan
(CCC is Holder) Program (CCC is Holder) and recipient of
acknowledgment/summary is the Subholder
10 Electronic N 8 57-64 Total number of uncanceled Electronic
Receipts held Receipts held (Received by warehouses only)
(Whse Only)
11 Paper Receipts N 8 65-72 Total number of uncanceled Paper Receipts
Held (Whse Only) held (Received by warehouses only)
12 Reserved A 8 73-80 Blank
13 Under Shipping N 8 81-88 Total number of receipts under a shipping
Order order
14 Pending Bank N 8 89-96 Total number of receipts pending a bank
release
15 Filler A 4 97-100 Reserved for EWR, Inc. use
TRAILER LAYOUT FOR HS82
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 The same as entered in the header record
3 Batch Number N 4 9-12 The same as entered in the header record
4 Record Count N 9 13-21 Control total record count of detail records in
the batch
5 Filler A 79 22-100 Reserved for EWR, Inc. use
6-4

## Page 74

HS83 - Summary of Receipts Issued (Received by Warehouse Users Only)
HS83 is a summary which is generated each night and delivered to the Warehouse’s holder mailbox.
The information contained in the summary is calculated through the previous day’s activity. It contains
the total number of receipts issued during the period August 1 through July 31. The total will include all
receipts issued during that period regardless of the crop year assigned. We believe that these dates will
give the entire Cotton Belt the most accurate totals for a harvest season.
Warehouses are encouraged to retain the July 31 report (Delivered on August 1), as it will be the last
report for the period August 1 - July 31.
HEADER LAYOUT FOR HS83 Record Size = 100
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H=Header Record
2 Holder ID AN 7 2-8 Holder ID who will receive summaries
3 Batch Number N 4 9-12 Batch Number generated by Host
4 Batch Type N 2 13-14 83=Receipts held summary for holder
5 Batch Date N 8 15-22 Date batch was created at host; MMDDYYYY
6 Batch Time N 6 23-28 Time batch was created at host; HHMMSS
7 Filler A 72 29-100 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HS83
Field Field Name Type Size Pos Description
1 Record Type A 1 1 D=Detail Record
2 Holder ID AN 7 2-8 Holder ID of receipts issued
3 Warehouse Code N 6 9-14 Warehouse Code of receipts issued
4 Filler AN 4 15-18 Reserved for EWR, Inc. use
5 Up to Date N 8 19-26 Totals calculated as of date; MMDDYYYY
6 Up to Time N 6 27-32 Totals calculated as of time; HHMMSS
7 *Issued-Regular N 8 33-40 Total number of electronic regular and
& Certificated certificated warehouse receipts issued as of
midnight (includes active and canceled
receipts)
8 *Issued-Block N 8 41-48 Number of electronic block receipts issued
9 *Issued-Cancel N 8 49-56 Number of receipts canceled
10 *Issued-Block N 8 57-64 Number of electronic block receipts canceled
Cancel
11 *Issued- N 8 65-72 Number of certificated receipts issued.
Certificated
12 *Cancel- N 8 73-80 Number of certificated receipts cancelled.
Certificated
13 Filler A 20 81-100 Reserved for EWR, Inc. use
*Total Issued Year-to-Date; Year is defined as the period beginning August 1 and ending July 31.
6-5

## Page 75

TRAILER LAYOUT FOR HS83
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 The same as entered in the header record
3 Batch N 4 9-12 The same as entered in the header record
Number
4 Record Count N 9 13-21 Control total record count of detail records in
the batch
5 Filler A 79 22-100 Reserved for EWR, Inc. use
6-6

## Page 76

HS89 - Bank Collateral Summaries (Banks Only)
A HS89 is a summary which provides banks with the number of bales they hold by subholder and by
warehouse. The batch is generated each night and placed in the banks Holder ID mailbox. The collateral
summaries are provided only once each day and are calculated through the previous day’s totals.
HEADER LAYOUT FOR HS89 Record Size = 90
Field Field Name Type Size Pos Description
1 Record Type A 1 1 H = Header Record
2 Holder ID AN 7 2-8 Holder ID who will receive summaries
3 Batch Number N 4 9-12 Batch Number generated by Host
4 Batch Type N 2 13-14 82 = Receipts held summary for
holder/subholder
5 Batch Date N 8 15-22 Date batch was created at host; MMDDYYYY
6 Batch Time N 6 23-28 Time batch was created at host; HHMMSS
7 Filler A 62 29-90 Reserved for EWR, Inc. use
DETAIL LAYOUT FOR HS89
Field Field Name Type Size Pos Description s
1 Record Type A 1 1 D = Detail Record
2 SubHolder ID AN 7 2-8 Sub Holder ID of the receipts (Bank is holder)
3 Merchant Name AN 25 9-33 Name of merchant who is the subholder
4 Warehouse Code N 6 34-39 Warehouse Code of receipts held as
collateral
5 Non-Block Balance N 6 40-45 Current count of receipts in the warehouse
6 Block Balance N 6 46-51 Current count of block receipts in the
warehouse
7 Block Bale Balance N 6 52-57 Current total of block bales in the
warehouse
8 Pending Non Block N 6 58-63 Current total of pending releases of non-
block receipts
9 Pending Block N 6 64-69 Current total of pending releases of block
receipts
10 Pending Block N 6 70-75 Current total of pending releases of block
Bales bales
11 Filler A 15 76-90 Reserved for EWR, Inc. use
6-7

## Page 77

TRAILER LAYOUT FOR HS89
Field Field Name Type Size Pos Description
1 Record Type A 1 1 T=Trailer Record
2 Holder ID AN 7 2-8 The same as entered in the header record
3 Batch Number N 4 9-12 The same as entered in the header record
4 Record Count N 9 13-21 Control total record of detail records in the
batch
5 Filler A 69 22-90 Reserved for EWR, Inc. use
6-8

### Table 1

| EWR Cotton Client Interface Manual   |
|:-------------------------------------|
| Files Received From EWR              |
| Updated: 08/20/2025                  |
| ©Copyright 1996-2025, EWR, Inc.      |

### Table 2

| SECTION 1 Table of Contents                                                                                         |                                                                                                                                                   |
|:--------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| SECTION 2 OVERVIEW ............................................................................................ 2-1 |                                                                                                                                                   |
| SECTION 3 FILE TYPE HD (DETAIL FILES) ........................................................ 3-1                  |                                                                                                                                                   |
|                                                                                                                     | HD –Default Delivery of Detail Data Information (Non-Block) ............................................................... 3-1                   |
|                                                                                                                     | HD07 - Cancel Receipts Delivery File .................................................................................................... 3-10    |
|                                                                                                                     | HD13 - Warehouse Bale Relocation File ............................................................................................... 3-12        |
|                                                                                                                     | HD21, 30, 31 - Shipping Orders Instructions & Receipts ...................................................................... 3-14                |
|                                                                                                                     | HD23 - Shipping Order Update ............................................................................................................. 3-17   |
|                                                                                                                     | HD24 - Warehouse Invoice ................................................................................................................... 3-19 |
|                                                                                                                     | HD25 – Phytosanitary Warehouse XML Delivery ................................................................................. 3-22                |
|                                                                                                                     | HD25 – Phytosanitary Forwarder XML Delivery ................................................................................... 3-24              |
|                                                                                                                     | HD- Delivery of Block Receipt Detail Data Information ....................................................................... 3-26                |
|                                                                                                                     | HD43 - Warehouse Loan Status Delivery ............................................................................................. 3-30          |
|                                                                                                                     | HD57 -Delivery Receipts via CMA Loan Redemption ........................................................................... 3-31                  |
|                                                                                                                     | HD64 - Warehouse Profile Requested ................................................................................................. 3-33         |
|                                                                                                                     | HD66 - Delivery of Reconciliation Detail .............................................................................................. 3-36      |
|                                                                                                                     | HD67 - EWR ASCII Text Message Received from EWR ......................................................................... 3-39                    |
|                                                                                                                     | HD68 - Holder Information Requested ................................................................................................ 3-40         |
|                                                                                                                     | HD86 - Shipping Order Release Request (Received by Banks Only) .................................................... 3-42                          |
|                                                                                                                     | HD87 - Bank Draft (Inbound only) (Received by Banks Only) .............................................................. 3-44                     |
| HD91 - Bank Draft (Outbound Only)                                                                                   | (Received by Banks Only) ....................................................... 3-45                                                             |
|                                                                                                                     | HD92 - Collateral Release Request (Received by Banks Only) ............................................................. 3-46                     |
|                                                                                                                     | HD97 – Batch 23 Compliance Detail ..................................................................................................... 3-48      |
|                                                                                                                     | HD98 - Delivery of Custom Report Detail ............................................................................................. 3-50        |
|                                                                                                                     | ii                                                                                                                                                |

### Table 3

| SECTION 4 FILE TYPE HA (SUCCESSFUL ACKNOWLEDGEMENT FILES) .. 4-1                               |                                                                                                                                                 |
|:-----------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                | HA – Default Successful Acknowledgments ........................................................................................... 4-2         |
|                                                                                                | HA18 – BMAS Receipted and Non-Receipted Bales Acknowledgment .................................................. 4-4                             |
|                                                                                                | HA25/26 – Phytosanitary Holder Acknowledgment .............................................................................. 4-6                |
|                                                                                                | HA81 - Collateral Holder Acknowledgment ........................................................................................... 4-8         |
| SECTION 5 FILE TYPE HE (ERROR ACKNOWLEDGEMENT FILES) ............. 5-1                         |                                                                                                                                                 |
| SECTION 6 FILE TYPE HS (SUMMARY FILES) ................................................... 6-1 |                                                                                                                                                 |
|                                                                                                | HS78 - Block Receipt Summary .............................................................................................................. 6-1 |
|                                                                                                | HS82 - Receipts Held Summary .............................................................................................................. 6-3 |
| HS83 - Summary of Receipts Issued                                                              | (Received by Warehouse Users Only) ....................................... 6-5                                                                  |
|                                                                                                | HS89 - Bank Collateral Summaries (Banks Only) .................................................................................... 6-7          |

### Table 4

| File names follow this pattern:                      |                                                              |
|:-----------------------------------------------------|:-------------------------------------------------------------|
| HSBB.NNNN.YYYYMMDD.HHMMSS.UUUUUU.dat or .zip, where: |                                                              |
| H                                                    | H holder                                                     |
| S                                                    | Type of file: D=detail, A=Acknowledgment, E=Error, S=Summary |
| BB                                                   | 2-digit batch type                                           |
| NNNN                                                 | Batch number                                                 |
| YYYYMMDDD                                            | Date                                                         |
| HHMMSS                                               | Time                                                         |
| UUUUUU                                               | Unique number                                                |

### Table 5

| SECTION 3 FILE TYPE HD (DETAIL FILES)                                                                        |                                                                                                              |                                           |     |
|:-------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|:------------------------------------------|:----|
| HD –Default Delivery of Detail Data Information (Non-Block)                                                  |                                                                                                              |                                           |     |
| T                                                                                                            | his file is the default or standard delivery file created from several batch types: (01, 02, 03, 04, 06, 08, |                                           |     |
| 22, 32, 35, 38, 39, 42, 44, 45, 50, 51, 52, 54, 56, 60, 62, 65; and 63).                                     |                                                                                                              |                                           |     |
| T                                                                                                            | his batch is a download of detailed receipt information contained in the host computer.  It is produced      |                                           |     |
| when users send to the host, batch type that is delivering receipts or updating receipts (in certain cases). |                                                                                                              |                                           |     |
| Normally, the recipient of the batch will be the entity who is the current holder or subholder of the        |                                                                                                              |                                           |     |
| receipts.                                                                                                    |                                                                                                              |                                           |     |
| T                                                                                                            | his file can be in 2 formats: Long or Short. The default is the Long format unless the holder has            |                                           |     |
| contacted EWR, Inc. support staff and requested that EWR send short records. This setting is saved in        |                                                                                                              |                                           |     |
| the holder profile.  A Short record download will contain receipt information only, required data and        |                                                                                                              |                                           |     |
| optional data.  A Long record download will contain the classing data.                                       |                                                                                                              |                                           |     |
| H                                                                                                            | D54 is received when CCC updates the bale information.                                                       |                                           |     |
| H                                                                                                            | D56 is received when CCC releases a bale from loan.                                                          |                                           |     |
| N                                                                                                            | ote: In January 2014, a certificated issue batch (Type 02) will have the tenderable field changed to         |                                           |     |
| allow for 3 options:                                                                                         |                                                                                                              |                                           |     |
|                                                                                                              | •                                                                                                            | Blank = Tenderable                        |     |
|                                                                                                              | •                                                                                                            | NT = Non Tenderable                       |     |
|                                                                                                              | •                                                                                                            | SD = Tenderable with Smith Doxey classing |     |
|                                                                                                              |                                                                                                              |                                           | 3-1 |

### Table 6

| Default Detail Delivery File Layout   |              |      |      |       |                                      |
|:--------------------------------------|:-------------|:-----|:-----|:------|:-------------------------------------|
| Short Record Size = 271               |              |      |      |       | Long Record Size = 345               |
| HEADER LAYOUT                         |              |      |      |       |                                      |
| Field                                 | Field Name   | Type | Size | Pos   | Description                          |
| 1                                     | Record Type  | A    | 1    | 1     | H=Header Record                      |
| 2                                     | Holder ID    | AN   | 7    | 2-8   | Holder ID – Person/Company making    |
|                                       |              |      |      |       | request                              |
| 3                                     | Batch Number | N    | 4    | 9-12  | Batch number , holder supplied       |
| 4                                     | Batch Type   | N    | 2    | 13-14 | Originating batch type               |
| 5                                     | Request      | A    | 1    | 15    | Single character                     |
|                                       | Flag/Action  |      |      |       | If field 4 is batch type 65 then the |
|                                       | Code         |      |      |       | following table applies:             |

### Table 7

| Single character                     |                         |
|:-------------------------------------|:------------------------|
| If field 4 is batch type 65 then the |                         |
| following table applies:             |                         |
| A                                    | All Receipts            |
| C                                    | Crop Year               |
| D                                    | Draft Number            |
| G                                    | Gin Code                |
| I                                    | Invoice Number          |
| L                                    | Loan Number             |
| O                                    | Purchase Order Number   |
| P                                    | Previous Holder ID      |
| R                                    | Grower Reference Number |
| S                                    | Subholder               |
| T                                    | EWR Container ID        |
| W                                    | Warehouse Code          |
| Z                                    | Shipping Order Number   |

### Table 8

| 6   | Request Field    | AN   | 11   | 16-26   | Text comment regarding the batch             |
|:----|:-----------------|:-----|:-----|:--------|:---------------------------------------------|
|     | / Activity Field |      |      |         | or                                           |
|     |                  |      |      |         | If field 4 is 34,35,38 then the field is the |
|     |                  |      |      |         | EWR Container ID processed in the batch      |
|     |                  |      |      |         | i                                            |
|     |                  |      |      |         | f field 4 is batch type 65 the following     |
|     |                  |      |      |         | table applies:                               |
|     |                  |      |      |         | Draft Number                                 |
|     |                  |      |      |         | AN                                           |
|     |                  |      |      |         | 10                                           |

### Table 9

| EWR Container ID processed in the batch   |                                          |    |    |
|:------------------------------------------|:-----------------------------------------|:---|:---|
| i                                         | f field 4 is batch type 65 the following |    |    |
| table applies:                            |                                          |    |    |
|                                           | Draft Number                             | AN | 10 |
|                                           | Gin Code                                 | N  | 5  |
|                                           | Invoice Number                           | AN | 10 |
|                                           | Loan Number                              | N  | 5  |
|                                           | Purchase Order                           | AN | 10 |
|                                           | Previous Holder                          | AN | 7  |
|                                           | Grower Reference                         | N  | 11 |
|                                           | Subholder                                | AN | 7  |
|                                           | Warehouse Code                           | N  | 6  |
|                                           | S/O Number                               | AN | 10 |
|                                           | EWR Container ID                         | N  | 8  |
| Empty unless batch type 65 Then the       |                                          |    |    |

### Table 10

|    |               |    |    |         | Holder ID is designated as the current       |
|:---|:--------------|:---|:---|:--------|:---------------------------------------------|
|    |               |    |    |         | holder.                                      |
| 8  | Batch Date    | N  | 8  | 28-35   | Holder supplied batch date; MMDDYYYY         |
| 9  | Batch Time    | N  | 6  | 36-41   | Holder supplied batch time; HHMMSS           |
| 10 | Draft Number  | AN | 10 | 42-51   | Bank Draft Number - if delivered via bank    |
|    |               |    |    |         | draft, otherwise zero or empty.              |
| 11 | Draft Amount  | N  | 10 | 52-61   | Draft Amount - if delivered via bank draft,  |
|    |               |    |    |         | otherwise zero or empty.                     |
| 12 | Long/Short    | A  | 1  | 62      | N = Short Record (no classing data)          |
|    | Record        |    |    |         | default;                                     |
|    |               |    |    |         | Y = Long Record (with classing data)         |
| 13 | From Holder   | AN | 7  | 63-69   |                                              |
| 14 | Holder Type   | A  | 15 | 70-84   | Output of holder selection type; i.e.,       |
|    |               |    |    |         | Holder; Subholder; Both. This is only filled |
|    |               |    |    |         | on batch types 65 and 60.                    |
| 15 | Holder Name   | A  | 40 | 85-124  | Name of the holder on file with EWR.         |
| 16 | Criteria Type | A  | 15 | 125-139 | This is only applicable to batch types 60    |
|    |               |    |    |         | and 65.                                      |

### Table 11

| 17   | Criteria Name   | A   | 40    | 140-179   | Criteria description. This is only applicable   |
|:-----|:----------------|:----|:------|:----------|:------------------------------------------------|
|      |                 |     |       |           | to batch types 60 and 65                        |
| 18   | Certificated    | A   | 1     | 180       | Blank = Regular Batch                           |
|      | Batch           |     |       |           | C = Certificated Batch                          |
| 19   | Block Receipts  | A   | 1     | 181       | Blank = No                                      |
|      |                 |     |       |           | N = No                                          |
|      |                 |     |       |           | Y = Yes                                         |
| 20   | Detail Source   | A   | 1     | 182       | If field 4 is 62 or 63: U=Holder is updating    |
|      |                 |     |       |           | warehouse fields on receipt  and receiver       |
|      |                 |     |       |           | is NOT the holder of receipts                   |
| 21   | Transaction ID  | N   | 9     | 183-191   | Reserved for EWR use.                           |
| 22   | Receipt Count   | A   | 6     | 192-197   |                                                 |
| 23   | Filler          | A   | 74/14 | 198-      | Short Record – 74; Long Record – 148            |
|      |                 |     | 8     | 271/345   | Reserved for EWR, Inc. use                      |

### Table 12

| DETAIL LAYOUT   |                |      |      |       |                                            |
|:----------------|:---------------|:-----|:-----|:------|:-------------------------------------------|
| Field           | Field Name     | Type | Size | Pos   | Description                                |
| 1               | Record Type    | A    | 1    | 1     | D = Detail Record                          |
| 2               | Warehouse      | N    | 6    | 2-7   | Warehouse code of the receipt              |
| 3               | Electronic     | N    | 7    | 8-14  | Electronic Receipt Number                  |
|                 | Receipt Number |      |      |       |                                            |
| 4               | Crop Year      | N    | 4    | 15-18 | Crop year of the receipt                   |
| 5               | Issue Date     | N    | 8    | 19-26 | Date entered by the warehouse, not         |
|                 |                |      |      |       | assigned by EWR – Storage date of the bale |
|                 |                |      |      |       | – MMDDYYYY                                 |
| 6               | Tare Weight    | N    | 2    | 27-28 | Represents pounds subtracted from gross    |
|                 |                |      |      |       | weight to compensate for bagging and ties  |
|                 |                |      |      |       | on the bale                                |
| 7               | Net Weight     | N    | 3    | 29-31 | Gross weight of bale minus tare weight –   |
|                 |                |      |      |       | User enters appropriate amount             |
| 8               | Bagging/Ties   | A    | 2    | 32-33 | Bagging in 32 / Ties in 33                 |
| 9               | Bagging        | A    | 1    | 34    | Bag condition – User defined.  Examples    |
|                 | Condition      |      |      |       | are:                                       |
|                 |                |      |      |       | A = Bale is completely covered             |
|                 |                |      |      |       | B = Bale may have minor tears and an       |
|                 |                |      |      |       | exposed sample opening                     |
|                 |                |      |      |       | C = Exposed cotton in addition to sample   |
|                 |                |      |      |       | opening                                    |
| 10              | Compression    | A    | 1    | 35    | Compression Code, valid entries are 1-7:   |
|                 | Code           |      |      |       | 1 = Flat                                   |
|                 |                |      |      |       | 2 = Modified Flat                          |
|                 |                |      |      |       | 3 = Standard Density                       |
|                 |                |      |      |       | 4 = Gin Standard                           |
|                 |                |      |      |       | 5 = Gin Universal Density                  |
|                 |                |      |      |       | 6 = Warehouse Universal Density            |
|                 |                |      |      |       | 7 = Gin Universal Density (1995)           |
| 11              | Receiving Fee  | N    | 4    | 36-39 | 9999 (2 decimal); Warehouse defined        |
|                 |                |      |      |       | charge, example 0250-$2.50 (US currency)   |
| 12              | Storage Fee    | N    | 4    | 40-43 | 9999 (2 decimal); Warehouse defined        |
|                 |                |      |      |       | charge, example 0250-$2.50 – If Storage    |
|                 |                |      |      |       | Charge Frequency is Daily, the entry will  |
|                 |                |      |      |       | display as cents/day.                      |
|                 |                |      |      |       | e.g., 0950=$9.50 per day(US currency)      |
| 13              | Storage Charge | A    | 1    | 44    | D=Daily; C=Calendar Months; S=Actual       |
|                 | Frequency      |      |      |       | Months (same day); F=Actual Months         |
|                 |                |      |      |       | (following day); M=Monthly (legacy         |
|                 |                |      |      |       | support)                                   |
|                 |                |      |      |       | See Appendix J – Files Sent To EWR         |
| 14              | Receiving Paid | A    | 1    | 45    | Y=receiving paid or waived                 |
|                 |                |      |      |       | N = not paid or waived                     |

### Table 13

| 15   | Loading Paid     | A   | 1   | 46      | Y= Paid; N=Not paid or waived                  |
|:-----|:-----------------|:----|:----|:--------|:-----------------------------------------------|
| 16   | Classing Paid    | A   | 1   | 47      | Y = Paid; N = Not Paid                         |
| 17   | Compression      | A   | 1   | 48      | Y = Paid; N = Not Paid                         |
|      | Paid             |     |     |         |                                                |
| 18   | Reconcentrated   | A   | 1   | 49      | R = Bale is reconcentrated                     |
|      |                  |     |     |         | Space = Not reconcentrated                     |
| 19   | Previous         | N   | 6   | 50-55   | Code of previous warehouse - Entered only      |
|      | Warehouse        |     |     |         | if the bale is reconcentrated                  |
| 20   | Previous Receipt | N   | 7   | 56-62   | Warehouse receipt number from previous         |
|      | Number           |     |     |         | warehouse, entered for reconcentrated          |
|      |                  |     |     |         | cotton only.                                   |
| 21   | Gin Code         | N   | 5   | 63-67   | USDA assigned code which identifies the        |
|      | Number           |     |     |         | site where the cotton was ginned               |
| 22   | Gin Tag Number   | N   | 7   | 68-74   | Sequential tag number assigned by the gin      |
| 23   | Storage Paid     | N   | 8   | 75-82   | Storage paid through date; MMDDYYYY.           |
|      | Through          |     |     |         | Last date that storage charges against the     |
|      |                  |     |     |         | bale were paid to the warehouse                |
| 24   | State Code       | AN  | 2   | 83-84   | USDA assigned State Code                       |
| 25   | County Code      | N   | 3   | 85-87   | USDA assigned County Code                      |
| 26   | Farm Number      | N   | 5   | 88-92   | Farm Serial number used for identifying        |
|      |                  |     |     |         | specific areas of production                   |
| 27   | Loan Number      | N   | 5   | 93-97   | FSA/CCC assigned Loan Number                   |
| 28   | CCC Loan Type    | A   | 1   | 98      | A = Form A; G = Form G; Blank = no loan        |
| 29   | CCC Loan Date    | N   | 8   | 99-106  | Loan Date. This field is initially supplied by |
|      |                  |     |     |         | the sender of the loan batch. Later it is      |
|      |                  |     |     |         | updated by CCC when the loan is accepted,      |
|      |                  |     |     |         | rejected or updated by CCC.                    |
| 30   | Mark             | AN  | 8   | 107-114 | If the receipt is under shipment, then this    |
|      |                  |     |     |         | field is the shipper mark. Otherwise it is     |
|      |                  |     |     |         | the mark from the batch header upload.         |
| 31   | Purchase Order   | AN  | 10  | 115-124 | Purchase Order Number assigned by seller       |
|      | Number           |     |     |         |                                                |
| 32   | Invoice Number   | AN  | 10  | 125-134 | Invoice Number assigned by seller              |
| 33   | Grower           | N   | 11  | 135-145 |                                                |

### Table 14

| 36   | Licensing      | A   | 2   | 185-186                          | US = USA Federal Licensing                  |
|:-----|:---------------|:----|:----|:---------------------------------|:--------------------------------------------|
|      | Authority      |     |     |                                  | NL =  Not Licensed                          |
|      |                |     |     |                                  | US Postal State Code = State Licensing      |
|      |                |     |     |                                  | IC = ICE Licensed (World)                   |
| 37   | Locator ID     | AN  | 8   | 187-194  Warehouse bale location |                                             |
| 38   | Electronic     | A   | 1   | 195                              | O=Open; C=Cancel; D=Deactivated; V=Void     |
|      | Receipt Status |     |     |                                  |                                             |
| 39   | Electronic     | A   | 1   | 196                              | E = Electronic                              |
|      | Receipt Flag   |     |     |                                  | P = Paper                                   |
| 40   | Receipt Type   | A   | 1   | 197                              | R = USA Regular                             |
|      |                |     |     |                                  | C = Certificated #2 (USA)                   |
|      |                |     |     |                                  | D = USA Decertificated                      |
|      |                |     |     |                                  | G = Block Negotiable                        |
|      |                |     |     |                                  | O = Block Non-Negotiable                    |
|      |                |     |     |                                  | T = World Container                         |
|      |                |     |     |                                  | W = World Certificated                      |
|      |                |     |     |                                  | X = World Decertificated                    |
| 41   | Paper Receipt  | N   | 7   | 198-204                          | Paper number assigned by warehouse (if      |
|      | Number         |     |     |                                  | any)                                        |
| 42   | Producer Name  | AN  | 34  | 205-238                          | Producer Name (May be truncated) on         |
|      | /              |     |     |                                  | world cotton.  On world cotton the first 12 |
|      | World Gin Tag  |     |     |                                  | characters will be the world gin tag        |
| 43   | EAD Eligible   | A   | 1   | 239                              | Y = Yes                                     |
|      |                |     |     |                                  | N = No or Blank                             |
| 44   | Gin Charges    | N   | 4   | 240-243                          | Used to enter gin fees when applicable      |
| 45   | User Defined   | AN  | 12  | 244-255                          |                                             |
|      | Field          |     |     |                                  |                                             |
| 46   | Warehouse      | A   | 1   | 256                              | Y = Warehouse & Producer are the same       |
|      | Depositor      |     |     |                                  | entity                                      |
|      |                |     |     |                                  | N = Warehouse & Producer not the same       |
| 47   | Graded Deposit | A   | 1   | 257                              | Y = Graded at the request of the depositor; |
|      |                |     |     |                                  | N = No or Blank                             |
| 48   | EAD Subholder  | A   | 1   | 258                              | Y = Yes                                     |
|      |                |     |     |                                  | N = No or blank                             |
| 49   | CCC Document   | N   | 8   | 259-266                          | This date is supplied by CCC and is in      |
|      | Received Date  |     |     |                                  | reference to a loan document type           |
| 50   | Current Holder | A   | 1   | 267                              | M = Merchant                                |
|      | Type           |     |     |                                  | W = Warehouse                               |
|      |                |     |     |                                  | G = Gin                                     |
|      |                |     |     |                                  | Z = Coop                                    |
|      |                |     |     |                                  | P = Producer                                |
|      |                |     |     |                                  | C = Government                              |
|      |                |     |     |                                  | B = Bank                                    |
| 51   | Loan Transfer  | A   | 1   | 268                              | Y = Yes.  This bale was transferred while   |
|      |                |     |     |                                  | under loan.                                 |

### Table 15

| 52   | CCC Storage       | A   | 1   | 269                        | Does the 75-day storage limit apply?        |
|:-----|:------------------|:----|:----|:---------------------------|:--------------------------------------------|
|      | Limitation        |     |     |                            |                                             |
| 53   | Is Stored Outside | A   | 1   | 270                        | Y=Yes Issue Date is date moved outside;     |
|      |                   |     |     |                            | N=No, Bale is inside;                       |
|      |                   |     |     |                            | Blank=unknown                               |
| 54   | EWR Definition    | A   | 1   | 271                        | Reference to the EWR Definition for a       |
|      | ID                |     |     |                            | cotton receipt.                             |
| 55   | Type Class        | A   | 1   | 272                        | A = AMS Smith-Doxey; O = Other Classing;    |
|      |                   |     |     |                            | N = No Class available; C = Certified       |
| 56   | Date Class        | N   | 8   | 273-280                    | Classing office assigned – Date Classed.    |
| 57   | Delivery Point    | N   | 2   | 281-282  World Cotton Only |                                             |
| 58   | Classing Point    | N   | 2   | 283-284                    | Assigned by EWR, Inc.                       |
| 59   | Origination Code  | A   | 3   | 285-287                    | Country 3 letter ISO code where cotton      |
|      |                   |     |     |                            | was grown                                   |
| 60   | Filler            | A   | 1   | 288                        |                                             |
| 61   | Color Grade       | N   | 2   | 289-290                    | Classing office assigned                    |
| 62   | Staple            | N   | 2   | 291-292                    | Classing office assigned                    |
| 63   | Micronaire        | N   | 2   | 293-294                    | Classing office assigned                    |
| 64   | Strength          | N   | 3   | 295-297                    | Classing office assigned                    |
| 65   | World             | A   | 1   | 298                        | T = Tenderable                              |
|      | Tenderable        |     |     |                            | N = Non-Tenderable                          |
| 66   | Leaf Grade        | N   | 1   | 299                        | Classing office assigned                    |
| 67   | Extraneous        | N   | 2   | 300-301                    | Classing office assigned                    |
|      | Matter            |     |     |                            |                                             |
| 68   | Remarks           | N   | 2   | 302-303                    | Classing office assigned                    |
| 69   | HVI Color         | N   | 2   | 304-305                    | Classing office assigned                    |
| 70   | Color Quadrant    | N   | 1   | 306                        | Classing office assigned                    |
| 71   | HVI RD            | AN  | 3   | 307-309                    | Classing office assigned                    |
| 72   | HVI + B           | AN  | 3   | 310-312                    | Classing office assigned                    |
| 73   | Trash %           | N   | 2   | 313-314                    | Classing office assigned                    |
| 74   | Length            | N   | 3   | 315-317                    | Classing office assigned                    |
| 75   | Uniformity        | N   | 3   | 318-320                    |                                             |
| 76   | Upland/Pima       | A   | 1   | 321                        | Growth type; 1 = Upland; 2 = Pima           |
| 77   | Classing Type     | N   | 1   | 322                        | Reserved for EWR, Inc.                      |
| 78   | Filler            | N   | 5   | 323-327                    | Reserved for EWR, Inc.                      |
| 79   | Lot Number        | N   | 6   | 328-333                    | Lot number assigned by ICE                  |
| 80   | Weight Date       | N   | 8   |                            | 334-341  Weight date assigned by Warehouse; |
|      |                   |     |     |                            | MMDDYYYY                                    |
| 81   | USDA Tenderable   | AN  | 2   | 342-343                    | Is cert receipt tenderable on provider      |
|      |                   |     |     |                            | system? Blank=Tenderable, NT=Non-           |
|      |                   |     |     |                            | Tenderable, SD=Tenderable w Smith-Doxey     |
|      |                   |     |     |                            | classing                                    |

### Table 16

|    |               | Flag         |      |      |         |                                             |
|:---|:--------------|:-------------|:-----|:-----|:--------|:--------------------------------------------|
| T  | RAILER LAYOUT |              |      |      |         |                                             |
|    | Field         | Field Name   | Type | Size | Pos     | Description                                 |
|    | 1             | Record Type  | A    | 1    | 1       | T = Trailer Record                          |
|    | 2             | Holder ID    | AN   | 7    | 2-8     | The same as entered in the header record    |
|    | 3             | Batch Number | N    | 4    | 9-12    | The same as entered in the header record    |
|    | 4             | Record Count | N    | 9    | 13-21   | Control total record count of the number of |
|    |               |              |      |      |         | detail records in the batch                 |
|    | 5             | Filler       | A    | 9    | 22-30   | Reserved for EWR, Inc. use                  |
|    | 6             | Hash Total   | N    | 15   | 31-45   | Electronic Receipt number hash total        |
|    | 7             | Filler       | A    | 226  | 46-     | Blank 226 = short; 300 = long               |
|    |               |              |      |      | 271-345 | Reserved for EWR, Inc. use                  |
|    |               |              |      | 00   |         |                                             |

### Table 17

| T                                             | his is created when the warehouse sends up 07 or 36 to cancel receipts and they may include   |                |      |      |         |                                |
|:----------------------------------------------|:----------------------------------------------------------------------------------------------|:---------------|:-----|:-----|:--------|:-------------------------------|
| container/seal and Shipper Order Number/Mark. |                                                                                               |                |      |      |         |                                |
| H                                             | EADER LAYOUT FOR HD07                                                                         |                |      |      |         |                                |
|                                               | Field                                                                                         | Field Name     | Type | Size | Pos     | Description                    |
|                                               | 1                                                                                             | Record Type    | A    | 1    | 1       | H = Header Record              |
|                                               | 2                                                                                             | Holder ID      | AN   | 7    | 2-8     | Holder                         |
|                                               | 3                                                                                             | Batch Number   | N    | 4    | 9-12    | Batch number , holder supplied |
|                                               | 4                                                                                             | Type           | N    | 2    | 13-14   | 07=Cancel receipts             |
|                                               | 5                                                                                             | Filler         | A    | 1    | 15      | Reserved for EWR, Inc. use     |
|                                               | 6                                                                                             | Request Field  | AN   | 10   | 16-26   | The word “CONTAINER”           |
|                                               | 7                                                                                             | Filler         | A    | 1    | 27      | Reserved for EWR, Inc. use     |
|                                               | 8                                                                                             | Date           | N    | 8    | 28-35   | Date created                   |
|                                               | 9                                                                                             | Time           | N    | 6    | 36-41   | Time created                   |
|                                               | 10                                                                                            | Filler         | A    | 21   | 42-62   | Reserved for EWR, Inc. use     |
|                                               | 11                                                                                            | From Holder    | AN   | 7    | 63-69   | Blank                          |
|                                               | 12                                                                                            | From Name      | A    | 33   | 70-102  | Blank                          |
|                                               | 13                                                                                            | Receipt Count  | A    | 6    | 103-108 | Blank                          |
|                                               | 14                                                                                            | Filler         | A    | 2    | 109-110 | Reserved for EWR, Inc. use     |
|                                               | 15                                                                                            | Transaction ID | N    | 9    | 111-119 | Reserved for EWR, Inc. use     |
|                                               | 16                                                                                            | Filler         | A    | 1    | 120     | Reserved for EWR, Inc. use     |

### Table 18

| DETAIL LAYOUT FOR HD07   |              |      |      |         |                                           |
|:-------------------------|:-------------|:-----|:-----|:--------|:------------------------------------------|
| Field                    | Field Name   | Type | Size | Pos     | Description                               |
| 1                        | Record Type  | A    | 1    | 1       | D = Detail Record                         |
| 2                        | Warehouse    | N    | 6    | 2-7     | Warehouse code of the receipt             |
|                          | Code         |      |      |         |                                           |
| 3                        | Electronic   | N    | 7    | 8-14    | Electronic receipt number                 |
|                          | Receipt      |      |      |         |                                           |
|                          | Number       |      |      |         |                                           |
| 4                        | Crop Year    | N    | 4    | 15-18   | Crop year of the receipt                  |
| 5                        | Mark         | A    | 8    | 19-26   | Shipper Mark                              |
| 6                        | Order Number | A    | 10   | 27-36   | Shipper’s order number (Note 1)           |
| 7                        | Container    | A    | 25   | 37-61   |                                           |
| 8                        | Seal         | A    | 25   | 62-86   |                                           |
| 9                        | Requested    | N    | 8    | 87-94   | Optional – Supplied by Warehouse (Note 1) |
|                          | Load Date    |      |      |         |                                           |
| 10                       | Filler       | N    | 8    | 95-102  | Optional – Supplied by Warehouse (Note 1) |
| 11                       | Shipped Date | N    | 8    | 103-110 | Optional – Supplied by Warehouse (Note 1) |
| 12                       | Filler       | A    | 10   | 111-120 | Reserved for EWR, Inc. use                |

### Table 19

|    | 12                     | Filler       | A    | 10   | 111-120   | Reserved for EWR, Inc. use                         |
|:---|:-----------------------|:-------------|:-----|:-----|:----------|:---------------------------------------------------|
| T  | RAILER LAYOUT FOR HD07 |              |      |      |           |                                                    |
|    | Field                  | Field Name   | Type | Size | Pos       | Description                                        |
|    | 1                      | Record Type  | A    | 1    | 1         | T = Trailer record                                 |
|    | 2                      | Holder ID    | AN   | 7    | 2-8       |                                                    |
|    | 3                      | Batch Number | N    | 4    | 9-12      |                                                    |
|    | 4                      | Record Count | N    | 9    | 13-21     | Control total record count of the number of detail |
|    |                        |              |      |      |           | records in the batch                               |
|    | 5                      | Filler       | A    | 9    | 22-30     | Reserved for EWR, Inc. use                         |
|    | 6                      | Hash Total   | N    | 15   | 31-45     | Electronic Receipt number hash total               |
|    | 7                      | Filler       | A    | 74   | 46-120    | Reserved for EWR, Inc use                          |

### Table 20

| produced when warehouses send Batch Type 13 to the host computer.  The recipient of the batch will   |                       |                    |      |      |        |                                                |
|:-----------------------------------------------------------------------------------------------------|:----------------------|:-------------------|:-----|:-----|:-------|:-----------------------------------------------|
| be the current holder or subholder of the receipt when the change was made.                          |                       |                    |      |      |        |                                                |
| H                                                                                                    | EADER LAYOUT FOR HD13 |                    |      |      |        | Record Size = 120                              |
|                                                                                                      | Field                 | Field Name         | Type | Size | Pos    | Description                                    |
|                                                                                                      | 1                     | Record Type        | A    | 1    | 1      | H = Header Record                              |
|                                                                                                      | 2                     | Holder ID          | AN   | 7    | 2-8    | Holder ID who sent the batch.                  |
|                                                                                                      | 3                     | Batch Number       | N    | 4    | 9-12   | Batch number, holder supplied                  |
|                                                                                                      | 4                     | Batch Type         | N    | 2    | 13-14  | 13                                             |
|                                                                                                      | 5                     | Activity           | AN   | 11   | 15-25  |                                                |
|                                                                                                      | 6                     | Action Code        | AN   | 1    | 26     |                                                |
|                                                                                                      | 7                     | Filler             | A    | 1    | 27     | Reserved for EWR, Inc. use                     |
|                                                                                                      | 8                     | Batch Date         | N    | 8    | 28-35  | Date batch was created / updated; MMDDYYYY     |
|                                                                                                      | 9                     | Batch Time         | N    | 6    | 36-41  | Holder supplied batch time; HHMMSS             |
|                                                                                                      | 10                    | Filler             | AN   | 61   | 42-102 | Reserved for EWR, Inc. use                     |
|                                                                                                      | 11                    | Receipt Count      | N    | 6    | 103-   | Number of receipts in file                     |
|                                                                                                      |                       |                    |      |      | 108    |                                                |
|                                                                                                      | 12                    | Filler             | AN   | 12   | 80-120 | Reserved for EWR, Inc. use                     |
| D                                                                                                    | ETAIL LAYOUT FOR HD13 |                    |      |      |        |                                                |
|                                                                                                      | Field                 | Field Name         | Type | Size | Pos    | Description                                    |
|                                                                                                      | 1                     | Record Type        | A    | 1    | 1      | D=Detail Record                                |
|                                                                                                      | 2                     | Warehouse          | N    | 6    | 2-7    | Warehouse code of the receipt                  |
|                                                                                                      | 3                     | Electronic Receipt | N    | 7    | 8-14   | Receipt Number                                 |
|                                                                                                      |                       | Number             |      |      |        |                                                |
|                                                                                                      | 4                     | Crop Year          | N    | 4    | 15-18  | Crop year of the receipt                       |
|                                                                                                      | 5                     | Locator ID         | A    | 8    | 19-26  | Used to identify exact location of a bale in a |
|                                                                                                      |                       |                    |      |      |        | warehouse                                      |
|                                                                                                      | 6                     | Is Stored Outside  | N    | 1    | 27     | Is receipt stored outside – Y/N                |
|                                                                                                      | 7                     | Stored Inside Date | N    | 8    | 28-35  | Date moved inside                              |
|                                                                                                      | 8                     | Stored Outside     | N    | 8    | 36-43  | Date moved outside                             |
|                                                                                                      |                       | Date               |      |      |        |                                                |
|                                                                                                      | 9                     | Filler             | A    | 77   | 44-120 | Reserved for EWR, Inc. use                     |

### Table 21

| T   | RAILER LAYOUT FOR HD13   |              |      |      |        |                              |
|:----|:-------------------------|:-------------|:-----|:-----|:-------|:-----------------------------|
|     | Field                    | Field Name   | Type | Size | Pos    | Description                  |
|     | 1                        | Record Type  | A    | 1    | 1      | T=Trailer                    |
|     | 2                        | Holder ID    | AN   | 7    | 2-8    | Holder ID who sent the batch |
|     | 3                        | Batch Number | N    | 4    | 9-12   | Batch number                 |
|     | 4                        | Record Count | N    | 9    | 13-21  | Number of receipts           |
|     | 5                        | Filler       | A    | 9    | 22-30  | Reserved for EWR, Inc. use   |
|     | 6                        | Filler       | A    | 15   | 31-45  | Reserved for EWR, Inc. use   |
|     | 7                        | Filler       | A    | 75   | 46-120 | Reserved for EWR, Inc. use   |

### Table 22

| HD21, 30, 31 - Shipping Orders Instructions & Receipts                                                       |
|:-------------------------------------------------------------------------------------------------------------|
| B                                                                                                            |
| atch Type 21, 30 and 31 received from the host, is a batch which contains a shipping, staging or sample      |
| order instructions and a list of warehouse receipts on an order. This detail file is different than the full |
| detail data downloads of receipt information generated by most batch types, this file contains only the      |
| warehouse number, receipt number, crop year, and net weight (if entered by the shipper.)                     |
| O                                                                                                            |
| n shipping orders a bank lien will be downloaded at the beginning of the instruction list if the bales       |
| being shipped are held as collateral by a bank.                                                              |
| T                                                                                                            |
| here are some in the industry that are using the “Text Line” field to deliver special instructions to the    |
| warehouse.  The codes that are currently being used are in the document “Files Sent to Host" (Appendix       |
| B). EWR, Inc. does not use these codes within the host application.  They are recorded in this manual for    |
| documentation purposes only.                                                                                 |

### Table 23

| B). EWR, Inc. does not use these codes within the host application.  They are recorded in this manual for   |              |                |      |      |         |                                                   |
|:------------------------------------------------------------------------------------------------------------|:-------------|:---------------|:-----|:-----|:--------|:--------------------------------------------------|
| documentation purposes only.                                                                                |              |                |      |      |         |                                                   |
| H                                                                                                           | EADER LAYOUT |                |      |      |         | Record Size = 120                                 |
|                                                                                                             | Field        | Field Name     | Type | Size | Pos     | Description                                       |
|                                                                                                             | 1            | Record Type    | A    | 1    | 1       | H = Header Record                                 |
|                                                                                                             | 2            | Warehouse      | AN   | 7    | 2-8     | Holder ID of warehouse which store the cotton     |
|                                                                                                             |              | Holder ID      |      |      |         |                                                   |
|                                                                                                             | 3            | Batch Number   | N    | 4    | 9-12    | Batch number, holder supplied                     |
|                                                                                                             | 4            | Batch Type     | N    | 2    | 13-14   | 21 = Shipping Order 30=Sample, 31=Staging         |
|                                                                                                             | 5            | Batch Date     | N    | 8    | 15-22   | Holder supplied batch date; MMDDYYYY              |
|                                                                                                             | 6            | Batch Time     | N    | 6    | 23-28   | Time batch was created; HHMMSS                    |
|                                                                                                             | 7            | Warehouse      | N    | 6    | 29-34   | Code which identifies the warehouse where         |
|                                                                                                             |              | Code           |      |      |         | bales are stored                                  |
|                                                                                                             | 8            | Shipping Order | AN   | 10   | 35-44   | Shipper’s Order Number                            |
|                                                                                                             |              | Number         |      |      |         |                                                   |
|                                                                                                             | 9            | Shipper’s Mark | AN   | 8    | 45-52   | Shipper’s Mark                                    |
|                                                                                                             | 10           | Balance Flag   | A    | 1    | 53      | Y = Yes, net weights are included in the batch;   |
|                                                                                                             |              |                |      |      |         | N = No, net weights are not included in the batch |
|                                                                                                             |              |                |      |      |         | from the host                                     |
|                                                                                                             | 11           | Shipper Holder | AN   | 7    | 54-60   | Holder ID of Shipper, input when the Batch Type   |
|                                                                                                             |              | ID             |      |      |         | 21 was sent to the Host                           |
|                                                                                                             | 12           | Requested Load | N    | 8    | 61-68   | Shipper’s requested loading date for the          |
|                                                                                                             |              | Date           |      |      |         | shipment                                          |
|                                                                                                             | 13           | Shipper Name   | AN   | 30   | 69-98   | Name of Shipper; (May be truncated)               |
|                                                                                                             | 14           | Reserved       | A    | 3    | 99-101  | Reserved for future EWR, Inc. use.                |
|                                                                                                             | 15           | Decert Action  | A    | 1    | 102     | Blank,                                            |
|                                                                                                             |              |                |      |      |         | Y=Has been decertificated                         |
|                                                                                                             |              |                |      |      |         | T = Certificated Transfer (All receipts are cert) |
|                                                                                                             | 16           | Bale count     | N    | 6    | 103-108 | Bale Count                                        |
|                                                                                                             | 17           | Staging Order  | A    | 1    | 109     | Y = Yes; N = No – Batch 21 only                   |
|                                                                                                             |              | Sent           |      |      |         |                                                   |

### Table 24

|    | 4                                         | Text Line          | AN   | 76   | 5-80   | 76 Character Text Line                               |
|:---|:------------------------------------------|:-------------------|:-----|:-----|:-------|:-----------------------------------------------------|
|    | 5                                         | Filler             | A    | 40   | 81-120 | Reserved for EWR, Inc. use                           |
| D  | ETAIL LAYOUT – RECORD 2 (SO Receipt List) |                    |      |      |        |                                                      |
|    | Field                                     | Field Name         | Type | Size | Pos    | Description                                          |
|    | 1                                         | Record Type        | A    | 1    | 1      | D = Detail Record                                    |
|    | 2                                         | Detail Type        | A    | 1    | 2      | O = Shipping Order Receipts                          |
|    | 3                                         | Electronic Receipt | N    | 7    | 3-9    | Electronic Receipt Number for each bale to be        |
|    |                                           | Number             |      |      |        | shipped – Input by the shipper when the Batch        |
|    |                                           |                    |      |      |        | Type 21 was sent to the Host                         |
|    | 4                                         | Net Weight         | N    | 3    | 10-12  | Net weight of bale, only if Balance = Y in the       |
|    |                                           |                    |      |      |        | header                                               |
|    | 5                                         | Crop Year          | N    | 4    | 13-16  | Crop year of the receipt; YYYY                       |
|    | 6                                         | Gin Code           | N    | 5    | 17-21  | may be blank, if a world receipt                     |
|    | 7                                         | Gin Tag            | N    | 7    | 22-28  | may be blank, if a world receipt                     |
|    | 8                                         | Locator ID         | AN   | 8    | 29-36  | Used to identify exact location of a bale in a       |
|    |                                           |                    |      |      |        | warehouse                                            |
|    | 9                                         | IsUSDATenderable   | A    | 1    | 37     | If Bale is certificated , then is the receipt        |
|    |                                           |                    |      |      |        | tenderable  Y or N. If non-cert bale then field will |

### Table 25

|    | 18                                                                       | Block Receipts     | A    | 1    | 110     | Y=Yes; N=No -Receipts are block receipts             |
|:---|:-------------------------------------------------------------------------|:-------------------|:-----|:-----|:--------|:-----------------------------------------------------|
|    | 19                                                                       | Window Days        | N    | 2    | 111-112 | Days before or after to reschedule                   |
|    | 20                                                                       | Shipping Order     | N    | 8    | 113-120 | Unique number assigned by EWR, Inc                   |
|    |                                                                          | ID                 |      |      |         | Batch 21 only                                        |
| D  | ETAIL LAYOUT – RECORD 1 (SO Instructions – Maximum of 99 Detail Records) |                    |      |      |         |                                                      |
|    | Field                                                                    | Field Name         | Type | Size | Pos     | Description                                          |
|    | 1                                                                        | Record Type        | A    | 1    | 1       | D = Detail Record                                    |
|    | 2                                                                        | Detail Type        | A    | 1    | 2       | I = Shipping Instructions                            |
|    | 3                                                                        | Record Number      | N    | 2    | 3-4     | Record Number (1-99)                                 |
|    | 4                                                                        | Text Line          | AN   | 76   | 5-80    | 76 Character Text Line                               |
|    | 5                                                                        | Filler             | A    | 40   | 81-120  | Reserved for EWR, Inc. use                           |
| D  | ETAIL LAYOUT – RECORD 2 (SO Receipt List)                                |                    |      |      |         |                                                      |
|    | Field                                                                    | Field Name         | Type | Size | Pos     | Description                                          |
|    | 1                                                                        | Record Type        | A    | 1    | 1       | D = Detail Record                                    |
|    | 2                                                                        | Detail Type        | A    | 1    | 2       | O = Shipping Order Receipts                          |
|    | 3                                                                        | Electronic Receipt | N    | 7    | 3-9     | Electronic Receipt Number for each bale to be        |
|    |                                                                          | Number             |      |      |         | shipped – Input by the shipper when the Batch        |
|    |                                                                          |                    |      |      |         | Type 21 was sent to the Host                         |
|    | 4                                                                        | Net Weight         | N    | 3    | 10-12   | Net weight of bale, only if Balance = Y in the       |
|    |                                                                          |                    |      |      |         | header                                               |
|    | 5                                                                        | Crop Year          | N    | 4    | 13-16   | Crop year of the receipt; YYYY                       |
|    | 6                                                                        | Gin Code           | N    | 5    | 17-21   | may be blank, if a world receipt                     |
|    | 7                                                                        | Gin Tag            | N    | 7    | 22-28   | may be blank, if a world receipt                     |
|    | 8                                                                        | Locator ID         | AN   | 8    | 29-36   | Used to identify exact location of a bale in a       |
|    |                                                                          |                    |      |      |         | warehouse                                            |
|    | 9                                                                        | IsUSDATenderable   | A    | 1    | 37      | If Bale is certificated , then is the receipt        |
|    |                                                                          |                    |      |      |         | tenderable  Y or N. If non-cert bale then field will |
|    |                                                                          |                    |      |      |         | be blank.                                            |
|    |                                                                          |                    |      |      |         | A decert bale SHOULD be N.                           |
|    | 10                                                                       | Receipt Type       | A    | 1    | 38      | R = Regular                                          |
|    |                                                                          |                    |      |      |         | C= Certificated #2                                   |
|    |                                                                          |                    |      |      |         | D = Decertificate #2 USA receipt                     |
|    |                                                                          |                    |      |      |         | W = World Single Certificated                        |
|    |                                                                          |                    |      |      |         | T = World Container                                  |
|    |                                                                          |                    |      |      |         | X= World Decertificated Receipt                      |
|    | 11                                                                       | World Tenderable   | A    | 1    | 39      | T = Tenderable under ICE world contract              |
|    |                                                                          |                    |      |      |         | N = Non-Tenderable under ICE world contract          |
|    | 12                                                                       | World Gin Tag      | AN   | 12   | 40-51   | may be blank, if a non-world receipt                 |
|    | 13                                                                       | Filler             | AN   | 69   | 52-     | Reserved for EWR, Inc. use                           |
|    |                                                                          |                    |      |      | 120     |                                                      |

### Table 26

| TRAILER LAYOUT   |              |      |      |       |                                                     |
|:-----------------|:-------------|:-----|:-----|:------|:----------------------------------------------------|
| Field            | Field Name   | Type | Size | Pos   | Description                                         |
| 1                | Record Type  | A    | 1    | 1     | T = Trailer Record                                  |
| 2                | Holder ID    | AN   | 7    | 2-8   | The same as entered in the header record            |
|                  |              |      |      |       | (Warehouse Holder ID)                               |
| 3                | Batch Number | N    | 4    | 9-12  | The same as entered in the header record            |
| 4                | Record Count | N    | 9    | 13-21 | Control total record count of detail records in the |
|                  |              |      |      |       | batch                                               |
| 5                | Total Weight | N    | 9    | 22-30 | Total net weight of bales in the shipping order     |
| 6                | Hash Total   | N    | 15   | 31-45 | Electronic receipt number hash total                |
| 7                | Filler       | A    | 75   | 46-   | Reserved for EWR, Inc. use                          |
|                  |              |      |      | 120   |                                                     |

### Table 27

| HD23 - Shipping Order Update                                                                                 |
|:-------------------------------------------------------------------------------------------------------------|
| This batch is a download of shipment information that has processed/updated when a batch 23 is               |
| received. The recipient of the batch should verify the date field in the detail record against their records |
| for verification.                                                                                            |
| T                                                                                                            |
| he shipper will receive the warehouse schedule date in the detail date field, while the warehouse will       |
| receive the requested load date.                                                                             |

### Table 28

| T                                | he shipper will receive the warehouse schedule date in the detail date field, while the warehouse will   |                |      |      |        |                                            |
|:---------------------------------|:---------------------------------------------------------------------------------------------------------|:---------------|:-----|:-----|:-------|:-------------------------------------------|
| receive the requested load date. |                                                                                                          |                |      |      |        |                                            |
| H                                | EADER LAYOUT FOR HD23                                                                                    |                |      |      |        |                                            |
|                                  | Field                                                                                                    | Field Name     | Type | Size | Pos    | Description                                |
|                                  | 1                                                                                                        | Record Type    | A    | 1    | 1      | H=Header record                            |
|                                  | 2                                                                                                        | Holder ID      | AN   | 7    | 2-8    | Receiving holder ID                        |
|                                  | 3                                                                                                        | Batch Number   | N    | 4    | 9-12   | Batch number, holder supplied              |
|                                  | 4                                                                                                        | Type           | N    | 2    | 13-14  | 23= shipment update                        |
|                                  | 5                                                                                                        | Filler         | A    | 13   | 15-27  | Reserved for EWR, Inc. use                 |
|                                  | 8                                                                                                        | Date           | N    | 8    | 28-35  | Date created                               |
|                                  | 9                                                                                                        | Time           | N    | 6    | 36-41  | Time created                               |
|                                  | 10                                                                                                       | Filler         | A    | 21   | 42-62  | Reserved for EWR, Inc. use                 |
|                                  | 11                                                                                                       | From Holder ID | AN   | 7    | 63-69  | From EWR holder number                     |
|                                  | 12                                                                                                       | From Name      | A    | 40   | 70-109 | From holder name                           |
|                                  | 13                                                                                                       | Filler         | A    | 11   | 110-   | Reserved for EWR, Inc. use                 |
|                                  |                                                                                                          |                |      |      | 120    |                                            |
| DETAIL LAYOUT FOR HD23           |                                                                                                          |                |      |      |        |                                            |
|                                  | Field                                                                                                    | Field Name     | Type | Size | Pos    | Description                                |
|                                  | 1                                                                                                        | Record Type    | A    | 1    | 1      | D=Detail record                            |
|                                  | 2                                                                                                        | Warehouse      | N    | 6    | 2-7    | Warehouse code for the order               |
|                                  |                                                                                                          | Code           |      |      |        |                                            |
|                                  | 3                                                                                                        | Action         | A    | 1    | 8-8    | Reserved for EWR use                       |
|                                  | 4                                                                                                        | Bales          | N    | 5    | 9-13   | Number of bales (Supplied by sender of 23) |
|                                  | 5                                                                                                        | Mark           | A    | 8    | 14-21  |                                            |
|                                  | 6                                                                                                        | Order Number   | A    | 10   | 22-31  | Shippers order number                      |
|                                  | 7                                                                                                        | Date           | N    | 8    | 32-39  | Requested load date or Schedule date       |
|                                  | 8                                                                                                        | Shipper Holder | AN   | 7    | 40-46  | Merchant holder number                     |
|                                  |                                                                                                          | ID             |      |      |        |                                            |
|                                  | 9                                                                                                        | EWR ID         | N    | 8    | 47-54  | EWR shipping order ID (Optional)           |
|                                  | 10                                                                                                       | Window Days    | N    | 8    | 55-62  | Days before or after to reschedule         |
|                                  | 11                                                                                                       | Filler         | N    | 58   | 63-120 | Reserved for EWR use                       |

### Table 29

| TRAILER LAYOUT FOR HD23   |              |      |      |        |                                             |
|:--------------------------|:-------------|:-----|:-----|:-------|:--------------------------------------------|
| Field                     | Field Name   | Type | Size | Pos    | Description                                 |
| 1                         | Record Type  | A    | 1    | 1      | T=Trailer record                            |
| 2                         | Holder ID    | AN   | 7    | 2-8    |                                             |
| 3                         | Batch Number | N    | 4    | 9-12   |                                             |
| 4                         | Record Count | N    | 9    | 13-21  | Control total record count of the number of |
|                           |              |      |      |        | detail records in the batch                 |
| 5                         | Filler       | A    | 99   | 22-120 |                                             |

### Table 30

| HD24 - Warehouse Invoice                                                                               |
|:-------------------------------------------------------------------------------------------------------|
| T                                                                                                      |
| he batch 24 will be provided to the shipper (merchant) in XML format.  All of the data will be under a |
| node called “WarehouseInvoice”. This data is “passed” thru by EWR, Inc. If it is incomplete or wrong,  |
| the warehouse should be contacted.                                                                     |
| A                                                                                                      |
| ll files created by EWR will follow the usual filename convention (prefixed with HD24) with an .XML    |
| (period XML) extension and will be stored in the usual holders NOTZIP FTP mailbox. There will be a     |
| zipped (compressed) copy of this file with the .zip extension in the ZIP FTP Mailbox. For example:     |
| HD24.1234.20080801.101022.83838A.XML                                                                   |

### Table 31

| ?xml version="1.0" encoding="utf-8" ?>   |
|:-----------------------------------------|
| <WarehouseInvoice ">                     |
| <Originator>                             |
| <Address>                                |
| <AddressType>Shipping</AddressType>      |
| <Address1>P O Box 1</Address1>           |
| <Address2 />                             |
| <City>Memphis</City>                     |
| <State>TN</State>                        |
| <CountryCode>US</CountryCode>            |
| <PostalCode>79336</PostalCode>           |
| </Address>                               |
| <PhoneNumber>                            |
| <PhoneNumberType>Main</PhoneNumberType>  |
| <PhoneNumber>901-396-3243</PhoneNumber>  |
| </PhoneNumber>                           |

### Table 32

| <Instructions>Payable upon receipt of invoice. </Instructions>   |
|:-----------------------------------------------------------------|
| <Address>                                                        |
| <AddressType>Billing</AddressType>                               |
| <Address1>BOX 443</Address1>                                     |
| <Address2 />                                                     |
| <City>MEMPHIS</City>                                             |
| <State>TN</State>                                                |
| <CountryCode>US</CountryCode>                                    |
| <PostalCode>381010443</PostalCode>                               |
| </Address>                                                       |

### Table 33

| <Item>                                                     |      |
|:-----------------------------------------------------------|:-----|
| <Description>Receiving</Description>                       |      |
| <Quantity>88</Quantity>                                    |      |
| <UnitCost>3.25</UnitCost>                                  |      |
| <Total>286</Total>                                         |      |
| </Item>                                                    |      |
| </Charge>                                                  |      |
| <Charge>                                                   |      |
| <Item>                                                     |      |
| <Description>Loading Other</Description>                   |      |
| <Quantity>88</Quantity>                                    |      |
| <UnitCost>5.25</UnitCost>                                  |      |
| <Total>462</Total>                                         |      |
| </Item>                                                    |      |
| </Charge>                                                  |      |
| <Number>247181</Number>                                    |      |
| <Date>2008-04-08</Date>                                    |      |
| <Mark>CRNZ</Mark>                                          |      |
| </Shipment>                                                |      |
| <FilePath>C:\FileImports\WebServices\1.8733.xml</FilePath> |      |
| </WarehouseInvoice>                                        |      |
|                                                            | 3-21 |

### Table 34

| HD25 – Phytosanitary Warehouse XML Delivery                                                               |
|:----------------------------------------------------------------------------------------------------------|
| T                                                                                                         |
| he batch 25 will be provided to the warehouse in XML format.  All of the data will be under a node        |
| called “PhytosanitaryRequests”. This data is “passed” thru by EWR, Inc. If it is incomplete or wrong, the |
| merchant or shipper should be contacted.                                                                  |
| A                                                                                                         |
| ll files created by EWR will follow the usual filename convention (prefixed with HD25) with an .XML       |
| (period XML) extension and will be stored in the usual holders NOTZIP FTP mailbox. There will be a        |
| zipped (compressed) copy of this file with the .zip extension in the ZIP FTP Mailbox. For example:        |
| HD25.1234.20080801.101022.83838A.XML                                                                      |
| E                                                                                                         |
| xample of a file received. NOTE: There may be more fields included than shown.                            |
| <?xml version="1.0" encoding="us-ascii"?>                                                                 |
| <PhytosanitaryRequests xmlns="EWRInc">                                                                    |
| <ContractNumber>S04935.A01</ContractNumber>                                                               |
| <Exporter>                                                                                                |
| <Line1>COTTON LLC</Line1>                                                                                 |
| <Line2>55 GOODLETT FARMS PARKWAY</Line2>                                                                  |
| <Line3>PO BOX 54</Line3>                                                                                  |
| <Line4>CORDOVA, TN 38446 US</Line4>                                                                       |
| <AgentSignature>Amy</AgentSignature>                                                                      |
| <AgentSignatureDate>2018-05-26</AgentSignatureDate>                                                       |
| <EWRShipperHolderID>M999999   </EWRShipperHolderID>                                                       |
| </Exporter>                                                                                               |
| <Applicant>                                                                                               |
| <Line1>INTERNATIONAL LOGISTIC</Line1>                                                                     |
| <Line2>75 GOODLETT FARMS PARKWAY</Line2>                                                                  |
| <Line3 />                                                                                                 |
| <Line4>CORDOVA, TN 38016 US</Line4>                                                                       |
| <PhoneNumber>(9999) 284-5000</PhoneNumber>                                                                |
| <EWRFreightForwarderHolderID>F000001</EWRFreightForwarderHolderID>                                        |
| </Applicant>                                                                                              |
| <ForeignConsignee>                                                                                        |
| <Line1>LAX        Los Angeles</Line1>                                                                     |
| <Line2>US</Line2>                                                                                         |
| </ForeignConsignee>                                                                                       |
| <DateOfDeparture>2019-05-26</DateOfDeparture>                                                             |
| <PortOfExport>LAX        Los Angeles US</PortOfExport>                                                    |
| <ConveyanceMeans>Ocean Vessel</ConveyanceMeans>                                                           |
| <PortOfEntry>SRG        SEMARANG ID</PortOfEntry>                                                         |
| <Warehouse>                                                                                               |
| <EWRTrackingNumber>34739</EWRTrackingNumber>                                                              |
| <AcceptsElectronicPhytosanitary>true</AcceptsElectronicPhytosanitary>                                     |
| <Line1>COMPRESS #6</Line1>                                                                                |
| <Line2>2590 CR 95</Line2>                                                                                 |
| <Line3>PLAINVIEW, TX 79072 US</Line3>                                                                     |
| <Code>911525</Code>                                                                                       |
| <EWRAction>NEW</EWRAction>                                                                                |
| <ProduceQuantity>86</ProduceQuantity>                                                                     |
| <QuantityAndName>                                                                                         |
| <Line1>100 Bales Cotton</Line1>                                                                           |
| <Line2>Gossypium SPP</Line2>                                                                              |
| </QuantityAndName>                                                                                        |
| 3-22                                                                                                      |

### Table 35

| <NumberAndDescription>                               |
|:-----------------------------------------------------|
| <Line1>100 Bales</Line1>                             |
| </NumberAndDescription>                              |
| <CertifiedOrigin>                                    |
| <Line1>USA</Line1>                                   |
| <Line2>ONCE INSPECTED PLEASE EMAIL APPLICANT</Line2> |
| <Line3>Team@group.com</Line3>                        |
| </CertifiedOrigin>                                   |
| <Shipment>                                           |
| <Mark>28B142</Mark>                                  |
| <OrderNumber>1758290</OrderNumber>                   |
| <Bales>86</Bales>                                    |
| </Shipment>                                          |
| <Shipment>                                           |
| <Mark>8B42</Mark>                                    |
| <OrderNumber>58290</OrderNumber>                     |
| <Bales>14</Bales>                                    |
| </Shipment>                                          |
| </Warehouse>                                         |
| </PhytosanitaryRequests>                             |

### Table 36

| HD25 – Phytosanitary Forwarder XML Delivery                                                               |
|:----------------------------------------------------------------------------------------------------------|
| T                                                                                                         |
| he batch 25 will be provided to the forwarder in XML format.  All of the data will be under a node        |
| called “PhytosanitaryRequests”. This data is “passed” thru by EWR, Inc. If it is incomplete or wrong, the |
| merchant or shipper should be contacted.                                                                  |
| A                                                                                                         |
| ll files created by EWR will follow the usual filename convention (prefixed with HD25) with an .XML       |
| (period XML) extension and will be stored in the usual holders NOTZIP FTP mailbox. There will be a        |
| zipped (compressed) copy of this file with the .zip extension in the ZIP FTP Mailbox. For example:        |
| HD25.1234.20080801.101022.83838A.XML                                                                      |
| E                                                                                                         |
| xample of a file received. NOTE: There may be more fields included than shown.                            |
| <?xml version="1.0" encoding="us-ascii"?>                                                                 |
| <PhytosanitaryRequests xmlns="EWRInc">                                                                    |
| <ContractNumber>S05261.A04</ContractNumber>                                                               |
| <Exporter>                                                                                                |
| <Line1>ABC Merchant</Line1>                                                                               |
| <Line2>255 GOOD FARMS PARKWAY</Line2>                                                                     |
| <Line3>PO BOX 54</Line3>                                                                                  |
| <Line4>CORDOVA, TN 38016 US</Line4>                                                                       |
| <AgentSignature>TOm</AgentSignature>                                                                      |
| <AgentSignatureDate>2018-04-24</AgentSignatureDate>                                                       |
| <EWRShipperHolderID>M381180   </EWRShipperHolderID>                                                       |
| </Exporter>                                                                                               |
| <Applicant>                                                                                               |
| <Line1>BIG LOGISTIC</Line1>                                                                               |
| <Line2>75 FARMS PARKWAY</Line2>                                                                           |
| <Line3 />                                                                                                 |
| <Line4>CORDOVA, TN 38016 US</Line4>                                                                       |
| <PhoneNumber>(999) 999-5000</PhoneNumber>                                                                 |
| <EWRFreightForwarderHolderID>F000001</EWRFreightForwarderHolderID>                                        |
| </Applicant>                                                                                              |
| <ForeignConsignee>                                                                                        |
| <Line1>SAV        Savannah</Line1>                                                                        |
| <Line2>US</Line2>                                                                                         |
| </ForeignConsignee>                                                                                       |
| <DateOfDeparture>2018-06-03</DateOfDeparture>                                                             |
| <PortOfExport>SAV        Savannah US</PortOfExport>                                                       |
| <ConveyanceMeans>Ocean Vessel</ConveyanceMeans>                                                           |
| <PortOfEntry>QCT        PORT QASIM PK</PortOfEntry>                                                       |
| <trailer RecordCount="1" />                                                                               |
| <Warehouse>                                                                                               |
| <EWRTrackingNumber>396</EWRTrackingNumber>                                                                |
| <AcceptsElectronicPhytosanitary>false</AcceptsElectronicPhytosanitary>                                    |
| <Line1>DISTRIBUTION CENTER</Line1>                                                                        |
| <Line2>101 South Street</Line2>                                                                           |
| <Line3>WEST MEMPHIS, AR 72301 US</Line3>                                                                  |
| <Code>167035</Code>                                                                                       |
| <EWRAction>NEW</EWRAction>                                                                                |
| <ProduceQuantity>88</ProduceQuantity>                                                                     |
| <QuantityAndName>                                                                                         |
| <Line1>88 Bales Cotton</Line1>                                                                            |
| <Line2>Gossypium SPP</Line2>                                                                              |
| 3-24                                                                                                      |

### Table 37

| </QuantityAndName>                                   |
|:-----------------------------------------------------|
| <NumberAndDescription>                               |
| <Line1>88 Bales</Line1>                              |
| </NumberAndDescription>                              |
| <CertifiedOrigin>                                    |
| <Line1>USA</Line1>                                   |
| <Line2>ONCE INSPECTED PLEASE EMAIL APPLICANT</Line2> |
| <Line3>Email group.com</Line3>                       |
| </CertifiedOrigin>                                   |
| <Shipment>                                           |
| <Mark>6Y353</Mark>                                   |
| <OrderNumber>1759522</OrderNumber>                   |
| <Bales>88</Bales>                                    |
| </Shipment>                                          |
| </Warehouse>                                         |
| </PhytosanitaryRequests>                             |

### Table 38

| N                                                                                                       | ote: Batch Types 09 & 14, without a Disposition Holder, will not produce a “Delivery” of detail due to   |                   |      |      |         |                                                  |
|:--------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|:------------------|:-----|:-----|:--------|:-------------------------------------------------|
| the fact that the entire batch rejects if one error is detected in the original batch sent to the host. |                                                                                                          |                   |      |      |         |                                                  |
| H                                                                                                       | EADER LAYOUT FOR HD Block                                                                                |                   |      |      |         | Record Size = 271                                |
|                                                                                                         | Field                                                                                                    | Field Name        | Type | Size | Pos     | Description                                      |
|                                                                                                         | 1                                                                                                        | Record Type       | A    | 1    | 1       | H = Header Record                                |
|                                                                                                         | 2                                                                                                        | Holder ID         | AN   | 7    | 2-8     | Holder ID - user receiving download              |
|                                                                                                         | 3                                                                                                        | Batch Number      | N    | 4    | 9-12    | Batch assigned by sender                         |
|                                                                                                         | 4                                                                                                        | Batch Type        | N    | 2    | 13-14   | 41 = Detail Block Receipt Data received          |
|                                                                                                         | 5                                                                                                        | Request Flag      | A    | 1    | 15      | Blank                                            |
|                                                                                                         | 6                                                                                                        | Request Field     | AN   | 11   | 16-26   | Batch 50 only = Action Code; Batch 15 change     |
|                                                                                                         |                                                                                                          |                   |      |      |         | Holder ID of person making change otherwise      |
|                                                                                                         |                                                                                                          |                   |      |      |         | blank                                            |
|                                                                                                         | 7                                                                                                        | Holder Selection  | A    | 1    | 27      | Blank                                            |
|                                                                                                         | 8                                                                                                        | Batch Date        | N    | 8    | 28-35   | Holder supplied batch date; MMDDYYYY             |
|                                                                                                         | 9                                                                                                        | Batch Time        | N    | 6    | 36-41   | Holder supplied batch time; HHMMSS               |
|                                                                                                         | 10                                                                                                       | Draft Number      | AN   | 10   | 42-51   | Bank Draft Number - if delivered via bank draft  |
|                                                                                                         | 11                                                                                                       | Draft Amount      | N    | 10   | 52-61   | Draft Amount - if delivered via bank draft       |
|                                                                                                         | 12                                                                                                       | Filler            | A    | 1    | 62      | Reserved for EWR, Inc. use                       |
|                                                                                                         | 13                                                                                                       | From Holder       | AN   | 7    | 63-69   | Holder who transferred the data.                 |
|                                                                                                         | 14                                                                                                       | Filler            | A    | 1    | 70      | Reserved for EWR, Inc. use                       |
|                                                                                                         | 15                                                                                                       | Originating Batch | N    | 2    | 71-72   | Batch type initiating this download (08, 09, 14, |
|                                                                                                         |                                                                                                          | Type              |      |      |         | 15, 50, 51, 52)                                  |
|                                                                                                         | 16                                                                                                       | Holder Type       | A    | 15   | 73-87   | Output of holder selection type                  |
|                                                                                                         | 17                                                                                                       | Holder Name       | A    | 40   | 88-127  | Name of holder                                   |
|                                                                                                         | 18                                                                                                       | Criteria Type     | A    | 15   | 128-142 | Selection Criteria                               |
|                                                                                                         | 19                                                                                                       | Criteria          | A    | 37   | 143-179 |                                                  |
|                                                                                                         |                                                                                                          | Description       |      |      |         |                                                  |
|                                                                                                         | 20                                                                                                       | Filler            | A    | 1    | 180     | Reserved for EWR, Inc. use                       |
|                                                                                                         | 21                                                                                                       | Block Receipts    | A    | 1    | 181     | Always Y                                         |
|                                                                                                         | 22                                                                                                       | Filler            | A    | 1    | 182     | Reserved for EWR, Inc. use                       |
|                                                                                                         | 23                                                                                                       | EWR Transaction   | N    | 9    | 183-191 | Assigned by EWR, Inc.                            |
|                                                                                                         | 24                                                                                                       | Receipt Count     | N    | 6    | 192-197 |                                                  |
|                                                                                                         | 25                                                                                                       | Filler            | A    | 74   | 198-271 | Reserved for EWR, Inc. use                       |

### Table 39

| DETAIL LAYOUT FOR HD Block   |                    |      |      |         |                                                 |
|:-----------------------------|:-------------------|:-----|:-----|:--------|:------------------------------------------------|
| Field                        | Field Name         | Type | Size | Pos     | Description                                     |
| 1                            | Record Type        | A    | 1    | 1       | D = Detail Record                               |
| 2                            | Detail Type        | A    | 1    | 2       | R = Regular Block                               |
| 3                            | Warehouse Code     | N    | 6    | 3-8     | Warehouse Code of the Block                     |
| 4                            | Electronic Receipt | N    | 7    | 9-15    | Electronic Block Number                         |
|                              | Number             |      |      |         |                                                 |
| 5                            | Crop Year          | N    | 4    | 16-19   | Crop Year of the Block                          |
| 6                            | Issue Date         | N    | 8    | 20-27   | Date entered by the warehouse, not assigned     |
|                              |                    |      |      |         | by EWR.  Storage date of the bale -             |
|                              |                    |      |      |         | MMDDYYYY                                        |
| 7                            | Receiving Fee      | N    | 4    | 28-31   | 9999 (2 decimal places); Warehouse defined      |
|                              |                    |      |      |         | charge                                          |
|                              |                    |      |      |         | Example 0250 = $2.50 - Charge is per bale       |
|                              |                    |      |      |         | (US currency)                                   |
| 8                            | Storage Fee        | N    | 4    | 32-35   | 9999 (2 decimal places); Warehouse defined      |
|                              |                    |      |      |         | charge                                          |
|                              |                    |      |      |         | Example 0250 - $2.50.  If storage Charge        |
|                              |                    |      |      |         | Frequency is daily, the entry will display as   |
|                              |                    |      |      |         | cents/day, e.g. 0950 =9.50 cents per day -      |
|                              |                    |      |      |         | Charge is per bale. (US currency)               |
| 9                            | Storage Charge     | A    | 1    | 36      | D=Daily; C=Calendar Months; S=Actual            |
|                              | Frequency          |      |      |         | Months (same day); F=Actual Months              |
|                              |                    |      |      |         | (following day); M=Monthly (legacy support)     |
|                              |                    |      |      |         | See Appendix J – Files Sent To EWR              |
| 10                           | Receiving Paid     | A    | 1    | 37      | Y = Receiving paid or waived                    |
|                              |                    |      |      |         | N = not paid or waived                          |
| 11                           | Loading Paid       | A    | 1    | 38      | Y = Paid   N = Not Paid                         |
| 12                           | Classing Paid      | A    | 1    | 39      | Y = Paid   N = Not Paid                         |
| 13                           | Storage Paid       | N    | 8    | 40-47   | Storage paid through date; MMDDYYYY             |
|                              | Through            |      |      |         | Last date that storage charges against the bale |
|                              |                    |      |      |         | were paid                                       |
| 14                           | Mark               | AN   | 8    | 48-55   | Shipper assigned mark                           |
| 15                           | Purchase Order     | AN   | 10   | 56-65   | Purchase Order Number assigned by seller        |
|                              | Number             |      |      |         |                                                 |
| 16                           | Invoice Number     | AN   | 10   | 66-75   | Invoice Number assigned by seller               |
| 17                           | Received From      | AN   | 30   | 76-105  | Received from name                              |
| 18                           | Licensing          | AN   | 2    | 106-107 | Federal Licensing                               |
|                              |                    |      |      |         |  US                                             |

### Table 40

| 20   | Electronic Receipt   | A    | 1   | 116     | O = Open                                     |
|:-----|:---------------------|:-----|:----|:--------|:---------------------------------------------|
|      | Status               |      |     |         | C = Cancel                                   |
| 21   | Electronic Receipt   | A    | 1   | 117     | E = Electronic                               |
|      | Flag                 |      |     |         | P = Paper                                    |
| 22   | Receipt Type         | A    | 1   | 118     | G = Negotiable   O = Non-Negotiable          |
| 23   | Paper Receipt        | N    | 7   | 119-125 | Paper Receipt Number assigned by warehouse   |
|      | Number               |      |     |         | (if any)                                     |
| 24   | User Defined         | AN   | 12  | 126-137 | 12 bytes used to enter any optional          |
|      | Field                |      |     |         | information                                  |
| 25   | Warehouse/           | A    | 1   | 138     | Y = Warehouse & Producer are the same        |
|      | Depositor            |      |     |         | entity                                       |
|      |                      |      |     |         | N = Warehouse & Producer not the same        |
| 26   | Graded/Deposit       | A    | 1   | 139     | Y = Graded at the request of the depositor   |
|      |                      |      |     |         | N = Not graded at request of the depositor   |
| 27   | Bale Count           | N    | 5   | 140-144 | Number of bales in block                     |
| 28   | Lot ID               | AN   | 12  | 145-156 | Lot identifier from the depositor.  Often    |
|      |                      |      |     |         | equivalent to the Mark                       |
| 29   | Total Net Weight     | N    | 6   | 157-162 | Total Net Weight of bales in block           |
| 30   | Total Tare Weight    | N    | 4   | 163-166 | Total Tare Weight of bales in block          |
| 31   | Control Number       | A/AN | 10  | 167-176 | A 10-character field used for control number |
| 32   | Draft Number         | A/N  | 10  | 177-186 | Bank Draft Number assigned by seller         |
| 33   | Holder Type          | A    | 1   | 187     | M = Merchant                                 |
|      |                      |      |     |         | W = Warehouse                                |
|      |                      |      |     |         | G = Gin                                      |
|      |                      |      |     |         | Z = Coop                                     |
|      |                      |      |     |         | P = Producer                                 |
|      |                      |      |     |         | C = Government                               |
|      |                      |      |     |         | B = Bank                                     |
| 34   | Filler               | A    | 84  | 188-271 | Reserved for EWR, Inc. use                   |

### Table 41

| DETAIL- BALE DATA This record is not used for non-negotiable block receipts.  For negotiable block   |                            |               |      |      |        |                                                 |
|:-----------------------------------------------------------------------------------------------------|:---------------------------|:--------------|:-----|:-----|:-------|:------------------------------------------------|
| receipts, there will be one record for each bale in the block receipt.                               |                            |               |      |      |        |                                                 |
|                                                                                                      | Field                      | Field Name    | Type | Size | Pos    | Description                                     |
|                                                                                                      | 1                          | Record Type   | A    | 1    | 1      | D = Detail Record                               |
|                                                                                                      | 2                          | Detail Type   | A    | 1    | 2      | B = Bale                                        |
|                                                                                                      | 3                          | Warehouse     | N    | 6    | 3-8    | Warehouse Code of the Block                     |
|                                                                                                      |                            | Code          |      |      |        |                                                 |
|                                                                                                      | 4                          | Block Receipt | N    | 7    | 9-15   | Electronic Block Number                         |
|                                                                                                      |                            | Number        |      |      |        |                                                 |
|                                                                                                      | 5                          | Crop Year     | N    | 4    | 16-19  | Crop year in which the cotton was grown: YYYY   |
|                                                                                                      | 6                          | Tag ID        | N    | 7    | 20-26  | The tag number that is assigned by warehouse to |
|                                                                                                      |                            |               |      |      |        | identify each bale in the entire block          |
|                                                                                                      | 7                          | Net Weight    | N    | 3    | 27-29  | Gross weight of bale minus tare weight.  User   |
|                                                                                                      |                            |               |      |      |        | enters appropriate amount                       |
|                                                                                                      | 8                          | Tare Weight   | N    | 2    | 30-31  | Represents the number pounds subtracted from    |
|                                                                                                      |                            |               |      |      |        | the gross weight to compensate for bagging and  |
|                                                                                                      |                            |               |      |      |        | ties on the bale                                |
|                                                                                                      | 9                          | Gin Code      | N    | 5    | 32-36  | USDA assigned code which identifies the site    |
|                                                                                                      |                            |               |      |      |        | where the cotton was ginned                     |
|                                                                                                      | 10                         | Gin Tag       | N    | 7    | 37-43  | Tag number assigned by gin                      |
|                                                                                                      | 11                         | Filler        |      | 228  | 44-271 | Reserved for EWR, Inc. use                      |
| T                                                                                                    | RAILER LAYOUT FOR HD Block |               |      |      |        |                                                 |
|                                                                                                      | Field                      | Field Name    | Type | Size | Pos    | Description                                     |
|                                                                                                      | 1                          | Record Type   | A    | 1    | 1      | T = Trailer Record                              |
|                                                                                                      | 2                          | Holder ID     | AN   | 7    | 2-8    | The same as entered in the header record        |
|                                                                                                      | 3                          | Batch         | N    | 4    | 9-12   | The same as entered in the header record        |
|                                                                                                      |                            | Number        |      |      |        |                                                 |
|                                                                                                      | 4                          | Record Count  | N    | 9    | 13-21  | Control total record count of the number of     |
|                                                                                                      |                            |               |      |      |        | detail records in the batch                     |
|                                                                                                      | 5                          | Filler        | A    | 9    | 22-30  | Reserved for EWR, Inc. use                      |
|                                                                                                      | 6                          | Hash Total    | N    | 15   | 31-45  | Electronic Block number hash total              |
|                                                                                                      | 7                          | Filler        |      | 75   | 46-271 | Reserved for EWR, Inc. use                      |

### Table 42

| HD43 - Warehouse Loan Status Delivery                                                                      |
|:-----------------------------------------------------------------------------------------------------------|
| T                                                                                                          |
| his batch is a download of receipt information that has been placed under loan or redeemed by CCC for      |
| a specific warehouse. It is produced when CCC sends a “CL” file (put under loan) or a “CR” file when it is |
| released. The recipient of the batch will be the issuing warehouse that has chosen to receive this file    |
| (Holder Preferences). The warehouse will also be billed on a per receipt basis according to the latest     |
| tariff.                                                                                                    |

### Table 43

| (Holder Preferences). The warehouse will also be billed on a per receipt basis according to the latest   |                        |      |      |         |                                      |
|:---------------------------------------------------------------------------------------------------------|:-----------------------|:-----|:-----|:--------|:-------------------------------------|
| tariff.                                                                                                  |                        |      |      |         |                                      |
|                                                                                                          | HEADER LAYOUT FOR HD43 |      |      |         | Record Size = 120                    |
| Field                                                                                                    | Field Name             | Type | Size | Pos     | Description                          |
| 1                                                                                                        | Record Type            | A    | 1    | 1       | H=Header record                      |
| 2                                                                                                        | Holder ID              | AN   | 7    | 2-8     | Warehouse holder ID                  |
| 3                                                                                                        | Batch Number           | N    | 4    | 9-12    | Batch number assigned by EWR         |
| 4                                                                                                        | Batch Type             | N    | 2    | 13-14   | 43                                   |
| 5                                                                                                        | Activity               | AN   | 11   | 15-25   | CL or CR                             |
| 6                                                                                                        | Filler                 | AN   | 1    | 26      | Reserved for EWR Inc. use            |
| 7                                                                                                        | Filler                 | A    | 1    | 27      | Reserved for EWR Inc. use            |
| 8                                                                                                        | Batch Date             | N    | 8    | 28-35   | Holder supplied batch date; MMDDYYYY |
| 9                                                                                                        | Batch Time             | N    | 6    | 36-41   | Holder supplied batch time; HHMMSS   |
| 10                                                                                                       | Filler                 | AN   | 61   | 42-102  | Reserved for EWR Inc. use            |
| 11                                                                                                       | Receipt Count          | N    | 6    | 103-108 | Number of receipts in file           |
| 12                                                                                                       | Filler                 | AN   | 12   | 80-120  | Reserved for EWR, Inc. use           |

### Table 44

|    | 11                    | Receipt Count   | N    | 6    | 103-108   | Number of receipts in file    |
|:---|:----------------------|:----------------|:-----|:-----|:----------|:------------------------------|
|    | 12                    | Filler          | AN   | 12   | 80-120    | Reserved for EWR, Inc. use    |
| D  | ETAIL LAYOUT FOR HD43 |                 |      |      |           |                               |
|    | Field                 | Field Name      | Type | Size | Pos       | Description                   |
|    | 1                     | Record Type     | A    | 1    | 1         | D = Detail record             |
|    | 2                     | Warehouse       | N    | 6    | 2-7       | Warehouse code of the receipt |
|    | 3                     | Receipt Number  | N    | 7    | 8-14      | Electronic Receipt Number     |
|    | 4                     | Crop Year       | N    | 4    | 15-18     | Crop year of the receipt      |
|    | 5                     | Status          | A    | 1    | 19        | L=Under loan, R=Redeem        |
|    | 6                     | Loan Type       | A    | 1    | 20        | A=Form-A, G=Form-G            |
|    | 7                     | Filler          | A    | 100  | 21-120    | Reserved for EWR Inc. use     |

### Table 45

| the CMA.  The header contains Redemption Date and E-mail address of redeemer.  The detail contains   |                       |               |      |      |        |                                        |
|:-----------------------------------------------------------------------------------------------------|:----------------------|:--------------|:-----|:-----|:-------|:---------------------------------------|
| warehouse number, receipt number, crop year and redeemer’s calculated redemption amount.             |                       |               |      |      |        |                                        |
| H                                                                                                    | EADER LAYOUT FOR HD57 |               |      |      |        | Record Size = 120                      |
|                                                                                                      | Field                 | Field Name    | Type | Size | Pos    | Description                            |
|                                                                                                      | 1                     | Record Type   | A    | 1    | 1      | H = Header Record                      |
|                                                                                                      | 2                     | Holder ID     | AN   | 7    | 2-8    | Holder ID - CMA receiving the download |
|                                                                                                      | 3                     | Batch Number  | N    | 4    | 9-12   | Batch number assigned                  |
|                                                                                                      | 4                     | Batch Type    | N    | 2    | 13-14  | 57 = CMA Loan Redemption               |
|                                                                                                      | 5                     | Batch Date    | N    | 8    | 15-22  | Holder supplied batch date:   MMDDYYYY |
|                                                                                                      | 6                     | Batch Time    | N    | 6    | 23-28  | Holder supplied batch time:  HHMMSS    |
|                                                                                                      | 7                     | From Holder   | AN   | 7    | 29-35  | Holder Redeeming Bales/Receipts        |
|                                                                                                      | 8                     | Redemption    | N    | 8    | 36-43  | Date of redemption:  MMDDYYYY          |
|                                                                                                      |                       | Date          |      |      |        |                                        |
|                                                                                                      | 9                     | Redeemer’s    | AN   | 45   | 44-88  | E-mail address of redeemer             |
|                                                                                                      |                       | E-mail        |      |      |        |                                        |
|                                                                                                      | 10                    | Filler        | A    | 14   | 89-102 | Reserved for EWR, Inc. use             |
|                                                                                                      | 11                    | Receipt Count | N    | 6    | 103-   |                                        |
|                                                                                                      |                       |               |      |      | 108    |                                        |
|                                                                                                      | 12                    | Filler        | A    | 12   | 109-   | Reserved for EWR, Inc. use             |
|                                                                                                      |                       |               |      |      | 120    |                                        |

### Table 46

| 12    | Filler                 | A    | 12   | 109-   | Reserved for EWR, Inc. use                       |
|:------|:-----------------------|:-----|:-----|:-------|:-------------------------------------------------|
|       |                        |      |      | 120    |                                                  |
|       | DETAIL LAYOUT FOR HD57 |      |      |        |                                                  |
| Field | Field Name             | Type | Size | Pos    | Description                                      |
| 1     | Record Type            | A    | 1    | 1      | D = Detail Record                                |
| 2     | Warehouse              | A    | 6    | 2-7    | Warehouse Code of the receipt                    |
|       | Code                   |      |      |        |                                                  |
| 3     | Electronic             | N    | 7    | 8-14   | Electronic Receipt Number                        |
|       | Receipt                |      |      |        |                                                  |
|       | Number                 |      |      |        |                                                  |
| 4     | Crop Year              | N    | 4    | 15-18  | Crop Year of the receipt:   YYYY                 |
| 5     | Redemption             | N    | 5    | 19-23  | Redeemer’s calculated redemption amount          |
|       | Amount                 |      |      |        | 99999 (2decimal) 35025=$350.25                   |
| 6     | Reconcentrated         | A    | 1    | 24     | Y = is reconcentrated loan                       |
|       | Loan                   |      |      |        | N = Not reconcentrated loan                      |
| 7     | Previous               | N    | 6    | 25-30  | Code of previous warehouse.  Entered only if the |
|       | Warehouse              |      |      |        | bale is reconcentrated                           |

### Table 47

| 8   | Previous   | N   | 7   | 31-37   | Warehouse receipt number from previous         |
|:----|:-----------|:----|:----|:--------|:-----------------------------------------------|
|     | Receipt    |     |     |         | warehouse.  Entered only if the bale is        |
|     | Number     |     |     |         | reconcentrated                                 |
| 9   | Gin Code   | N   | 5   | 38-42   | USDA assigned code which identifies the site   |
|     |            |     |     |         | where the cotton was ginned                    |
| 10  | Gin Tag    | N   | 7   | 43-49   | Sequential tag number assigned by the gin.     |
|     | Number     |     |     |         |                                                |
| 11  | Issue Date | N   | 8   | 50-57   | Date entered by the warehouse, not assigned by |
|     |            |     |     |         | EWR.  Storage date of the bale-MMDDYYYY        |
| 12  | Filler     | A   | 63  | 58-     | Reserved for EWR, Inc. use                     |
|     |            |     |     | 120     |                                                |

### Table 48

|    | 12                     | Filler       | A    | 63   | 58-    | Reserved for EWR, Inc. use                          |
|:---|:-----------------------|:-------------|:-----|:-----|:-------|:----------------------------------------------------|
|    |                        |              |      |      | 120    |                                                     |
| T  | RAILER LAYOUT FOR HD57 |              |      |      |        |                                                     |
|    | Field                  | Field Name   | Type | Size | Pos    | Description                                         |
|    | 1                      | Record Type  | A    | 1    | 1      | T=Trailer Record                                    |
|    | 2                      | Holder ID    | AN   | 7    | 2-8    | Must be the same as enter in the header record      |
|    | 3                      | Batch        | N    | 4    | 9-12   | The same as entered in the header record            |
|    |                        | Number       |      |      |        |                                                     |
|    | 4                      | Record Count | N    | 9    | 13-21  | Control total record count of detail records in the |
|    |                        |              |      |      |        | batch                                               |
|    | 5                      | Total Weight | N    | 9    | 22-30  | Total net weight of bales                           |
|    | 6                      | Hash Total   | N    | 15   | 31-45  | Electronic receipt number has total                 |
|    | 7                      | Filler       | A    | 75   | 46-120 | Reserved for EWR, Inc. use                          |

### Table 49

| file and contains general (public) information about a specific warehouse.  Any user on the system can   |                                  |                |      |      |         |                                              |
|:---------------------------------------------------------------------------------------------------------|:---------------------------------|:---------------|:-----|:-----|:--------|:---------------------------------------------|
| request warehouse information for any warehouse that uses EWR, Inc. as its provider.                     |                                  |                |      |      |         |                                              |
| H                                                                                                        | EADER LAYOUT FOR HD64            |                |      |      |         | Record Size = 120                            |
|                                                                                                          | Field                            | Field Name     | Type | Size | Pos     | Description                                  |
|                                                                                                          | 1                                | Record Type    | A    | 1    | 1       | H=Header Record                              |
|                                                                                                          | 2                                | Holder ID      | AN   | 7    | 2-8     | Holder ID of requestor                       |
|                                                                                                          | 3                                | Batch Number   | N    | 4    | 9-12    | Batch number , holder supplied               |
|                                                                                                          | 4                                | Batch Type     | N    | 2    | 13-14   | 64=Request Warehouse Profile                 |
|                                                                                                          | 5                                | Batch Date     | N    | 8    | 15-22   | Holder supplied batch date; MMDDYYYY         |
|                                                                                                          | 6                                | Batch Time     | N    | 6    | 23-28   | Holder supplied batch time; HHMMSS           |
|                                                                                                          | 7                                | Filler         | A    | 92   | 29-120  | Reserved for EWR, Inc. use                   |
| D                                                                                                        | ETAIL LAYOUT FOR HD64 (Record 1) |                |      |      |         |                                              |
|                                                                                                          | Field                            | Field Name     | Type | Size | Pos     | Description                                  |
|                                                                                                          | 1                                | Record Type    | A    | 1    | 1       | D=Detail Record                              |
|                                                                                                          | 2                                | Record Number  | N    | 2    | 2-3     | 01=First Record                              |
|                                                                                                          | 3                                | Warehouse      | N    | 6    | 4-9     | Warehouse Code                               |
|                                                                                                          |                                  | Code           |      |      |         |                                              |
|                                                                                                          | 4                                | Effective Date | N    | 8    | 10-17   | Effective date MMDDYYYY                      |
|                                                                                                          | 5                                | Type Code      | A    | 1    | 18      | F=Federal, S=State,  O=Other                 |
|                                                                                                          | 6                                | Name           | AN   | 40   | 19-58   | Warehouse Name (trade name)                  |
|                                                                                                          | 7                                | City           | AN   | 40   | 59-98   | Warehouse Location (city)                    |
|                                                                                                          | 8                                | State          | A    | 2    | 99-100  | Warehouse Location (state)                   |
|                                                                                                          | 9                                | Receiving Rate | N    | 4    | 101-104 |                                              |
|                                                                                                          | 10                               | Storage Rate   | N    | 5    | 105-109 |                                              |
|                                                                                                          | 11                               | Compression    | N    | 4    | 110-113 |                                              |
|                                                                                                          |                                  | Rate           |      |      |         |                                              |
|                                                                                                          | 12                               | Loading Rate   | N    | 4    | 114-117 |                                              |
|                                                                                                          | 13                               | Storage Charge | A    | 1    | 118     | D=Daily; C=Calendar Months; S=Actual Months  |
|                                                                                                          |                                  | Frequency      |      |      |         | (same day); F=Actual Months (following day); |
|                                                                                                          |                                  |                |      |      |         | M=Monthly (legacy support)                   |
|                                                                                                          |                                  |                |      |      |         | See Appendix J – Files Sent To EWR           |
|                                                                                                          | 14                               | Filler         | A    | 2    | 119-120 | Reserved for EWR, Inc. use                   |
| D                                                                                                        | ETAIL LAYOUT FOR HD64 (Record 2) |                |      |      |         |                                              |
|                                                                                                          | Field                            | Field Name     | Type | Size | Pos     | Description                                  |
|                                                                                                          | 1                                | Record Type    | A    | 1    | 1       | D=Detail Record                              |
|                                                                                                          | 2                                | Record Number  | N    | 2    | 2-3     | 02=Second Record                             |

### Table 50

|    | 3                                | Warehouse      | N    | 6    | 4-9     | Warehouse Code                              |
|:---|:---------------------------------|:---------------|:-----|:-----|:--------|:--------------------------------------------|
|    |                                  | Code           |      |      |         |                                             |
|    | 4                                | Effective Date | N    | 8    | 10-17   | Effective date; MMDDYYYY                    |
|    | 5                                | City-Issued    | AN   | 40   | 18-57   | City in which receipt is issued             |
|    | 6                                | State-Issued   | A    | 2    | 58-59   | State in which receipt is issued            |
|    | 7                                | Signature      | A    | 40   | 60-99   | Name of person signing receipt              |
|    | 8                                | License Number | AN   | 6    | 100-105 | Warehouse License Number                    |
|    | 9                                | Fire Insurance | A    | 1    | 106     | Y=Has Fire Insurance, N=None                |
|    | 10                               | Open Yard      | A    | 1    | 107     | Open Yard Endorsement                       |
|    |                                  | Endorsement    |      |      |         | Y=yes, N= no                                |
|    | 11                               | Open Yard      | A    | 1    | 108     | Open Yard disclaimer                        |
|    |                                  | Disclaimer     |      |      |         | Y=yes, N=no                                 |
|    | 12                               | Receiving      | A    | 1    | 109     | Y=receiving fees include new ties; N= no    |
|    |                                  | Includes Ties  |      |      |         |                                             |
|    | 13                               | Compression    | A    | 1    | 110     | N=no compression facilities, compression is |
|    |                                  | Facilities     |      |      |         | not available;                              |
|    |                                  |                |      |      |         | Y=Compression service available             |
|    | 14                               | Claims/Liens   | A    | 1    | 111     | The warehouse will have claims or liens on  |
|    |                                  |                |      |      |         | bales other than normal tariff charges      |
|    |                                  |                |      |      |         | Y=yes, N=no                                 |
|    | 15                               | Incorporated   | A    | 1    | 112     | I = Incorporated; N = No Incorporated       |
|    |                                  | Type           |      |      |         | U or Empty = Unknown                        |
|    | 16                               | Incorporated   | A    | 2    | 113-114 | US State abbreviation                       |
|    |                                  | State          |      |      |         |                                             |
|    | 17                               | Filler         | A    | 6    | 115-120 | Reserved for EWR, Inc. use                  |
| D  | ETAIL LAYOUT FOR HD64 (Record 3) |                |      |      |         |                                             |
|    | Field                            | Field Name     | Type | Size | Pos     | Description                                 |
|    | 1                                | Record Type    | A    | 1    | 1       | D = Detail Record                           |
|    | 2                                | Record Number  | N    | 2    | 2-3     | 03 = Record Number                          |
|    | 3                                | Legal Name     | A    | 80   | 4-83    |                                             |
|    | 4                                | EWR Warehouse  | A    | 9    | 84-92   | Reserved for EWR, Inc. use                  |
|    |                                  | Profile ID     |      |      |         |                                             |
|    | 5                                | Filler         | A    | 28   | 193-120 | Reserved for EWR, Inc. use                  |

### Table 51

|    | 4                                   | Filler        | A    | 36   | 84-119   | Reserved for EWR, Inc. use                      |
|:---|:------------------------------------|:--------------|:-----|:-----|:---------|:------------------------------------------------|
|    | 5                                   | Filler        | A    | 1    | 120      | Reserved for EWR, Inc. use                      |
| D  | ETAIL LAYOUT FOR HD64 (Record 5)    |               |      |      |          |                                                 |
|    | Field                               | Field Name    | Type | Size | Pos      | Description                                     |
|    | 1                                   | Record Type   | A    | 1    | 1        | D = Detail record                               |
|    | 2                                   | Record Number | N    | 2    | 2-3      | 05 = Record Number                              |
|    | 3                                   | Legal State   | A    | 80   | 4-83     | Legal State – US Abbreviation                   |
|    | 4                                   | Filler        | A    | 37   | 84-120   | Reserved for EWR, Inc. use                      |
| D  | ETAIL LAYOUT FOR HD64 (Record 6-37) |               |      |      |          |                                                 |
|    | Field                               | Field Name    | Type | Size | Pos      | Description                                     |
|    | 1                                   | Record Type   | A    | 1    | 1        | D = Detail Record                               |
|    | 2                                   | Record Number | N    | 2    | 2-3      | Record Numbers = 06 through 37                  |
|    | 3                                   | Terms &       | AN   | 80   | 4-83     | No longer used.  This field will be filled with |
|    |                                     | Condition     |      |      |          | the following text:  “Please go to              |
|    |                                     |               |      |      |          | www.ewrinc.com\cotton to see terms.”            |
|    | 4                                   | Filler        | A    | 37   | 84-120   | Reserved for EWR, Inc. use                      |
| T  | RAILER LAYOUT FOR HD64              |               |      |      |          |                                                 |
|    | Field                               | Field Name    | Type | Size | Pos      | Description                                     |
|    | 1                                   | Record Type   | A    | 1    | 1        | T = Trailer Record                              |
|    | 2                                   | Holder ID     | AN   | 7    | 2-8      | The same as enter in the header record          |
|    | 3                                   | Batch Number  | N    | 4    | 9-12     | The same as enter in the header record          |
|    | 4                                   | Record Count  | N    | 9    | 13-21    | Control total record count of detail records in |
|    |                                     |               |      |      |          | the batch                                       |
|    | 5                                   | Filler        | A    | 99   | 22-120   | Reserved for EWR, Inc. use                      |

### Table 52

| DETAIL LAYOUT FOR HD64 (Record 4)   |                                     |               |      |      |        |                                                 |
|:------------------------------------|:------------------------------------|:--------------|:-----|:-----|:-------|:------------------------------------------------|
|                                     | Field                               | Field Name    | Type | Size | Pos    | Description                                     |
|                                     | 1                                   | Record Type   | A    | 1    | 1      | D = Detail Record                               |
|                                     | 2                                   | Record Number | N    | 2    | 2-3    | 04 = Record Number                              |
|                                     | 3                                   | Legal City    | A    | 80   | 4-83   | Legal entity name text line                     |
|                                     | 4                                   | Filler        | A    | 36   | 84-119 | Reserved for EWR, Inc. use                      |
|                                     | 5                                   | Filler        | A    | 1    | 120    | Reserved for EWR, Inc. use                      |
| D                                   | ETAIL LAYOUT FOR HD64 (Record 5)    |               |      |      |        |                                                 |
|                                     | Field                               | Field Name    | Type | Size | Pos    | Description                                     |
|                                     | 1                                   | Record Type   | A    | 1    | 1      | D = Detail record                               |
|                                     | 2                                   | Record Number | N    | 2    | 2-3    | 05 = Record Number                              |
|                                     | 3                                   | Legal State   | A    | 80   | 4-83   | Legal State – US Abbreviation                   |
|                                     | 4                                   | Filler        | A    | 37   | 84-120 | Reserved for EWR, Inc. use                      |
| D                                   | ETAIL LAYOUT FOR HD64 (Record 6-37) |               |      |      |        |                                                 |
|                                     | Field                               | Field Name    | Type | Size | Pos    | Description                                     |
|                                     | 1                                   | Record Type   | A    | 1    | 1      | D = Detail Record                               |
|                                     | 2                                   | Record Number | N    | 2    | 2-3    | Record Numbers = 06 through 37                  |
|                                     | 3                                   | Terms &       | AN   | 80   | 4-83   | No longer used.  This field will be filled with |
|                                     |                                     | Condition     |      |      |        | the following text:  “Please go to              |
|                                     |                                     |               |      |      |        | www.ewrinc.com\cotton to see terms.”            |
|                                     | 4                                   | Filler        | A    | 37   | 84-120 | Reserved for EWR, Inc. use                      |
| T                                   | RAILER LAYOUT FOR HD64              |               |      |      |        |                                                 |
|                                     | Field                               | Field Name    | Type | Size | Pos    | Description                                     |
|                                     | 1                                   | Record Type   | A    | 1    | 1      | T = Trailer Record                              |
|                                     | 2                                   | Holder ID     | AN   | 7    | 2-8    | The same as enter in the header record          |
|                                     | 3                                   | Batch Number  | N    | 4    | 9-12   | The same as enter in the header record          |
|                                     | 4                                   | Record Count  | N    | 9    | 13-21  | Control total record count of detail records in |
|                                     |                                     |               |      |      |        | the batch                                       |
|                                     | 5                                   | Filler        | A    | 99   | 22-120 | Reserved for EWR, Inc. use                      |

### Table 53

| the batch will be the holder that sent the request.   |                       |               |      |      |         |                                     |
|:------------------------------------------------------|:----------------------|:--------------|:-----|:-----|:--------|:------------------------------------|
| H                                                     | EADER LAYOUT FOR HD66 |               |      |      |         | Record Size = 271                   |
|                                                       | Field                 | Field Name    | Type | Size | Pos     | Description                         |
|                                                       | 1                     | Record Type   | A    | 1    | 1       | H = Header Record                   |
|                                                       | 2                     | Holder ID     | AN   | 7    | 2-8     | Holder ID who sent the batch        |
|                                                       | 3                     | Batch Number  | N    | 4    | 9-12    | Batch number , holder supplied      |
|                                                       | 4                     | Batch Type    | N    | 2    | 13-14   | 66                                  |
|                                                       | 5                     | Activity      | AN   | 11   | 15-25   |                                     |
|                                                       | 6                     | Action Code   | AN   | 1    | 26      |                                     |
|                                                       | 7                     | Filler        | A    | 1    | 27      | Reserved for EWR Inc., use          |
|                                                       | 8                     | Batch Date    | N    | 8    | 28-35   | Holder supplied batch time;MMDDYYYY |
|                                                       | 9                     | Batch Time    | N    | 6    | 36-41   | Holder supplied batch time; HHMMSS  |
|                                                       | 10                    | Filler        | AN   | 8    | 42-49   | Reserved for EWR Inc. use           |
|                                                       | 11                    | Filler        | AN   | 53   | 50-102  | Reserved for EWR Inc. use           |
|                                                       | 12                    | Receipt Count | N    | 6    | 103-108 | Number of receipts in file          |
|                                                       | 13                    | Filler        | AN   | 163  | 109-271 | Reserved for EWR, Inc. use          |

### Table 54

| 14   | Reconcentrated     | A   | 1   | 42      | R=Bale is reconcentrated                        |
|:-----|:-------------------|:----|:----|:--------|:------------------------------------------------|
|      |                    |     |     |         | Space = Not reconcentrated                      |
| 15   | Previous           | N   | 6   | 43-48   | Code of previous warehouse – Entered only if    |
|      | Warehouse          |     |     |         | the bale is reconcentrated.                     |
| 16   | Previous Receipt   | N   | 7   | 49-55   | Warehouse receipt number from previous          |
|      | Number             |     |     |         | warehouse, entered for reconcentrated cotton    |
|      |                    |     |     |         | only                                            |
| 17   | Gin Code Number    | N   | 5   | 56-60   | USDA assigned code where the cotton was         |
|      |                    |     |     |         | ginned                                          |
| 18   | Gin Tag Number     | N   | 7   | 61-67   | Sequential tag number assigned by the gin       |
| 19   | Storage Paid       | N   | 8   | 68-75   | Storage paid through date; MMDDYYYY.  Last      |
|      | Through            |     |     |         | date that storage charges against the bale      |
|      |                    |     |     |         | were paid to the warehouse                      |
| 20   | Mark               | AN  | 8   | 76-83   | Shipper assigned mark                           |
| 21   | Locator ID         | AN  | 8   | 84-91   | Warehouse bale location                         |
| 22   | Electronic Receipt | A   | 1   | 92      | O=Open; C=Cancel; D=Deactivated; V=Void         |
|      | Status             |     |     |         |                                                 |
| 23   | Electronic Receipt | A   | 1   | 93      | E=Electronic                                    |
|      | Flag               |     |     |         | P = Paper                                       |
| 24   | Receipt Type       | A   | 1   | 94      | See Appendix D – Receipt Types in “Files Sent   |
|      |                    |     |     |         | to EWR” document.                               |
| 25   | Current Holder     | A   | 1   | 95      | M = Merchant                                    |
|      | Type               |     |     |         | W = Warehouse                                   |
|      |                    |     |     |         | G = Gin                                         |
|      |                    |     |     |         | Z = Coop                                        |
|      |                    |     |     |         | P = Producer                                    |
|      |                    |     |     |         | C = Government                                  |
|      |                    |     |     |         | B = Bank                                        |
| 26   | Loan Transfer      | A   | 1   | 96      | Y = Yes.  This bale was transferred while under |
|      |                    |     |     |         | loan (Reconcentrated Loan Transfer)             |
| 27   | Filler             | N   | 5   | 97-101  |                                                 |
| 28   | Weight Date        | N   | 8   | 102-109 | Weight date assigned by warehouse;              |
|      |                    |     |     |         | MMDDYYYY                                        |
| 29   | Tenderable         | AN  | 2   | 110-111 | AMS assigned                                    |
| 30   | Rain Grown         | AN  | 1   | 112     | R = Rain grown; N = Not rain grown; Unknown     |
| 31   | Under S/O          | A   | 1   | 113     | Y = Under open shipping order                   |
| 32   | Block Receipt      | A   | 1   | 114     | Is this receipt a block receipt                 |
| 33   | Block Bales        | N   | 5   | 115-119 | Number of bales on block                        |
| 34   | Is Stored Outside  | A   | 1   | 120     | Y/N                                             |
| 35   | EWR Container ID   | N   | 8   | 121-128 | EWR unique number assigned to each              |
|      |                    |     |     |         | container                                       |
| 36   | Filler             | AN  | 12  | 129-140 |                                                 |
| 37   | World              | A   | 1   | 141     | T= Tenderable                                   |
|      | Tenderable         |     |     |         | N = Non-Tenderable                              |

### Table 55

| 38   | Lot #         | N   | 6   | 142-147   | Replaces field #27                           |
|:-----|:--------------|:----|:----|:----------|:---------------------------------------------|
| 39   | World Gin Tag | AN  | 12  | 148-159   |                                              |
| 40   | Type Bagging  | A   | 1   | 160       |                                              |
| 41   | Type of Ties  | A   | 1   | 161       |                                              |
| 42   | Bagging       | A   | 1   | 162       | Bag condition – User defined.  Examples are: |
|      | Condition     |     |     |           | A = Bale is completely covered               |
|      |               |     |     |           | B = Bale may have minor tears and an exposed |

### Table 56

|    |                        | Code         |      |      |         |                                         |
|:---|:-----------------------|:-------------|:-----|:-----|:--------|:----------------------------------------|
|    | 44                     | Filler       |      | 108  | 164-271 |                                         |
| T  | RAILER LAYOUT FOR HD66 |              |      |      |         |                                         |
|    | Field                  | Field Name   | Type | Size | Pos     | Description                             |
|    | 1                      | Record Type  | A    | 1    | 1       | T=Trailer Record                        |
|    | 2                      | Holder ID    | AN   | 7    | 2-8     | Holder ID who sent the batch            |
|    | 3                      | Batch Number | N    | 4    | 9-12    | The same as enter in the header record. |
|    | 4                      | Record Count | N    | 9    | 13-21   | Number of receipts                      |
|    | 5                      | Filler       | A    | 9    | 22-30   | Reserved for EWR, Inc. use              |
|    | 6                      | Filler       | A    | 15   | 31-45   | Reserved for EWR, Inc. use              |
|    | 7                      | Filler       | A    | 226  | 46-271  | Reserved for EWR Inc. use               |

### Table 57

| H                             | D67 is used to inform users of special events, such as if the database was temporarily unavailable   |              |      |      |       |                                                 |
|:------------------------------|:-----------------------------------------------------------------------------------------------------|:-------------|:-----|:-----|:------|:------------------------------------------------|
| during a time of maintenance. |                                                                                                      |              |      |      |       |                                                 |
| H                             | EADER LAYOUT FOR HD67                                                                                |              |      |      |       | Record Size = 85                                |
|                               | Field                                                                                                | Field Name   | Type | Size | Pos   | Description                                     |
|                               | 1                                                                                                    | Record Type  | A    | 1    | 1     | H-Header Record                                 |
|                               | 2                                                                                                    | Holder ID    | AN   | 7    | 2-8   | Holder ID of participant receiving the message  |
|                               |                                                                                                      |              |      |      |       | from EWR                                        |
|                               | 3                                                                                                    | Batch Number | N    | 4    | 9-12  | Batch number assigned - Cannot be duplicated    |
|                               |                                                                                                      |              |      |      |       | within the same day                             |
|                               | 4                                                                                                    | Batch Type   | N    | 2    | 13-14 | 67=ASCII Text Message from EWR, Inc. Host       |
|                               |                                                                                                      |              |      |      |       | Computer                                        |
|                               | 5                                                                                                    | Batch Date   | N    | 8    | 15-22 | Holder supplied batch date; MMDDYYYY            |
|                               | 6                                                                                                    | Batch Time   | N    | 6    | 23-28 | Holder supplied batch time; HHMMSS              |
|                               | 7                                                                                                    | Date Entered | AN   | 8    | 29-36 | Date EWR created the message                    |
|                               | 8                                                                                                    | Filler       | A    | 49   | 37-85 | Reserved for EWR, Inc. use                      |
| D                             | ETAIL LAYOUT FOR HD67 (Maximum of 32 lines) Records 1-32                                             |              |      |      |       |                                                 |
|                               | Field                                                                                                | Field Name   | Type | Size | Pos   | Description                                     |
|                               | 1                                                                                                    | Record Type  | A    | 1    | 1     | D=Detail Record                                 |
|                               | 2                                                                                                    | Record       | N    | 2    | 2-3   | Record number                                   |
|                               |                                                                                                      | Number       |      |      |       |                                                 |
|                               | 3                                                                                                    | Text Line    | AN   | 80   | 4-83  | 80 character text line                          |
|                               | 4                                                                                                    | Filler       | A    | 2    | 84-85 | Reserved for EWR, Inc. use                      |
|                               | TRAILER LAYOUT FOR HD67                                                                              |              |      |      |       |                                                 |
|                               | Field                                                                                                | Field Name   | Type | Size | Pos   | Description                                     |
|                               | 1                                                                                                    | Record Type  | A    | 1    | 1     | T=Trailer Record                                |
|                               | 2                                                                                                    | Holder ID    | AN   | 7    | 2-8   | The same as entered in the header record        |
|                               | 3                                                                                                    | Batch Number | N    | 4    | 9-12  | The same as entered in the header record        |
|                               | 4                                                                                                    | Record Count | N    | 9    | 13-21 | Control total record count of detail records in |
|                               |                                                                                                      |              |      |      |       | the batch                                       |
|                               | 5                                                                                                    | Filler       | A    | 64   | 22-85 | Reserved for EWR, Inc. use                      |

### Table 58

| Holder Type = A)   |                        |                |      |      |         |                                               |
|:-------------------|:-----------------------|:---------------|:-----|:-----|:--------|:----------------------------------------------|
|                    | HEADER LAYOUT FOR HD68 |                |      |      |         | Record Size =120                              |
|                    | Field                  | Field Name     | Type | Size | Pos     | Description                                   |
|                    | 1                      | Record Type    | A    | 1    | 1       | H-Header Record                               |
|                    | 2                      | Holder ID      | AN   | 7    | 2-8     | Holder ID of requestor                        |
|                    | 3                      | Batch Number   | N    | 4    | 9-12    | Batch number assigned                         |
|                    | 4                      | Batch Type     | N    | 2    | 13-14   | 68=Holder Information Request                 |
|                    | 5                      | Batch Date     | N    | 8    | 15-22   | Holder supplied batch date; MMDDYYYY          |
|                    | 6                      | Batch Time     | N    | 6    | 23-28   | Holder supplied batch time; HHMMSS            |
|                    | 7                      | Filler         | A    | 74   | 29-102  | Reserved for EWR, Inc. use                    |
|                    | 8                      | Receipt Count  | N    | 6    | 103-108 |                                               |
|                    | 9                      | Filler         | A    | 12   | 109-120 | Reserved for EWR, Inc. use                    |
| D                  | ETAIL LAYOUT FOR HD68  |                |      |      |         |                                               |
|                    | Field                  | Field Name     | Type | Size | Pos     | Description                                   |
|                    | 1                      | Record Type    | A    | 1    | 1       | D=Detail Record                               |
|                    | 2                      | Warehouse      | N    | 6    | 2-7     | Warehouse Code of the Receipt                 |
|                    |                        | Code           |      |      |         |                                               |
|                    | 3                      | Electronic     | N    | 7    | 8-14    | Electronic Receipt Number                     |
|                    |                        | Receipt        |      |      |         |                                               |
|                    |                        | Number         |      |      |         |                                               |
|                    | 4                      | Crop Year      | N    | 4    | 15-18   | Crop year of the Receipt                      |
|                    | 5                      | Current Holder | AN   | 7    | 19-25   | Holder ID of the current Holder of the        |
|                    |                        | ID             |      |      |         | electronic receipt(s)                         |
|                    | 6                      | Subholder ID   | AN   | 7    | 26-32   | Holder ID of the current Subholder of the     |
|                    |                        |                |      |      |         | electronic receipt(s)                         |
|                    | 7                      | Previous       | AN   | 7    | 33-39   | Holder ID of the previous Holder of the       |
|                    |                        | Holder ID      |      |      |         | electronic receipt(s)                         |
|                    | 8                      | Electronic     | A    | 1    | 40      | O=Open  C=Cancel  D=Deactivated  V=Void       |
|                    |                        | Receipt Status |      |      |         |                                               |
|                    | 9                      | Electronic     | A    | 1    | 41      | E=Electronic                                  |
|                    |                        | Receipt Flag   |      |      |         | P=Paper                                       |
|                    | 10                     | Receipt Type   | A    | 1    | 42      | See Appendix D – Receipt Types in “Files Sent |
|                    |                        |                |      |      |         | to EWR” document.                             |
|                    | 11                     | Filler         | A    | 78   | 43-120  | Reserved for EWR, Inc. use                    |

### Table 59

| Holder Type = A)   |                        |                |      |      |         |                                               |
|:-------------------|:-----------------------|:---------------|:-----|:-----|:--------|:----------------------------------------------|
|                    | HEADER LAYOUT FOR HD68 |                |      |      |         | Record Size =120                              |
|                    | Field                  | Field Name     | Type | Size | Pos     | Description                                   |
|                    | 1                      | Record Type    | A    | 1    | 1       | H-Header Record                               |
|                    | 2                      | Holder ID      | AN   | 7    | 2-8     | Holder ID of requestor                        |
|                    | 3                      | Batch Number   | N    | 4    | 9-12    | Batch number assigned                         |
|                    | 4                      | Batch Type     | N    | 2    | 13-14   | 68=Holder Information Request                 |
|                    | 5                      | Batch Date     | N    | 8    | 15-22   | Holder supplied batch date; MMDDYYYY          |
|                    | 6                      | Batch Time     | N    | 6    | 23-28   | Holder supplied batch time; HHMMSS            |
|                    | 7                      | Filler         | A    | 74   | 29-102  | Reserved for EWR, Inc. use                    |
|                    | 8                      | Receipt Count  | N    | 6    | 103-108 |                                               |
|                    | 9                      | Filler         | A    | 12   | 109-120 | Reserved for EWR, Inc. use                    |
| D                  | ETAIL LAYOUT FOR HD68  |                |      |      |         |                                               |
|                    | Field                  | Field Name     | Type | Size | Pos     | Description                                   |
|                    | 1                      | Record Type    | A    | 1    | 1       | D=Detail Record                               |
|                    | 2                      | Warehouse      | N    | 6    | 2-7     | Warehouse Code of the Receipt                 |
|                    |                        | Code           |      |      |         |                                               |
|                    | 3                      | Electronic     | N    | 7    | 8-14    | Electronic Receipt Number                     |
|                    |                        | Receipt        |      |      |         |                                               |
|                    |                        | Number         |      |      |         |                                               |
|                    | 4                      | Crop Year      | N    | 4    | 15-18   | Crop year of the Receipt                      |
|                    | 5                      | Current Holder | AN   | 7    | 19-25   | Holder ID of the current Holder of the        |
|                    |                        | ID             |      |      |         | electronic receipt(s)                         |
|                    | 6                      | Subholder ID   | AN   | 7    | 26-32   | Holder ID of the current Subholder of the     |
|                    |                        |                |      |      |         | electronic receipt(s)                         |
|                    | 7                      | Previous       | AN   | 7    | 33-39   | Holder ID of the previous Holder of the       |
|                    |                        | Holder ID      |      |      |         | electronic receipt(s)                         |
|                    | 8                      | Electronic     | A    | 1    | 40      | O=Open  C=Cancel  D=Deactivated  V=Void       |
|                    |                        | Receipt Status |      |      |         |                                               |
|                    | 9                      | Electronic     | A    | 1    | 41      | E=Electronic                                  |
|                    |                        | Receipt Flag   |      |      |         | P=Paper                                       |
|                    | 10                     | Receipt Type   | A    | 1    | 42      | See Appendix D – Receipt Types in “Files Sent |
|                    |                        |                |      |      |         | to EWR” document.                             |
|                    | 11                     | Filler         | A    | 78   | 43-120  | Reserved for EWR, Inc. use                    |

### Table 60

| TRAILER LAYOUT FOR HD68   |              |      |      |        |                                             |
|:--------------------------|:-------------|:-----|:-----|:-------|:--------------------------------------------|
| Field                     | Field Name   | Type | Size | Pos    | Description                                 |
| 1                         | Record Type  | A    | 1    | 1      | T=Trailer Record                            |
| 2                         | Holder ID    | AN   | 7    | 2-8    | The same as entered in the header record    |
| 3                         | Batch Number | N    | 4    | 9-12   | The same as entered in the header record    |
| 4                         | Record Count | N    | 9    | 13-21  | Control total record count of the number of |
|                           |              |      |      |        | detail records in the batch                 |
| 5                         | Filler       | A    | 9    | 22-30  | Reserved for EWR, Inc. use                  |
| 6                         | Hash Total   | N    | 15   | 31-45  | Electronic Receipt number hash total        |
| 7                         | Filler       | A    | 75   | 46-120 | Reserved for EWR, Inc. use                  |

### Table 61

| Receive Option in the PC software), the bank can easily take action on the shipping order, such as   |                        |      |      |       |                                                |
|:-----------------------------------------------------------------------------------------------------|:-----------------------|:-----|:-----|:------|:-----------------------------------------------|
| release or return to seller                                                                          |                        |      |      |       |                                                |
|                                                                                                      | HEADER LAYOUT FOR HD86 |      |      |       | Record Size = 60                               |
| Field                                                                                                | Field Name             | Type | Size | Pos   | Description                                    |
| 1                                                                                                    | Record Type            | A    | 1    | 1     | H=Header Record                                |
| 2                                                                                                    | Holder ID of           | AN   | 7    | 2-8   | Holder ID of Bank Holding the Receipts as      |
|                                                                                                      | Bank                   |      |      |       | Collateral                                     |
| 3                                                                                                    | Batch                  | N    | 4    | 9-12  | Batch Number assigned by Host                  |
|                                                                                                      | Number                 |      |      |       |                                                |
| 4                                                                                                    | Batch Type             | N    | 2    | 13-14 | 86=Shipping Orders Held by Bank                |
| 5                                                                                                    | Batch Date             | N    | 8    | 15-22 | Date batch was created; MMDDYYYY               |
| 6                                                                                                    | Batch Time             | N    | 6    | 23-28 | Time batch was created; HHMMSS                 |
| 7                                                                                                    | Warehouse              | N    | 6    | 29-34 | Warehouse code of facility where cotton is     |
|                                                                                                      | Code                   |      |      |       | stored                                         |
| 8                                                                                                    | Shipping               | AN   | 10   | 35-44 | S/O Number - This data is received in a batch  |
|                                                                                                      | Order                  |      |      |       | type 21 sent to host                           |
|                                                                                                      | Numbers                |      |      |       |                                                |
| 9                                                                                                    | Shipper’s              | AN   | 8    | 45-52 | Shipper's mark sent to host in a batch type 21 |
|                                                                                                      | Mark                   |      |      |       |                                                |
| 10                                                                                                   | Holder ID of           | AN   | 7    | 53-59 | Holder ID of shipper                           |
|                                                                                                      | Shipper                |      |      |       |                                                |
| 11                                                                                                   | Block                  | A    | 1    | 60    | Blank =Regular Receipts                        |
|                                                                                                      | Receipts               |      |      |       | Y =Block Receipts                              |

### Table 62

|       | DETAIL LAYOUT FOR HD86   |      |      |       |                                                         |
|:------|:-------------------------|:-----|:-----|:------|:--------------------------------------------------------|
| Field | Field Name               | Type | Size | Pos   | Description                                             |
| 1     | Record Type              | A    | 1    | 1     | D=Detail Record                                         |
| 2     | Electronic               | N    | 7    | 2-8   | Electronic Receipt Number                               |
|       | Receipt                  |      |      |       |                                                         |
|       | Number                   |      |      |       |                                                         |
| 3     | Net Weight               | N    | 3    | 9-11  | Net weight of bale                                      |
| 4     | Crop Year                | N    | 4    | 12-15 | YYYY                                                    |
| 5     | Filler                   | A    | 45   | 16-60 | Reserved for EWR, Inc. use                              |
|       | TRAILER LAYOUT FOR HD86  |      |      |       |                                                         |
| Field | Field Name               | Type | Size | Pos   | Description                                             |
| 1     | Record Type              | A    | 1    | 1     | T=Trailer Record                                        |
| 2     | Holder ID                | AN   | 7    | 2-8   | Must be the same as entered in batch header             |
| 3     | Batch Number             | N    | 4    | 9-12  | Must be the same as entered in batch header             |
| 4     | Record Count             | N    | 9    | 13-21 | Control total record count of the detail records in the |
|       |                          |      |      |       | batch                                                   |
| 5     | Total Weight             | N    | 9    | 22-30 | Total net weight of bales in the batch if entered in    |
|       |                          |      |      |       | the original batch from the shipper                     |
| 6     | Hash Total               | N    | 15   | 31-45 | Electronic receipt number hash total                    |
| 7     | Filler                   | A    | 15   | 46-60 | Reserved for EWR, Inc. use                              |

### Table 63

| W   | hen action is taken by the bank, a Batch Type 71 is created.   |                 |      |      |         |                                                  |
|:----|:---------------------------------------------------------------|:----------------|:-----|:-----|:--------|:-------------------------------------------------|
| F   | ILE LAYOUT FOR HD87 (HEADER RECORD ONLY)                       |                 |      |      |         | Record Size = 150                                |
|     | Field                                                          | Field Name      | Type | Size | Pos     | Description                                      |
|     | 1                                                              | Record Type     | A    | 1    | 1       | H=Header Record                                  |
|     | 2                                                              | Bank Holder ID  | AN   | 7    | 2-8     | Holder ID of Purchaser’s Bank                    |
|     | 3                                                              | Batch Number    | N    | 4    | 9-12    | Batch number assigned by user’s PC sending the   |
|     |                                                                |                 |      |      |         | request or batch type 51                         |
|     | 4                                                              | Batch Type      | N    | 2    | 13-14   | Type=87 Bank Draft                               |
|     | 5                                                              | Batch Date      | N    | 8    | 15-22   | Date batch was created; MMDDYYYY                 |
|     | 6                                                              | Batch Time      | N    | 6    | 23-28   | Time batch was created: HHMMSS                   |
|     | 7                                                              | Purchaser’s     | AN   | 7    | 29-35   | Holder ID of Purchaser, input by creator of      |
|     |                                                                | Holder ID       |      |      |         | batch type 51                                    |
|     | 8                                                              | Purchaser       | AN   | 20   | 36-55   | Purchaser Name from the holder control file in   |
|     |                                                                | Name            |      |      |         | the host                                         |
|     | 9                                                              | Seller Name     | AN   | 20   | 56-75   | Seller Name                                      |
|     | 10                                                             | Holder ID of    | AN   | 7    | 76-82   | Holder ID of Seller, or the holder who created   |
|     |                                                                | Seller          |      |      |         | the batch type 51                                |
|     | 11                                                             | Draft Number    | AN   | 10   | 83-92   | Bank Draft Number entered in batch type 51 by    |
|     |                                                                |                 |      |      |         | seller                                           |
|     | 12                                                             | Draft Amount    | N    | 10   | 93-102  | Draft Amount entered in batch type 51 by seller  |
|     |                                                                |                 |      |      |         | 99999999V99, must be at least $1.00              |
|     | 13                                                             | Presenting Bank | AN   | 24   | 103-126 | Presenting Bank Name - The bank on which the     |
|     |                                                                | Name            |      |      |         | draft is drawn                                   |
|     | 14                                                             | Block Receipts  | A    | 1    | 127     | Blank=Regular Receipt Batch                      |
|     |                                                                |                 |      |      |         | Y=Block Receipt Batch                            |
|     | 15                                                             | Receipt Count   | N    | 6    | 128-133 | Count of receipts in Draft                       |
|     | 16                                                             | Draft Control   | N    | 10   | 134-143 | Host assigned number to flag the receipts in the |
|     |                                                                | Number          |      |      |         | draft                                            |
|     | 17                                                             | Filler          | A    | 7    | 144-150 | Reserved for EWR, Inc. use                       |

### Table 64

| W   | hen the bank takes action on the outbound draft, a Batch Type 71 is created   |                     |      |      |         |                                                |
|:----|:------------------------------------------------------------------------------|:--------------------|:-----|:-----|:--------|:-----------------------------------------------|
| H   | EADER RECORD ONLY                                                             |                     |      |      |         | Record Size = 150                              |
|     | Field                                                                         | Field Name          | Type | Size | Pos     | Descriptions                                   |
|     | 1                                                                             | Record Type         | A    | 1    | 1       | H=Header Record                                |
|     | 2                                                                             | Bank Holder ID      | AN   | 7    | 2-8     | Holder ID of Purchaser’s Bank                  |
|     | 3                                                                             | Batch Number        | N    | 4    | 9-12    | Batch number assigned by user sending the      |
|     |                                                                               |                     |      |      |         | request or Batch Type 51                       |
|     | 4                                                                             | Batch Type          | N    | 2    | 13-14   | Type=91 Bank Draft - OUTBOUND DRAFTS           |
|     | 5                                                                             | Batch Date          | N    | 8    | 15-22   | Date batch was created; MMDDYYYY               |
|     | 6                                                                             | Batch Time          | N    | 6    | 23-28   | Time batch was created: HHMMSS                 |
|     | 7                                                                             | Purchaser’s         | AN   | 7    | 29-35   | Holder ID of the buyer (Purchaser), input by   |
|     |                                                                               | Holder ID           |      |      |         | creator of Batch Type 51                       |
|     | 8                                                                             | Purchaser’s Name    | A    | 20   | 36-55   | Purchaser name of the holder.                  |
|     | 9                                                                             | Seller’s Name       | A    | 20   | 56-75   | Seller name of the holder                      |
|     | 10                                                                            | Holder ID of Seller | AN   | 7    | 76-82   | Holder ID of Seller, or the holder who created |
|     |                                                                               |                     |      |      |         | the Batch Type 51                              |
|     | 11                                                                            | Draft Number        | N    | 10   | 83-92   | Bank draft number in Batch Type 51 by seller   |
|     | 12                                                                            | Draft Amount        | N    | 10   | 93-102  | Draft amount entered in Batch Type 51 by       |
|     |                                                                               |                     |      |      |         | seller 99999999V99                             |
|     | 13                                                                            | Presenting Bank     | AN   | 24   | 103-126 | Presenting Bank Name - The bank on which       |
|     |                                                                               | Name                |      |      |         | the draft is drawn                             |
|     | 14                                                                            | Block Receipts      | A    | 1    | 127     | Blank=Regular Receipt Batch                    |
|     |                                                                               |                     |      |      |         | Y=Block Receipt Batch                          |
|     | 15                                                                            | Receipt Count       | N    | 6    | 128-133 | Count of receipts in Draft                     |
|     | 16                                                                            | Draft Control       | N    | 10   | 134-143 | EWR assigned number to flag the receipts in    |
|     |                                                                               | Number              |      |      |         | the draft                                      |
|     | 17                                                                            | Purchaser’s         | AN   | 7    | 144-150 | The Holder ID of the Purchaser’s bank.  Can    |
|     |                                                                               | Bank’s Holder ID    |      |      |         | be the same Bank ID as that of the seller      |

### Table 65

| collateral.  Using the Collateral Release Request (found under the Receive Option in the EWRPlus   |                       |                |      |      |        |                                                  |
|:---------------------------------------------------------------------------------------------------|:----------------------|:---------------|:-----|:-----|:-------|:-------------------------------------------------|
| software), the bank can easily take action on the request, such as release or return to subholder. |                       |                |      |      |        |                                                  |
| H                                                                                                  | EADER LAYOUT FOR HD92 |                |      |      |        | Record Size = 120                                |
|                                                                                                    | Field                 | Field Name     | Type | Size | Pos    | Description                                      |
|                                                                                                    | 1                     | Record Type    | A    | 1    | 1      | H=Header Record                                  |
|                                                                                                    | 2                     | Holder ID of   | AN   | 7    | 2-8    | Holder ID of Bank Holding the Receipts as        |
|                                                                                                    |                       | Bank           |      |      |        | Collateral                                       |
|                                                                                                    | 3                     | Batch          | N    | 4    | 9-12   | Batch Number assigned by Host                    |
|                                                                                                    |                       | Number         |      |      |        |                                                  |
|                                                                                                    | 4                     | Batch Type     | N    | 2    | 13-14  | 92=Collateral Release Request                    |
|                                                                                                    | 5                     | Batch Date     | N    | 8    | 15-22  | Date batch was created; MMDDYYYY                 |
|                                                                                                    | 6                     | Batch Time     | N    | 6    | 23-28  | Time batch was created; HHMMSS                   |
|                                                                                                    | 7                     | Release        | AN   | 10   | 29-38  | A collateral release number assigned by the      |
|                                                                                                    |                       | Number         |      |      |        | Host to cross reference acknowledgments          |
|                                                                                                    | 8                     | Holder ID of   | AN   | 7    | 39-45  | Holder ID of Merchant requesting the release of  |
|                                                                                                    |                       | Requestor /    |      |      |        | collateral                                       |
|                                                                                                    |                       | Subhoder       |      |      |        |                                                  |
|                                                                                                    | 9                     | Tracking       | AN   | 10   | 46-55  | An optional entry to be entered by the           |
|                                                                                                    |                       | Code/Number    |      |      |        | subholder/merchant for referencing collateral    |
|                                                                                                    |                       |                |      |      |        | release requests, entered in Batch Type 22       |
|                                                                                                    | 10                    | To Holder ID   | AN   | 7    | 56-62  | Holder ID of the party which is to receive       |
|                                                                                                    |                       |                |      |      |        | Holdership.  This could be the same holder ID of |
|                                                                                                    |                       |                |      |      |        | the From Holder ID                               |
|                                                                                                    | 11                    | Block Receipts | A    | 1    | 63     | Y=Block Receipts Batch                           |
|                                                                                                    |                       |                |      |      |        | Blank=Regular Receipts Batch                     |
|                                                                                                    | 12                    | Filler         | A    | 57   | 64-120 | Reserved for EWR, Inc. use                       |

### Table 66

| D   | ETAIL LAYOUT FOR HD92   |              |      |      |        |                                                  |
|:----|:------------------------|:-------------|:-----|:-----|:-------|:-------------------------------------------------|
|     | Field                   | Field Name   | Type | Size | Pos    | Description                                      |
|     | 1                       | Record Type  | A    | 1    | 1      | D=Detail Record                                  |
|     | 2                       | Warehouse    | N    | 6    | 2-7    | Warehouse Code of the Receipt                    |
|     |                         | Code         |      |      |        |                                                  |
|     | 3                       | Electronic   | N    | 7    | 8-14   | Electronic Receipt Number                        |
|     |                         | Receipt      |      |      |        |                                                  |
|     |                         | Number       |      |      |        |                                                  |
|     | 4                       | Crop Year    | N    | 4    | 15-18  | YYYY                                             |
|     | 5                       | Filler       | A    | 102  | 19-120 | Reserved for EWR, Inc. use                       |
| T   | RAILER LAYOUT FOR HD92  |              |      |      |        |                                                  |
|     | Field                   | Field Name   | Type | Size | Pos    | Description                                      |
|     | 1                       | Record Type  | A    | 1    | 1      | T=Trailer Record                                 |
|     | 2                       | Holder ID    | AN   | 7    | 2-8    | Must be the same as entered in batch header      |
|     | 3                       | Batch Number | N    | 4    | 9-12   | Must be the same as entered in batch header      |
|     | 4                       | Record Count | N    | 9    | 13-21  | Control total record count of the detail records |
|     |                         |              |      |      |        | in the batch                                     |
|     | 5                       | Hash Total   | N    | 15   | 22-36  | Electronic receipt number hash total             |
|     | 6                       | Filler       | A    | 84   | 37-120 | Reserved for EWR, Inc. use                       |

### Table 67

| days have elapsed.     |                       |                |      |      |        |                                                  |
|:-----------------------|:----------------------|:---------------|:-----|:-----|:-------|:-------------------------------------------------|
| H                      | EADER LAYOUT FOR HD97 |                |      |      |        | Record Size = 120                                |
|                        | Field                 | Field Name     | Type | Size | Pos    | Description                                      |
|                        | 1                     | Record Type    | A    | 1    | 1      | H = Header Record                                |
|                        | 2                     | Holder ID      | AN   | 7    | 2-8    |                                                  |
|                        | 3                     | Batch Number   | N    | 4    | 9-12   | Batch number, holder supplied                    |
|                        | 4                     | Batch Type     | N    | 2    | 13-14  | 97                                               |
|                        | 5                     | Filler         | AN   | 13   | 15-27  | Reserved for EWR Inc. use                        |
|                        | 6                     | Batch Date     | N    | 8    | 28-35  | Holder supplied batch time; MMDDYYYY             |
|                        | 7                     | Batch Time     | N    | 6    | 36-41  | Holder supplied batch time; HHMMSS               |
|                        | 8                     | Early Warning  | A    | 1    | 42-43  | Y=Early Warning report.  Field will be blank for |
|                        |                       |                |      |      |        | out of compliance reports (free option).         |
|                        | 9                     | Filler         | AN   | 79   | 44-120 | Reserved for EWR Inc. use                        |
| DETAIL LAYOUT FOR HD97 |                       |                |      |      |        |                                                  |
|                        | Field                 | Field Name     | Type | Size | Pos    | Description                                      |
|                        | 1                     | Record Type    | A    | 1    | 1      | D=Detail Record                                  |
|                        | 2                     | Warehouse ID   | N    | 6    | 2-7    |                                                  |
|                        | 3                     | Shipper ID     | AN   | 7    | 8-14   | Shipper ID on the shipping order                 |
|                        | 4                     | Mark           | N    | 8    | 15-22  |                                                  |
|                        | 5                     | Order Number   | N    | 10   | 23-32  |                                                  |
|                        | 6                     | Received Date  | N    | 8    | 33-40  | Date 21 / 31 / 23 file received by EWR           |
|                        | 7                     | Batch Type     | N    | 2    | 41-42  | 21 / 23 / 31  = Batch Type indicator             |
|                        | 8                     | Requested Date | N    | 8    | 43-50  | Shipper Requested Date from 31 / 21 / 23         |
|                        | 9                     | Scheduled Date | N    | 8    | 51-58  | Warehouse Scheduled Date (if on file)            |

### Table 68

| TRAILER LAYOUT FOR HD97   |              |      |      |        |                                         |
|:--------------------------|:-------------|:-----|:-----|:-------|:----------------------------------------|
| Field                     | Field Name   | Type | Size | Pos    | Description                             |
| 1                         | Record Type  | A    | 1    | 1      | T=Trailer Record                        |
| 2                         | Holder ID    | AN   | 7    | 2-8    | Holder ID who sent the batch            |
| 3                         | Batch Number | N    | 4    | 9-12   | The same as enter in the header record. |
| 4                         | Record Count | N    | 9    | 13-21  | Number of receipts                      |
| 5                         | Filler       | A    | 9    | 22-30  | Reserved for EWR, Inc. use              |
| 6                         | Filler       | A    | 15   | 31-45  | Reserved for EWR, Inc. use              |
| 7                         | Filler       | A    | 75   | 46-120 | Reserved for EWR Inc. use               |

### Table 69

| receipts for a specific holder or subholder.  It is normally produced at the end of a month or year, upon   |                       |               |      |      |         |                                              |
|:------------------------------------------------------------------------------------------------------------|:----------------------|:--------------|:-----|:-----|:--------|:---------------------------------------------|
| request by a holder. There is a fee for each report.                                                        |                       |               |      |      |         |                                              |
| H                                                                                                           | EADER LAYOUT FOR HD98 |               |      |      |         | Record Size = 120                            |
|                                                                                                             | Field                 | Field Name    | Type | Size | Pos     | Description                                  |
|                                                                                                             | 1                     | Record Type   | A    | 1    | 1       | H = Header Record                            |
|                                                                                                             | 2                     | Holder ID     | AN   | 7    | 2-8     | Holder ID who sent the batch                 |
|                                                                                                             | 3                     | Batch Number  | N    | 4    | 9-12    | Batch number, holder supplied                |
|                                                                                                             | 4                     | Batch Type    | N    | 2    | 13-14   | 66                                           |
|                                                                                                             | 5                     | Activity      | AN   | 11   | 15-25   |                                              |
|                                                                                                             | 6                     | Action Code   | AN   | 1    | 26      | W=Warehouse Reconciliation                   |
|                                                                                                             |                       |               |      |      |         | H = Holder only receipts in 98 file          |
|                                                                                                             |                       |               |      |      |         | S = Subholder only and not on shipping order |
|                                                                                                             |                       |               |      |      |         | X = Subholder including receipts under order |
|                                                                                                             | 7                     | Filler        | A    | 1    | 27      | Reserved for EWR Inc., use                   |
|                                                                                                             | 8                     | Batch Date    | N    | 8    | 28-35   | Holder supplied batch time; MMDDYYYY         |
|                                                                                                             | 9                     | Batch Time    | N    | 6    | 36-41   | Holder supplied batch time; HHMMSS           |
|                                                                                                             | 10                    | Filler        | AN   | 8    | 42-49   | Reserved for EWR Inc. use                    |
|                                                                                                             | 11                    | Filler        | AN   | 53   | 50-102  | Reserved for EWR Inc. use                    |
|                                                                                                             | 12                    | Receipt Count | N    | 6    | 103-108 | Number of receipts in file                   |
|                                                                                                             | 13                    | Filler        | AN   | 12   | 109-120 | Reserved for EWR, Inc. use                   |

### Table 70

| 12   | Classing Paid      | A   | 1   | 40      | Y=Paid; N=Not paid                              |
|:-----|:-------------------|:----|:----|:--------|:------------------------------------------------|
| 13   | Compression Paid   | A   | 1   | 41      | Y=Paid; N=Not paid                              |
| 14   | Reconcentrated     | A   | 1   | 42      | R=Bale is reconcentrated                        |
|      |                    |     |     |         | Space = Not reconcentrated                      |
| 15   | Previous           | N   | 6   | 43-48   | Code of previous warehouse – Entered only if    |
|      | Warehouse          |     |     |         | the bale is reconcentrated.                     |
| 16   | Previous Receipt   | N   | 7   | 49-55   | Warehouse receipt number from previous          |
|      | Number             |     |     |         | warehouse, entered for reconcentrated cotton    |
|      |                    |     |     |         | only                                            |
| 17   | Gin Code Number    | N   | 5   | 56-60   | USDA assigned code where the cotton was         |
|      |                    |     |     |         | ginned                                          |
| 18   | Gin Tag Number     | N   | 7   | 61-67   | Sequential tag number assigned by the gin       |
| 19   | Storage Paid       | N   | 8   | 68-75   | Storage paid through date; MMDDYYYY.  Last      |
|      | Through            |     |     |         | date that storage charges against the bale      |
|      |                    |     |     |         | were paid to the warehouse                      |
| 20   | Mark               | AN  | 8   | 76-83   | Shipper assigned mark                           |
| 21   | Locator ID         | AN  | 8   | 84-91   | Warehouse bale location                         |
| 22   | Electronic Receipt | A   | 1   | 92      | O=Open; C=Cancel; D=Deactivated; V=Void         |
|      | Status             |     |     |         |                                                 |
| 23   | Electronic Receipt | A   | 1   | 93      | E=Electronic                                    |
|      | Flag               |     |     |         | P = Paper                                       |
| 24   | Receipt Type       | A   | 1   | 94      | See Appendix D – Receipt Types in “Files Sent   |
|      |                    |     |     |         | to EWR” document.                               |
| 25   | Current Holder     | A   | 1   | 95      | M = Merchant                                    |
|      | Type               |     |     |         | W = Warehouse                                   |
|      |                    |     |     |         | G = Gin                                         |
|      |                    |     |     |         | Z = Coop                                        |
|      |                    |     |     |         | P = Producer                                    |
|      |                    |     |     |         | C = Government                                  |
|      |                    |     |     |         | B = Bank                                        |
| 26   | Loan Transfer      | A   | 1   | 96      | Y = Yes.  This bale was transferred while under |
|      |                    |     |     |         | loan (Reconcentrated Loan Transfer)             |
| 27   | Lot Number         | N   | 5   | 97-101  | ICE Lot number entered by warehouse             |
| 28   | Filler             | N   | 8   | 102-109 |                                                 |
| 29   | USDA Tenderable    | A   | 2   | 110-111 | AMS assigned                                    |
| 30   | Rain Grown         | A   | 1   | 112     | R = Rain grown; N = Not rain grown              |
| 31   | Under S/O          | A   | 1   | 113     | Y = Under open shipping order                   |
| 32   | Block Receipt      | A   | 1   | 114     | Is this receipt a block receipt                 |
| 33   | Block Bales        | N   | 5   | 115-119 | Number of bales on block                        |
| 34   | Is Stored Outside  | A   | 1   | 120     | Y/N                                             |

### Table 71

| T   | RAILER LAYOUT FOR HD98   |              |      |      |        |                                         |
|:----|:-------------------------|:-------------|:-----|:-----|:-------|:----------------------------------------|
|     | Field                    | Field Name   | Type | Size | Pos    | Description                             |
|     | 1                        | Record Type  | A    | 1    | 1      | T=Trailer Record                        |
|     | 2                        | Holder ID    | AN   | 7    | 2-8    | Holder ID who sent the batch            |
|     | 3                        | Batch Number | N    | 4    | 9-12   | The same as enter in the header record. |
|     | 4                        | Record Count | N    | 9    | 13-21  | Number of receipts                      |
|     | 5                        | Filler       | A    | 9    | 22-30  | Reserved for EWR, Inc. use              |
|     | 6                        | Filler       | A    | 15   | 31-45  | Reserved for EWR, Inc. use              |
|     | 7                        | Filler       | A    | 75   | 46-120 | Reserved for EWR Inc. use               |

### Table 72

| SECTION 4 FILE TYPE HA (SUCCESSFUL ACKNOWLEDGEMENT FILES)                                            |                                                                                                   |                                                 |     |
|:-----------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|:------------------------------------------------|:----|
| T                                                                                                    | his section explains how the EWR, Inc. host system handles successful acknowledgement files.      |                                                 |     |
| Successful acknowledgements are batches that completed with NO errors. There are 4 basic layouts for |                                                                                                   |                                                 |     |
| acknowledgement files:                                                                               |                                                                                                   |                                                 |     |
|                                                                                                      | •                                                                                                 | Type 85 (The standard, default layout)          |     |
|                                                                                                      | •                                                                                                 | Type 81 Collateral acknowledgement layout       |     |
|                                                                                                      | •                                                                                                 | Type 18 BMAS acknowledgement layout             |     |
|                                                                                                      | •                                                                                                 | Type 25/26 Phytosanitary acknowledgement layout |     |
| W                                                                                                    | hen the host generates acknowledgements, it consists of the following types lines:                |                                                 |     |
|                                                                                                      | •                                                                                                 | Batch Header (H)                                |     |
|                                                                                                      | •                                                                                                 | Acknowledgment (AC)                             |     |
|                                                                                                      | •                                                                                                 | Batch Trailer (T)                               |     |
| A                                                                                                    | cknowledgment s are received by all users who create and transmit batches to the host and in some |                                                 |     |
| cases by the users whose Holder IDs are involved in the transactions.                                |                                                                                                   |                                                 |     |
|                                                                                                      |                                                                                                   |                                                 | 4-1 |

### Table 73

| starts with HA21, then the sending batch was a type 21 batch (Shipping order). Excluding bank releases,   |              |                       |      |       |                                            |
|:----------------------------------------------------------------------------------------------------------|:-------------|:----------------------|:-----|:------|:-------------------------------------------|
| in that instance a bank release of shipping order is HA70, while a draft is HA71.                         |              |                       |      |       |                                            |
| H                                                                                                         | EADER LAYOUT |                       |      |       | Record Size = 120                          |
|                                                                                                           | Field        | Field Name            | Size | Pos   | Description                                |
|                                                                                                           |              | Type                  |      |       |                                            |
|                                                                                                           | 1            | Record Type           | 1    | 1     | H=Header Record                            |
|                                                                                                           |              | A                     |      |       |                                            |
|                                                                                                           | 2            | Holder ID             | 7    | 2-8   | Holder ID who will receiving               |
|                                                                                                           |              | AN                    |      |       |                                            |
|                                                                                                           |              |                       |      |       | acknowledgement                            |
|                                                                                                           | 3            | Batch Number          | 4    | 9-12  | Batch number of sending holder             |
|                                                                                                           |              | N                     |      |       |                                            |
|                                                                                                           | 4            | Batch Type            | 2    | 13-14 | 85                                         |
|                                                                                                           |              | N                     |      |       |                                            |
|                                                                                                           | 5            | Batch Date            | 8    | 15-22 | Holder supplied batch date; MMDDYYYY       |
|                                                                                                           |              | N                     |      |       |                                            |
|                                                                                                           | 6            | Batch Time            | 6    | 23-28 | Holder supplied batch time; HHMMSS         |
|                                                                                                           |              | N                     |      |       |                                            |
|                                                                                                           | 7            | Filler                | 1    | 29    | Reserved for EWR Inc. use                  |
|                                                                                                           |              | A                     |      |       |                                            |
|                                                                                                           | 8            | EWR ID                | 9    | 30-38 | Internal ID assigned by EWR, Inc           |
|                                                                                                           |              | N                     |      |       |                                            |
|                                                                                                           | 9            | Original Batch        | 4    | 39-42 | Valid only on bank release batches (70-72) |
|                                                                                                           |              | N                     |      |       |                                            |
|                                                                                                           |              | Number                |      |       |                                            |
|                                                                                                           | 10           | Original Batch        | 2    | 43-44 | Valid only on bank release batches (70-72) |
|                                                                                                           |              | N                     |      |       |                                            |
|                                                                                                           |              | Type                  |      |       |                                            |
|                                                                                                           | 11           | Sender                | 1    | 45    | Holder initiated the batch (Y/N)           |
|                                                                                                           |              | A                     |      |       |                                            |
| D                                                                                                         | ETAIL LAYOUT |                       |      |       | Record Size = 120                          |
|                                                                                                           | Field        | Field Name            | Type | Size  | Description                                |
|                                                                                                           |              |                       |      | Pos   |                                            |
|                                                                                                           | 1            | Record Type           | A    | 2     | AC=Acknowledgments                         |
|                                                                                                           |              |                       |      | 1-2   |                                            |
|                                                                                                           | 2            | Orig. Transmission    | N    | 6     | Transmission Number                        |
|                                                                                                           |              |                       |      | 3-8   |                                            |
|                                                                                                           |              | Number                |      |       |                                            |
|                                                                                                           | 3            | Date Acknowledged     | N    | 8     | Date Host Completed Batch Processing       |
|                                                                                                           |              |                       |      | 9-16  |                                            |
|                                                                                                           |              |                       |      |       | Request                                    |
|                                                                                                           | 4            | Time Acknowledged     | N    | 6     | Time Host Completed Batch Processing       |
|                                                                                                           |              |                       |      | 17-22 |                                            |
|                                                                                                           |              |                       |      |       | Request                                    |
|                                                                                                           | 5            | Original Batch Type   | N    | 2     | Batch Type (sent from PC to host)          |
|                                                                                                           |              |                       |      | 23-24 |                                            |
|                                                                                                           | 6            | Original Batch Number | N    | 4     | Batch Number (sent from PC to host)        |
|                                                                                                           |              |                       |      | 25-28 |                                            |

### Table 74

|    | 7             | From Holder ID         | AN   | 7    | 29-35   | Holder ID who sent batch                    |
|:---|:--------------|:-----------------------|:-----|:-----|:--------|:--------------------------------------------|
|    | 8             | From User ID           | AN   | 6    | 36-41   | User ID who sent batch                      |
|    | 9             | Name of From Holder    | AN   | 20   | 42-61   | Name of From Holder - stored in the host    |
|    |               |                        |      |      |         | control file, input by the host             |
|    | 10            | To Holder ID           | AN   | 7    | 62-68   | To Holder ID                                |
|    | 11            | Name of To Holder      | AN   | 20   | 69-88   | Name of To Holder - stored in the host      |
|    |               |                        |      |      |         | control file, input by the host             |
|    | 12            | Activity ID            | AN   | 10   | 89-98   | Identifying characters such as SO number,   |
|    |               |                        |      |      |         | Mark, Draft #, CCC Collateral Release Code, |
|    |               |                        |      |      |         | EWR Container ID                            |
|    | 13            | Total Detail Records   | N    | 8    | 99-106  | Total detail records in batch sent to host  |
|    |               | Sent                   |      |      |         |                                             |
|    | 14            | Total Detail Processed | N    | 8    | 107-114 | Total detail records that processed in the  |
|    |               |                        |      |      |         | batch                                       |
|    | 15            | Action Flag            | A    | 1    | 115     | If field 5 is 34,35,38: C=Container created |
|    |               |                        |      |      |         | D=Container Dissolved                       |
|    |               |                        |      |      |         | Otherwise:                                  |
|    |               |                        |      |      |         | B=Block Receipts (HA71 B= Pending           |
|    |               |                        |      |      |         | Release)                                    |
|    |               |                        |      |      |         | R=Regular or Release if HA70 or HA71        |
|    |               |                        |      |      |         | C=Bank holds collateral (buyer becomes      |
|    |               |                        |      |      |         | subholder)                                  |
|    |               |                        |      |      |         | T=Returned to seller or Rejected by Bank;   |
|    |               |                        |      |      |         | S=Sent to CCC for Loan Approval – Batch 53  |
|    |               |                        |      |      |         | A=Approved by CCC for loan – Batch 53       |
|    |               |                        |      |      |         | N=No Download (Batch 50 only)               |
|    |               |                        |      |      |         | L=Loan Option Delivery (Batch 63 only)      |
|    |               |                        |      |      |         | U=Warehouse updating Locator ID (Batch      |
|    |               |                        |      |      |         | 03 & 04 only)                               |
|    | 16            | Bale Count             | A    | 5    | 116-120 | Number of bales/receipts (not records) in   |
|    |               |                        |      |      |         | the batch                                   |
| T  | RAILER LAYOUT |                        |      |      |         |                                             |
|    | Field         | Field Name             | Type | Size | Pos     | Description                                 |
|    | 1             | Record Type            | A    | 1    | 1       | T=Trailer                                   |
|    | 2             | Holder ID              | AN   | 7    | 2-8     | Holder ID receiving acknowledgement         |
|    | 3             | Batch Number           | N    | 4    | 9-12    | Batch number assigned                       |
|    | 4             | Record Count           | N    | 9    | 13-21   | Number of receipts                          |
|    | 5             | Filler                 | A    | 9    | 22-120  | Reserved for EWR Inc., use                  |

### Table 75

| ID.  The HA18 provides the final BMAS in the last field “BMAS Bale Count”.  Also, the individual numbers   |              |                        |      |       |                                          |
|:-----------------------------------------------------------------------------------------------------------|:-------------|:-----------------------|:-----|:------|:-----------------------------------------|
| used to calculate the final BMAS number are provided in this acknowledgement file.                         |              |                        |      |       |                                          |
| H                                                                                                          | EADER LAYOUT |                        |      |       | Record Size = 120                        |
|                                                                                                            | Field        | Field Name             | Size | Pos   | Description                              |
|                                                                                                            |              | Type                   |      |       |                                          |
|                                                                                                            | 1            | Record Type            | 1    | 1     | H=Header Record                          |
|                                                                                                            |              | A                      |      |       |                                          |
|                                                                                                            | 2            | Holder ID              | 7    | 2-8   | Holder ID who will receiving             |
|                                                                                                            |              | AN                     |      |       |                                          |
|                                                                                                            |              |                        |      |       | acknowledgement                          |
|                                                                                                            | 3            | Batch Number           | 4    | 9-12  | Batch number of sending holder           |
|                                                                                                            |              | N                      |      |       |                                          |
|                                                                                                            | 4            | Batch Type             | 2    | 13-14 | 18                                       |
|                                                                                                            |              | N                      |      |       |                                          |
|                                                                                                            | 5            | Batch Date             | 8    | 15-22 | Holder supplied batch date; MMDDYYYY     |
|                                                                                                            |              | N                      |      |       |                                          |
|                                                                                                            | 6            | Batch Time             | 6    | 23-28 | Holder supplied batch time; HHMMSS       |
|                                                                                                            |              | N                      |      |       |                                          |
|                                                                                                            | 7            | Filler                 | 1    | 29    | Reserved for EWR Inc. use                |
|                                                                                                            |              | A                      |      |       |                                          |
|                                                                                                            | 8            | Filler                 | 9    | 30-38 | Reserved for EWR Inc. use                |
|                                                                                                            |              | N                      |      |       |                                          |
|                                                                                                            | 9            | Filler                 | 4    | 39-42 | Reserved for EWR Inc. use                |
|                                                                                                            |              | N                      |      |       |                                          |
|                                                                                                            | 10           | Filler                 | 2    | 43-44 | Reserved for EWR Inc. use                |
|                                                                                                            |              | N                      |      |       |                                          |
|                                                                                                            | 11           | Filler                 | 1    | 45    | Reserved for EWR Inc. use                |
|                                                                                                            |              | A                      |      |       |                                          |
| D                                                                                                          | ETAIL LAYOUT |                        |      |       | Record Size = 120                        |
|                                                                                                            | Field        | Field Name             | Type | Size  | Description                              |
|                                                                                                            |              |                        |      | Pos   |                                          |
|                                                                                                            | 1            | Record Type            | A    | 2     | AC=Acknowledgments                       |
|                                                                                                            |              |                        |      | 1-2   |                                          |
|                                                                                                            | 2            | Filler                 | N    | 6     | Transmission Number                      |
|                                                                                                            |              |                        |      | 3-8   |                                          |
|                                                                                                            | 3            | Date Acknowledged      | N    | 8     | Date Host Completed Batch Processing     |
|                                                                                                            |              |                        |      | 9-16  |                                          |
|                                                                                                            |              |                        |      |       | Request                                  |
|                                                                                                            | 4            | Time Acknowledged      | N    | 6     | Time Host Completed Batch Processing     |
|                                                                                                            |              |                        |      | 17-22 |                                          |
|                                                                                                            |              |                        |      |       | Request                                  |
|                                                                                                            | 5            | Original Batch Type    | N    | 2     | Batch Type (sent from PC to host)        |
|                                                                                                            |              |                        |      | 23-24 |                                          |
|                                                                                                            | 6            | Original Batch Number  | N    | 4     | Batch Number (sent from PC to host)      |
|                                                                                                            |              |                        |      | 25-28 |                                          |
|                                                                                                            | 7            | From Holder ID         | AN   | 7     | Holder ID who sent batch                 |
|                                                                                                            |              |                        |      | 29-35 |                                          |
|                                                                                                            | 8            | From User ID           | AN   | 6     | User ID who sent batch                   |
|                                                                                                            |              |                        |      | 36-41 |                                          |
|                                                                                                            | 9            | Name of From Holder    | AN   | 20    | Name of From Holder - stored in the host |
|                                                                                                            |              |                        |      | 42-61 |                                          |
|                                                                                                            |              |                        |      |       | control file, input by the host          |
|                                                                                                            | 10           | Flow Reporting Date    | N    | 8     | Sent by Warehouse in Batch 18 Header     |
|                                                                                                            |              |                        |      | 62-69 |                                          |
|                                                                                                            | 11           | Total Bales Not Picked | N    | 5     | Sent by Warehouse when submitting flow   |
|                                                                                                            |              |                        |      | 70-74 |                                          |
|                                                                                                            |              | Up                     |      |       | report                                   |
|                                                                                                            | 12           | Total Bales Shipped    | N    | 5     | Sent by Warehouse when submitting flow   |
|                                                                                                            |              |                        |      | 75-79 |                                          |
|                                                                                                            |              |                        |      |       | report                                   |
|                                                                                                            | 13           | Total Previously       | N    | 5     | Calculated when 18 is processed.         |
|                                                                                                            |              |                        |      | 80-84 |                                          |
|                                                                                                            |              | Reported Bales         |      |       | Previously reported bale within past 12  |
|                                                                                                            |              |                        |      |       | months                                   |

### Table 76

|    | 10           | Filler                 | 2    | 43-44   | Reserved for EWR Inc. use                |
|    |              | N                      |      |         |                                          |
|:---|:-------------|:-----------------------|:-----|:--------|:-----------------------------------------|
|    | 11           | Filler                 | 1    | 45      | Reserved for EWR Inc. use                |
|    |              | A                      |      |         |                                          |
| D  | ETAIL LAYOUT |                        |      |         | Record Size = 120                        |
|    | Field        | Field Name             | Type | Size    | Description                              |
|    |              |                        |      | Pos     |                                          |
|    | 1            | Record Type            | A    | 2       | AC=Acknowledgments                       |
|    |              |                        |      | 1-2     |                                          |
|    | 2            | Filler                 | N    | 6       | Transmission Number                      |
|    |              |                        |      | 3-8     |                                          |
|    | 3            | Date Acknowledged      | N    | 8       | Date Host Completed Batch Processing     |
|    |              |                        |      | 9-16    |                                          |
|    |              |                        |      |         | Request                                  |
|    | 4            | Time Acknowledged      | N    | 6       | Time Host Completed Batch Processing     |
|    |              |                        |      | 17-22   |                                          |
|    |              |                        |      |         | Request                                  |
|    | 5            | Original Batch Type    | N    | 2       | Batch Type (sent from PC to host)        |
|    |              |                        |      | 23-24   |                                          |
|    | 6            | Original Batch Number  | N    | 4       | Batch Number (sent from PC to host)      |
|    |              |                        |      | 25-28   |                                          |
|    | 7            | From Holder ID         | AN   | 7       | Holder ID who sent batch                 |
|    |              |                        |      | 29-35   |                                          |
|    | 8            | From User ID           | AN   | 6       | User ID who sent batch                   |
|    |              |                        |      | 36-41   |                                          |
|    | 9            | Name of From Holder    | AN   | 20      | Name of From Holder - stored in the host |
|    |              |                        |      | 42-61   |                                          |
|    |              |                        |      |         | control file, input by the host          |
|    | 10           | Flow Reporting Date    | N    | 8       | Sent by Warehouse in Batch 18 Header     |
|    |              |                        |      | 62-69   |                                          |
|    | 11           | Total Bales Not Picked | N    | 5       | Sent by Warehouse when submitting flow   |
|    |              |                        |      | 70-74   |                                          |
|    |              | Up                     |      |         | report                                   |
|    | 12           | Total Bales Shipped    | N    | 5       | Sent by Warehouse when submitting flow   |
|    |              |                        |      | 75-79   |                                          |
|    |              |                        |      |         | report                                   |
|    | 13           | Total Previously       | N    | 5       | Calculated when 18 is processed.         |
|    |              |                        |      | 80-84   |                                          |
|    |              | Reported Bales         |      |         | Previously reported bale within past 12  |
|    |              |                        |      |         | months                                   |

### Table 77

|    | 14            | Bales In Error           | N    | 5    | 85-89   | Bales that resulted in an error code      |
|:---|:--------------|:-------------------------|:-----|:-----|:--------|:------------------------------------------|
|    | 15            | Effective Capacity       | N    | 6    | 90-95   | Current warehouse effective capacity as   |
|    |               |                          |      |      |         | recorded on the provider system           |
|    | 16            | Filler                   | A    | 3    | 96-98   |                                           |
|    | 17            | Total Details Rec Sent   | N    | 8    | 99-106  | (Same position as default HA)             |
|    | 18            | Total Detail Rec Process | N    | 8    | 107-114 | (Same position as default HA)             |
|    | 19            | Filler                   | N    | 1    | 115     |                                           |
|    | 20            | BMAS Bale Count          | N    | 5    | 116-120 | Final BMAS – Calculated when 18 is        |
|    |               |                          |      |      |         | processed.  (Total Shipped + Total Not    |
|    |               |                          |      |      |         | Picked Up) – (Previously Reported + Bales |
|    |               |                          |      |      |         | In Error)                                 |
| T  | RAILER LAYOUT |                          |      |      |         |                                           |
|    | Field         | Field Name               | Type | Size | Pos     | Description                               |
|    | 1             | Record Type              | A    | 1    | 1       | T=Trailer                                 |
|    | 2             | Holder ID                | AN   | 7    | 2-8     | Holder ID receiving acknowledgement       |
|    | 3             | Batch Number             | N    | 4    | 9-12    | Batch number assigned                     |
|    | 4             | Record Count             | N    | 9    | 13-21   | Number of receipts                        |
|    | 5             | Filler                   | A    | 9    | 22-120  | Reserved for EWR Inc., use                |

### Table 78

|                                                                                                    | 5                           | Filler   | A   | 9   | 22-120   | Reserved for EWR Inc., use   |
|:---------------------------------------------------------------------------------------------------|:----------------------------|:---------|:----|:----|:---------|:-----------------------------|
| C                                                                                                  | alculating Flow Percentage: |          |     |     |          |                              |
| To calculate the warehouse flow percentage, divide the BMAS Bale Count (Field 20) by the Effective |                             |          |     |     |          |                              |
| Capacity (Field 15), then multiply by 100.                                                         |                             |          |     |     |          |                              |
| E                                                                                                  | xample:                     |          |     |     |          |                              |
| Effective Capacity = 50,000                                                                        |                             |          |     |     |          |                              |
| BMAS Bale Count = 2,250                                                                            |                             |          |     |     |          |                              |
| 2                                                                                                  | 250 / 50000 = 0.045         |          |     |     |          |                              |
| 0.045 x 100 = 4.5%                                                                                 |                             |          |     |     |          |                              |

### Table 79

| involved their Holder ID.  This acknowledgment is received by the merchant. A summary of the   |                                  |                                                                                        |
|:-----------------------------------------------------------------------------------------------|:---------------------------------|:---------------------------------------------------------------------------------------|
| acknowledgment is as follows:                                                                  |                                  |                                                                                        |
| B                                                                                              | atch Type 25 AC to the Merchant: |                                                                                        |
|                                                                                                | •                                | “From Holder” will be the merchant (buyer’s) Holder ID.                                |
|                                                                                                | •                                | “EWR Tracking Number” is the unique EWR assigned number assigned to each phytosanitary |
|                                                                                                |                                  | request. This number should be saved by the merchant and referenced when sending any   |
|                                                                                                |                                  | updates or cancels for phyto request.                                                  |
| B                                                                                              | atch Type 26 AC to the Merchant: |                                                                                        |
|                                                                                                | •                                | “From Holder” will be the warehouses Holder ID.                                        |
|                                                                                                | •                                | “EWR Tracking Number” is the unique EWR assigned number assigned to each phytosanitary |
|                                                                                                |                                  | request.                                                                               |

### Table 80

| 11            | Sender       | A    | 1    | 60     |
|:--------------|:-------------|:-----|:-----|:-------|
| 11            | Filler       | A    | 1    | 61-120 |
| DETAIL LAYOUT |              |      |      |        |
| Field         | Field Name   | Type | Size | Pos    |
| 1             | Record Type  | A    | 2    | 1-2    |
| 2             | Filler       | N    | 6    | 3-8    |
| 3             | Date         | N    | 8    | 9-16   |
|               | Acknowledged |      |      |        |
| 4             | Time         | N    | 6    | 17-22  |
|               | Acknowledged |      |      |        |
| 5             | From Holder  | AN   | 7    | 23-29  |
|               | ID           |      |      |        |

### Table 81

|    | •             | “EWR Tracking Number” is the unique EWR assigned number assigned to each phytosanitary   |      |      |        |                                           |
|:---|:--------------|:-----------------------------------------------------------------------------------------|:-----|:-----|:-------|:------------------------------------------|
|    |               | request.                                                                                 |      |      |        |                                           |
| H  | EADER LAYOUT  |                                                                                          |      |      |        | Record Size = 120                         |
|    | Field         | Field Name                                                                               | Type | Size | Pos    | Description                               |
|    | 1             | Record Type                                                                              | A    | 1    | 1      | H=Header Record                           |
|    | 2             | Holder ID                                                                                | AN   | 7    | 2-8    | Holder ID who will receiving              |
|    |               |                                                                                          |      |      |        | acknowledgement                           |
|    | 3             | Batch Number                                                                             | N    | 4    | 9-12   | Batch number of sending holder            |
|    | 4             | Batch Type                                                                               | N    | 2    | 13-14  | 25/26                                     |
|    | 5             | Batch Date                                                                               | N    | 8    | 15-22  | Holder supplied batch date; MMDDYYYY      |
|    | 6             | Batch Time                                                                               | N    | 6    | 23-28  | Holder supplied batch time; HHMMSS        |
|    | 7             | From User                                                                                | AN   | 6    | 29-34  | User ID that sent batch                   |
|    | 8             | EWR Trans ID                                                                             | N    | 9    | 35-43  | EWR Transaction ID                        |
|    | 9             | Records Sent                                                                             | N    | 8    | 44-51  | Total detail records sent to host         |
|    | 10            | Records Process                                                                          | N    | 8    | 52-59  | Total detail records processed            |
|    | 11            | Sender                                                                                   | A    | 1    | 60     | Holder initiated the batch (Y/N)          |
|    | 11            | Filler                                                                                   | A    | 1    | 61-120 | Reserved for EWR, Inc. use                |
|    | DETAIL LAYOUT |                                                                                          |      |      |        | Record Size = 120                         |
|    | Field         | Field Name                                                                               | Type | Size | Pos    | Description                               |
|    | 1             | Record Type                                                                              | A    | 2    | 1-2    | AC=Acknowledgments                        |
|    | 2             | Filler                                                                                   | N    | 6    | 3-8    | Reserved for EWR, Inc. use                |
|    | 3             | Date                                                                                     | N    | 8    | 9-16   | Date Host Completed Batch Processing      |
|    |               | Acknowledged                                                                             |      |      |        | Request                                   |
|    | 4             | Time                                                                                     | N    | 6    | 17-22  | Time Host Completed Batch Processing      |
|    |               | Acknowledged                                                                             |      |      |        | Request                                   |
|    | 5             | From Holder                                                                              | AN   | 7    | 23-29  | Holder ID who sent batch (sent from PC to |
|    |               | ID                                                                                       |      |      |        | host)                                     |

### Table 82

|    | 6                      | Name of From   | AN   | 17   | 30-46                                         |
|    |                        |                |      |      | Name of From Holder – stored in the host      |
|:---|:-----------------------|:---------------|:-----|:-----|:----------------------------------------------|
|    |                        | Holder         |      |      | control file, input by the host               |
|    | 7                      | Forwarder      | AN   | 7    | 47-53                                         |
|    |                        |                |      |      | Holder ID of Freight Forwarder                |
|    |                        | Holder ID      |      |      |                                               |
|    | 8                      | Forwarder      | AN   | 17   | 54-70                                         |
|    |                        |                |      |      | Name of Forwarder                             |
|    |                        | Name           |      |      |                                               |
|    | 9                      | EWR Tracking   | N    | 8    | 71-78                                         |
|    |                        |                |      |      | Unique tracking number assigned by EWR to     |
|    |                        | Number         |      |      | each phyto request (per whse)                 |
|    | 10                     | Total Marks    | N    | 2    | 79-80                                         |
|    |                        |                |      |      | Total number of marks on phyto                |
|    | 11                     | Bale Count     | N    | 5    | 81-85                                         |
|    |                        |                |      |      | Number of bales/receipts (not records) in the |
|    |                        |                |      |      | batch.                                        |
|    | 12                     | Warehouse ID   | N    | 8    | 86-91                                         |
|    |                        |                |      |      | Warehouse inspecting phyto                    |
|    | 13                     | Warehouse      | AN   | 17   | 92-108                                        |
|    |                        | Name           |      |      |                                               |
|    | 14                     | Activity ID    | A    | 10   | 109-118                                       |
|    | 15                     | Filler         | AN   | 2    | 119-120                                       |
|    |                        |                |      |      | Reserved for EWR, Inc. use                    |
| T  | RAILER LAYOUT FOR HA81 |                |      |      |                                               |
|    | Field                  | Field Name     |      | Type | Size                                          |
|    |                        |                |      |      | Pos                                           |
|    |                        |                |      |      | Description                                   |
|    | 1                      | Record Type    |      | A    | 1                                             |
|    |                        |                |      |      | 1                                             |
|    |                        |                |      |      | T=Trailer                                     |
|    | 2                      | Holder ID      |      | AN   | 7                                             |
|    |                        |                |      |      | 2-8                                           |
|    |                        |                |      |      | Holder ID receiving acknowledgement           |
|    | 3                      | Batch Number   |      | N    | 4                                             |
|    |                        |                |      |      | 9-12                                          |
|    |                        |                |      |      | Batch number assigned                         |
|    | 4                      | Record Count   |      | N    | 9                                             |
|    |                        |                |      |      | 13-21                                         |
|    |                        |                |      |      | Number of receipts                            |
|    | 5                      | Filler         |      | A    | 9                                             |
|    |                        |                |      |      | 22-120                                        |
|    |                        |                |      |      | Reserved for EWR Inc., use                    |

### Table 83

| HA81 - Collateral Holder Acknowledgment                                                              |
|:-----------------------------------------------------------------------------------------------------|
| (This acknowledgment is received by collateralized merchants and their banks)                        |
| H                                                                                                    |
| olders can designate if they want a Bank to automatically receive holdership of ALL receipts         |
| transferred to their Holder ID number.  For example, if a merchant uses warehouse receipts for       |
| collateral, anytime another user sends receipts to the merchants Holder ID number, the host will     |
| process the batch and immediately change holdership to the Bank’s Holder ID number and move the      |
| merchant (buyer) to the subholder field.                                                             |
| B                                                                                                    |
| atch Type 81 is an acknowledgment sent to users to inform them of the status of batches which        |
| involved their Holder ID.  This acknowledgment is received by the merchant and by the bank who holds |
| the receipts as collateral.  A summary of the acknowledgment is as follows:                          |

### Table 84

| involved their Holder ID.  This acknowledgment is received by the merchant and by the bank who holds   |                                  |                                                                                        |
|:-------------------------------------------------------------------------------------------------------|:---------------------------------|:---------------------------------------------------------------------------------------|
| the receipts as collateral.  A summary of the acknowledgment is as follows:                            |                                  |                                                                                        |
| B                                                                                                      | atch Type 81 AC to the Merchant: |                                                                                        |
|                                                                                                        | •                                | “From Holder” will be the Holder who delivered/transferred holdership to the merchant. |
|                                                                                                        | •                                | “To Holder” will be the merchant (buyer’s) Holder ID.                                  |
|                                                                                                        | •                                | “Collateral Holder” will be the bank’s Holder ID.                                      |
| B                                                                                                      | atch Type 81 AC to the Bank:     |                                                                                        |
|                                                                                                        | •                                | “From Holder” will be the Holder who delivered/transferred holdership to the merchant. |
|                                                                                                        | •                                | “To Holder” will be the bank’s Holder ID.                                              |
|                                                                                                        | •                                | “Collateral Holder” will be the merchant (buyer’s) Holder ID.                          |

### Table 85

|    | •                      | “To Holder” will be the bank’s Holder ID.                     |      |      |        |                                      |
|:---|:-----------------------|:--------------------------------------------------------------|:-----|:-----|:-------|:-------------------------------------|
|    | •                      | “Collateral Holder” will be the merchant (buyer’s) Holder ID. |      |      |        |                                      |
| H  | EADER LAYOUT FOR HA81  |                                                               |      |      |        | Record Size = 120                    |
|    | Field                  | Field Name                                                    | Type | Size | Pos    | Description                          |
|    | 1                      | Record Type                                                   | A    | 1    | 1      | H=Header Record                      |
|    | 2                      | Holder ID                                                     | AN   | 7    | 2-8    | Holder ID who will receiving         |
|    |                        |                                                               |      |      |        | acknowledgement                      |
|    | 3                      | Batch Number                                                  | N    | 4    | 9-12   | Batch number of sending holder       |
|    | 4                      | Batch Type                                                    | N    | 2    | 13-14  | 81                                   |
|    | 5                      | Batch Date                                                    | N    | 8    | 15-22  | Holder supplied batch date; MMDDYYYY |
|    | 6                      | Batch Time                                                    | N    | 6    | 23-28  | Holder supplied batch time; HHMMSS   |
|    | 7                      | Filler                                                        | A    | 1    | 29-120 | Reserved for EWR Inc. use            |
|    | DETAIL LAYOUT FOR HA81 |                                                               |      |      |        | Record Size = 120                    |
|    | Field                  | Field Name                                                    | Ty   | Size | Pos    | Description                          |
|    |                        |                                                               | pe   |      |        |                                      |
|    | 1                      | Record Type                                                   | A    | 2    | 1-2    | AC=Acknowledgments                   |
|    | 2                      | Originating                                                   | N    | 6    | 3-8    | Transmission Number                  |
|    |                        | Transmission                                                  |      |      |        |                                      |
|    |                        | Number                                                        |      |      |        |                                      |
|    | 3                      | Date                                                          | N    | 8    | 9-16   | Date Host Completed Batch Processing |
|    |                        | Acknowledged                                                  |      |      |        | Request                              |

### Table 86

| 6     | Batch Time             | N   | 6    | 23-28   | Holder supplied batch time; HHMMSS   |
|:------|:-----------------------|:----|:-----|:--------|:-------------------------------------|
| 7     | Filler                 | A   | 1    | 29-120  | Reserved for EWR Inc. use            |
|       | DETAIL LAYOUT FOR HA81 |     |      |         | Record Size = 120                    |
| Field | Field Name             | Ty  | Size | Pos     | Description                          |
|       |                        | pe  |      |         |                                      |
| 1     | Record Type            | A   | 2    | 1-2     | AC=Acknowledgments                   |
| 2     | Originating            | N   | 6    | 3-8     | Transmission Number                  |
|       | Transmission           |     |      |         |                                      |
|       | Number                 |     |      |         |                                      |
| 3     | Date                   | N   | 8    | 9-16    | Date Host Completed Batch Processing |
|       | Acknowledged           |     |      |         | Request                              |

### Table 87

| 4   | Time           | N   | 6   | 17-22   | Time Host Completed Batch Processing          |
|:----|:---------------|:----|:----|:--------|:----------------------------------------------|
|     | Acknowledged   |     |     |         | Request                                       |
| 5   | Original Batch | N   | 2   | 23-24   | Batch Type (sent from PC to host)             |
|     | Type           |     |     |         |                                               |
| 6   | Original Batch | N   | 4   | 25-28   | Batch number (sent from PC to host)           |
|     | Number         |     |     |         |                                               |
| 7   | From Holder ID | AN  | 7   | 29-35   | Holder ID who sent batch (sent from PC to     |
|     |                |     |     |         | host)                                         |
| 8   | From User ID   | AN  | 6   | 36-41   | User ID who sent batch (sent from PC to host) |
| 9   | Name of From   | AN  | 17  | 42-58   | Name of From Holder – stored in the host      |
|     | Holder         |     |     |         | control file, input by the host               |
| 10  | To Holder ID   | AN  | 7   | 59-65   | Holder ID of Bank which became the holder of  |
|     |                |     |     |         | the receipts *the To Holder ID will change    |
|     |                |     |     |         | from the Bank’s ID to the Subholder ID to     |
|     |                |     |     |         | accomomodate the IBM Mail Handling            |
|     |                |     |     |         | System.  This change is necessary to ensure   |
|     |                |     |     |         | that the bank and the merchant receive an AC  |
| 11  | Name of To     | AN  | 17  | 66-82   | Name of Bank [To Holder] – stored in the host |
|     | Holder         |     |     |         | control file, input by the host.              |
| 12  | Collateral /   | AN  | 7   | 83-89   | Holder ID of Merchant who is the subholder of |
|     | Subholder ID   |     |     |         | the receipts *the Subholder ID will change    |
|     |                |     |     |         | from the Merchant’s ID to the Subholder ID to |
|     |                |     |     |         | accommodate the host system.  This change is  |
|     |                |     |     |         | necessary to ensure that the bank and the     |
|     |                |     |     |         | merchant receive an AC                        |
| 13  | Activity ID    | AN  | 10  | 90-99   | Identifying characters such as SO number,     |
|     |                |     |     |         | Mark, Draft #, etc.                           |
| 14  | Total Detail   | N   | 8   | 100-107 | Total detail records in batch sent to host    |
|     | Records Sent   |     |     |         |                                               |
| 15  | Total Detail   | N   | 8   | 108-115 | Total detail records that processed in the    |
|     | Processed      |     |     |         | batch                                         |
| 16  | Bale Count     | A   | 5   | 116-120 | Number of bales/receipts (not records) in the |
|     |                |     |     |         | batch.                                        |

### Table 88

| TRAILER LAYOUT FOR HA81   |              |      |      |        |                                     |
|:--------------------------|:-------------|:-----|:-----|:-------|:------------------------------------|
| Field                     | Field Name   | Type | Size | Pos    | Description                         |
| 1                         | Record Type  | A    | 1    | 1      | T=Trailer                           |
| 2                         | Holder ID    | AN   | 7    | 2-8    | Holder ID receiving acknowledgement |
| 3                         | Batch Number | N    | 4    | 9-12   | Batch number assigned               |
| 4                         | Record Count | N    | 9    | 13-21  | Number of receipts                  |
| 5                         | Filler       | A    | 9    | 22-120 | Reserved for EWR Inc., use          |

### Table 89

| SECTION 5 FILE TYPE HE (ERROR ACKNOWLEDGEMENT FILES)                                                             |                                                                                                             |                                                                                     |     |
|:-----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:----|
| T                                                                                                                | his section contains information regarding batch processing and rejections, i.e., what causes a batch to    |                                                                                     |     |
| reject, and what type of acknowledgments the user will receive.                                                  |                                                                                                             |                                                                                     |     |
| E                                                                                                                | rrors: How Processing is affected and expected acknowledgments                                              |                                                                                     |     |
| E                                                                                                                | rrors are caused by any number of mistakes including invalid entries, or lack of required information.      |                                                                                     |     |
| The EWR host does not verify information, it only checks to ensure that the entries are within the               |                                                                                                             |                                                                                     |     |
| parameters of the field specifications.                                                                          |                                                                                                             |                                                                                     |     |
| W                                                                                                                | hen batches which contain errors are transmitted to the host, errors will be identified and                 |                                                                                     |     |
| acknowledged to the user.  The acknowledgments generated vary by batch.                                          |                                                                                                             |                                                                                     |     |
| T                                                                                                                | he following batches do not process any of the data if one error is detected by the host.  The host         |                                                                                     |     |
| REJECTS the entire batch and no receipts are updated.                                                            |                                                                                                             |                                                                                     |     |
|                                                                                                                  |                                                                                                             | BATCH TYPES: 05, 06, 19, 20, 21, 24, 30, 31, 34, 37, 38, 51, 55, 65, 70, 71, and 72 |     |
| A                                                                                                                | ll other batch types will continue processing if errors are detected by the host.  However, there is an     |                                                                                     |     |
| exception: If the first 11 records in the batch are in error, the host will REJECT the entire batch. For         |                                                                                                             |                                                                                     |     |
| example, if there are 20 records in a batch and records 1,3,5,7,9,11,13,15,17, and 19 have errors, the           |                                                                                                             |                                                                                     |     |
| host will process 10 records and reject 10.                                                                      |                                                                                                             |                                                                                     |     |
| O                                                                                                                | n the other hand, if the first consecutive 11 (1-11) receipts are in error, the host will reject the entire |                                                                                     |     |
| batch. The reason for the entire batch rejecting is that if the first 11 bales are in error, it is very possible |                                                                                                             |                                                                                     |     |
| that the batch contains many additional errors, therefore the host rejects the batch instead of                  |                                                                                                             |                                                                                     |     |
| downloading an error message for all receipts in the batch.                                                      |                                                                                                             |                                                                                     |     |
| W                                                                                                                | hen the host generates and HE file it consists of the following 4 lines (minimum):                          |                                                                                     |     |
|                                                                                                                  | •                                                                                                           | Batch Header (H) – Same layout has HA85                                             |     |
|                                                                                                                  | •                                                                                                           | Acknowledgments (AC) – Same Layout as HA85                                          |     |
|                                                                                                                  | •                                                                                                           | Error(s) line; There are 3 types ET , EB or ED, see the layout below for specifics  |     |
|                                                                                                                  | •                                                                                                           | Batch Trailer (T) – Same Layout as HA85                                             |     |
|                                                                                                                  |                                                                                                             |                                                                                     | 5-1 |

### Table 90

| T                                            | o determine what processed and what failed, the following steps should be taken:   |              |    |    |         |                                               |
|:---------------------------------------------|:-----------------------------------------------------------------------------------|:-------------|:---|:---|:--------|:----------------------------------------------|
| Examine the following fields of the AC line: |                                                                                    |              |    |    |         |                                               |
|                                              | 14                                                                                 | Total Detail | N  | 8  | 99-106  | Total detail records in batch sent to host    |
|                                              |                                                                                    | Records Sent |    |    |         |                                               |
|                                              | 15                                                                                 | Total Detail | N  | 8  | 107-114 | Total detail records that processed in the    |
|                                              |                                                                                    | Processed    |    |    |         | batch                                         |
|                                              | 16                                                                                 | Action Flag  | A  | 1  | 115     | E                                             |
|                                              | 17                                                                                 | Bale Count   | A  | 5  | 116-120 | Number of bales/receipts (not records) in the |
|                                              |                                                                                    |              |    |    |         | batch.                                        |

### Table 91

| There should be a single EB line, if the batch is not formatted correctly.   |                                    |                        |      |      |        |                                           |
|:-----------------------------------------------------------------------------|:-----------------------------------|:-----------------------|:-----|:-----|:-------|:------------------------------------------|
| There may be multiple ED lines for each receipt in error.                    |                                    |                        |      |      |        |                                           |
| E                                                                            | T DETAIL   [Error in Transmission] |                        |      |      |        |                                           |
|                                                                              | Field                              | Field Name             | Type | Size | Pos    | Description                               |
|                                                                              | 1                                  | Record Type            | A    | 2    | 1-2    | ET=Error in Transmission file,  Header or |
|                                                                              |                                    |                        |      |      |        | Trailer                                   |
|                                                                              | 2                                  | Originating            | N    | 6    | 3-8    | Transmission Number (sent form PC to the  |
|                                                                              |                                    | Transmission Number    |      |      |        | Host)                                     |
|                                                                              | 3                                  | Date Error Occurred    | N    | 8    | 9-16   | Date Error Occurred                       |
|                                                                              | 4                                  | Time Error Occurred    | N    | 6    | 17-22  | Time Error Occurred                       |
|                                                                              | 5                                  | Error Code             | N    | 3    | 23-25  | Application Assigned Code, Created by the |
|                                                                              |                                    |                        |      |      |        | Host                                      |
|                                                                              | *6                                 | Error Data             | AN   | 8    | 26-33  | Specific Field in Error                   |
|                                                                              | 7                                  | Additional Information | A    | 32   | 34-65  | Can be used to provide additional         |
|                                                                              |                                    |                        |      |      |        | information about the error               |
|                                                                              | 8                                  | Filler                 | A    | 55   | 66-120 | Reserved for EWR, Inc. use                |

### Table 92

| EB and ED DETAIL [EB = Error in Batch] [ED = Error in Detail]   |                     |      |      |       |                                              |
|:----------------------------------------------------------------|:--------------------|:-----|:-----|:------|:---------------------------------------------|
| Field                                                           | Field Name          | Type | Size | Pos   | Description                                  |
| 1                                                               | Record Type         | A    | 2    | 1-2   | EB=Error in Batch Header or Batch Trailer    |
|                                                                 |                     |      |      |       | ED=Error in Batch Detail                     |
| 2                                                               | Originating         | N    | 6    | 3-8   | Transmission Number (sent from PC to Host)   |
|                                                                 | Transmission        |      |      |       |                                              |
|                                                                 | Number              |      |      |       |                                              |
| 3                                                               | Date Error          | N    | 8    | 9-16  | Date Error Occurred at Host                  |
|                                                                 | Occurred            |      |      |       |                                              |
| 4                                                               | Time Error          | N    | 6    | 17-22 | Time Error Occurred at Host                  |
|                                                                 | Occurred            |      |      |       |                                              |
| 5                                                               | Error Code          | N    | 3    | 23-25 | Application Assigned Code determined by the  |
|                                                                 |                     |      |      |       | host                                         |
| 6                                                               | Original Batch      | N    | 2    | 26-27 | Batch Type (sent from PC to host)            |
|                                                                 | Type                |      |      |       |                                              |
| 7                                                               | Original Batch      | N    | 4    | 28-31 | Batch number sent from PC to host            |
|                                                                 | Number              |      |      |       |                                              |
| 8                                                               | Originating Holder  | AN   | 7    | 32-38 | Holder who sent batch to host                |
|                                                                 | ID                  |      |      |       |                                              |
| 9                                                               | Originating User ID | AN   | 6    | 39-44 | User ID who sent Batch                       |
| 10                                                              | Error Data          | AN   | 40   | 45-84 | Can be used to provide additional info about |
|                                                                 |                     |      |      |       | error; otherwise blanks (format is dependent |
|                                                                 |                     |      |      |       | on Error Code) – Normally will contain       |
|                                                                 |                     |      |      |       | warehouse code, receipt number and crop      |
|                                                                 |                     |      |      |       | year                                         |
| 11                                                              | Error Message       | AN   | 32   | 85-   | EWR Host error message                       |
|                                                                 |                     |      |      | 116   |                                              |
| 12                                                              | Filler              | A    | 4    | 117-  | Reserved for EWR, Inc. use                   |
|                                                                 |                     |      |      | 120   |                                              |

### Table 93

| (negotiable and non-negotiable) and total number of bales (negotiable and non-negotiable) they hold by   |                       |                  |      |      |        |                                              |
|:---------------------------------------------------------------------------------------------------------|:----------------------|:-----------------|:-----|:-----|:-------|:---------------------------------------------|
| warehouse.                                                                                               |                       |                  |      |      |        |                                              |
| H                                                                                                        | EADER LAYOUT FOR HS78 |                  |      |      |        | Record Size = 100                            |
|                                                                                                          | Field                 | Field Name       | Type | Size | Pos    | Description                                  |
|                                                                                                          | 1                     | Record Type      | A    | 1    | 1      | H=Header Record                              |
|                                                                                                          | 2                     | Holder ID        | AN   | 7    | 2-8    | Holder ID who will receive summaries         |
|                                                                                                          | 3                     | Batch Number     | N    | 4    | 9-12   | Batch Number generated by Host               |
|                                                                                                          | 4                     | Batch Type       | N    | 2    | 13-14  | 78=Block Receipts summary for holder         |
|                                                                                                          | 5                     | Batch Date       | N    | 8    | 15-22  | Date batch was created at host; MMDDYYYY     |
|                                                                                                          | 6                     | Batch Time       | N    | 6    | 23-28  | Time batch was created at host; HHMMSS       |
|                                                                                                          | 7                     | Filler           | A    | 72   | 29-100 | Reserved for EWR, Inc. use                   |
| D                                                                                                        | ETAIL LAYOUT FOR HS78 |                  |      |      |        |                                              |
|                                                                                                          | Field                 | Field Name       | Type | Size | Pos    | Description                                  |
|                                                                                                          | 1                     | Record Type      | A    | 1    | 1      | D = Detail Record                            |
|                                                                                                          | 2                     | Holder ID        | AN   | 7    | 2-8    | Holder ID = Holder of block receipts         |
|                                                                                                          | 3                     | Warehouse Code   | N    | 6    | 9-14   | Warehouse code where block receipts are      |
|                                                                                                          |                       |                  |      |      |        | held                                         |
|                                                                                                          | 4                     | Crop Year        | N    | 4    | 15-18  | Crop Year of receipts held                   |
|                                                                                                          | 5                     | Up to Date       | N    | 8    | 19-26  | Totals calculated as of date; MMDDYYYY       |
|                                                                                                          | 6                     | Up to Date       | N    | 6    | 27-32  | Totals calculated as of time; HHMMSS         |
|                                                                                                          | 7                     | Current Holder   | N    | 8    | 33-40  | Current Holder count of negotiable block     |
|                                                                                                          |                       | Negotiable Count |      |      |        | receipts                                     |
|                                                                                                          | 8                     | Current Holder   | N    | 8    | 41-48  | Current Holder count of negotiable bales     |
|                                                                                                          |                       | Negotiable Bale  |      |      |        |                                              |
|                                                                                                          |                       | Count            |      |      |        |                                              |
|                                                                                                          | 9                     | Subholder        | N    | 8    | 49-56  | Subholder count of negotiable block receipts |
|                                                                                                          |                       | Negotiable Count |      |      |        |                                              |
|                                                                                                          | 10                    | Subholder        | N    | 8    | 57-64  | Subholder count of negotiable bales          |
|                                                                                                          |                       | Negotiable Bale  |      |      |        |                                              |
|                                                                                                          |                       | Count            |      |      |        |                                              |
|                                                                                                          | 11                    | Current Holder   | N    | 8    | 65-72  | Current count of non-negotiable receipts     |
|                                                                                                          |                       | Non-Negotiable   |      |      |        |                                              |
|                                                                                                          |                       | Count            |      |      |        |                                              |

### Table 94

|    | 12                     | Current Holder   | N    | 8    | 73-80   | Current count of non-negotiable bales           |
|:---|:-----------------------|:-----------------|:-----|:-----|:--------|:------------------------------------------------|
|    |                        | Non-Negotiable   |      |      |         |                                                 |
|    |                        | Bale Count       |      |      |         |                                                 |
|    | 13                     | Subholder Non-   | N    | 8    | 81-88   | Subholder count of non-negotiable receipts      |
|    |                        | Negotiable Count |      |      |         |                                                 |
|    | 14                     | Subholder Non-   | N    | 8    | 89-96   | Subholder count of non-negotiable bales         |
|    |                        | Negotiable Bale  |      |      |         |                                                 |
|    |                        | Count            |      |      |         |                                                 |
|    | 15                     | Filler           | A    | 4    | 97-100  | Reserved for EWR, Inc. use                      |
| T  | RAILER LAYOUT FOR HS78 |                  |      |      |         |                                                 |
|    | Field                  | Field Name       | Type | Size | Pos     | Description                                     |
|    | 1                      | Record Type      | A    | 1    | 1       | T = Trailer Record                              |
|    | 2                      | Holder ID        | AN   | 7    | 2-8     | The same as entered in the header record        |
|    | 3                      | Batch Number     | N    | 4    | 9-12    | The same as entered in the header record        |
|    | 4                      | Record Count     | N    | 9    | 13-21   | Control total record count of detail records in |
|    |                        |                  |      |      |         | the batch                                       |
|    | 5                      | Filler           | A    | 79   | 22-     | Reserved for EWR, Inc. use                      |
|    |                        |                  |      |      | 100     |                                                 |

### Table 95

| HS82 - Receipts Held Summary                                                                             |
|:---------------------------------------------------------------------------------------------------------|
| H                                                                                                        |
| S82 is a summary of receipts held or subheld; which is generated each night and delivered to the         |
| holder’s mailbox.  The information contained in the summary is calculated through the previous day’s     |
| activity.                                                                                                |
| R                                                                                                        |
| eceived by all Users who have requested that their holder profile be flagged so that this information is |
| given to them on a daily basis                                                                           |
| N                                                                                                        |
| OTE: Receipts on this page refer to regular receipts (negotiable and non-negotiable)                     |
| Block receipts are NOT included in these totals.                                                         |

### Table 96

| R                                        | eceipts transferred to the warehouse in a shipping order will be included in a warehouse holder   |              |      |      |        |                                          |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------|:-------------|:-----|:-----|:-------|:-----------------------------------------|
| summary until the receipts are canceled. |                                                                                                   |              |      |      |        |                                          |
| H                                        | EADER LAYOUT FOR HS82                                                                             |              |      |      |        | Record Size = 100                        |
|                                          | Field                                                                                             | Field Name   | Type | Size | Pos    | Description                              |
|                                          | 1                                                                                                 | Record Type  | A    | 1    | 1      | H=Header Record                          |
|                                          | 2                                                                                                 | Holder ID    | AN   | 7    | 2-8    | Holder ID who will receive summaries     |
|                                          | 3                                                                                                 | Batch Number | N    | 4    | 9-12   | Batch Number generated by Host           |
|                                          | 4                                                                                                 | Batch Type   | N    | 2    | 13-14  | 82=Receipts held summary for             |
|                                          |                                                                                                   |              |      |      |        | holder/subholder                         |
|                                          | 5                                                                                                 | Batch Date   | N    | 8    | 15-22  | Date batch was created at host; MMDDYYYY |
|                                          | 6                                                                                                 | Batch Time   | N    | 6    | 23-28  | Time batch was created at host; HHMMSS   |
|                                          | 7                                                                                                 | Filler       | A    | 72   | 29-100 | Reserved for EWR, Inc. use               |

### Table 97

|    | DETAIL LAYOUT FOR HS82   |                   |      |      |        |                                                 |
|:---|:-------------------------|:------------------|:-----|:-----|:-------|:------------------------------------------------|
|    | Field                    | Field Name        | Type | Size | Pos    | Description                                     |
|    | 1                        | Record Type       | A    | 1    | 1      | D=Detail Record                                 |
|    | 2                        | Holder ID         | AN   | 7    | 2-8    | Holder ID of receipts held                      |
|    | 3                        | Warehouse Code    | N    | 6    | 9-14   | Warehouse Code that identifies the storage      |
|    |                          |                   |      |      |        | location                                        |
|    | 4                        | Crop Year         | N    | 4    | 15-18  | Crop Year of receipts held                      |
|    | 5                        | Up to Date        | N    | 8    | 19-26  | Totals calculated as of date (MMDDYYYY)         |
|    | 6                        | Up to Time        | N    | 6    | 27-32  | Totals calculated as of time (HHMMSS)           |
|    | 7                        | Current Holder    | N    | 8    | 33-40  | Total number of receipts held as of 12:00       |
|    |                          | Balance           |      |      |        | midnight of the previous day (this total does   |
|    |                          |                   |      |      |        | not include canceled receipts)                  |
|    | 8                        | Subholder Balance | N    | 8    | 41-48  | Total number of receipts held as subholder -    |
|    |                          | (no CCC or Whse)  |      |      |        | This total excludes receipts held by            |
|    |                          |                   |      |      |        | warehouses and CCC                              |
|    | 9                        | Subholder Balance | N    | 8    | 49-56  | Total number of receipts in Price Support Loan  |
|    |                          | (CCC is Holder)   |      |      |        | Program (CCC is Holder) and recipient of        |
|    |                          |                   |      |      |        | acknowledgment/summary is the Subholder         |
|    | 10                       | Electronic        | N    | 8    | 57-64  | Total number of uncanceled Electronic           |
|    |                          | Receipts held     |      |      |        | Receipts held (Received by warehouses only)     |
|    |                          | (Whse Only)       |      |      |        |                                                 |
|    | 11                       | Paper Receipts    | N    | 8    | 65-72  | Total number of uncanceled Paper Receipts       |
|    |                          | Held (Whse Only)  |      |      |        | held (Received by warehouses only)              |
|    | 12                       | Reserved          | A    | 8    | 73-80  | Blank                                           |
|    | 13                       | Under Shipping    | N    | 8    | 81-88  | Total number of receipts under a shipping       |
|    |                          | Order             |      |      |        | order                                           |
|    | 14                       | Pending Bank      | N    | 8    | 89-96  | Total number of receipts pending a bank         |
|    |                          |                   |      |      |        | release                                         |
|    | 15                       | Filler            | A    | 4    | 97-100 | Reserved for EWR, Inc. use                      |
| T  | RAILER LAYOUT FOR HS82   |                   |      |      |        |                                                 |
|    | Field                    | Field Name        | Type | Size | Pos    | Description                                     |
|    | 1                        | Record Type       | A    | 1    | 1      | T=Trailer Record                                |
|    | 2                        | Holder ID         | AN   | 7    | 2-8    | The same as entered in the header record        |
|    | 3                        | Batch Number      | N    | 4    | 9-12   | The same as entered in the header record        |
|    | 4                        | Record Count      | N    | 9    | 13-21  | Control total record count of detail records in |
|    |                          |                   |      |      |        | the batch                                       |
|    | 5                        | Filler            | A    | 79   | 22-100 | Reserved for EWR, Inc. use                      |

### Table 98

| HS83 - Summary of Receipts Issued  (Received by Warehouse Users Only)                                       |
|:------------------------------------------------------------------------------------------------------------|
| H                                                                                                           |
| S83 is a summary which is generated each night and delivered to the Warehouse’s holder mailbox.             |
| The information contained in the summary is calculated through the previous day’s activity.  It contains    |
| the total number of receipts issued during the period August 1 through July 31.  The total will include all |
| receipts issued during that period regardless of the crop year assigned.   We believe that these dates will |
| give the entire Cotton Belt the most accurate totals for a harvest season.                                  |
| W                                                                                                           |
| arehouses are encouraged to retain the July 31 report (Delivered on August 1), as it will be the last       |
| report for the period August 1 - July 31.                                                                   |

### Table 99

| W                                         | arehouses are encouraged to retain the July 31 report (Delivered on August 1), as it will be the last   |                 |      |      |        |                                              |
|:------------------------------------------|:--------------------------------------------------------------------------------------------------------|:----------------|:-----|:-----|:-------|:---------------------------------------------|
| report for the period August 1 - July 31. |                                                                                                         |                 |      |      |        |                                              |
| H                                         | EADER LAYOUT FOR HS83                                                                                   |                 |      |      |        | Record Size = 100                            |
|                                           | Field                                                                                                   | Field Name      | Type | Size | Pos    | Description                                  |
|                                           | 1                                                                                                       | Record Type     | A    | 1    | 1      | H=Header Record                              |
|                                           | 2                                                                                                       | Holder ID       | AN   | 7    | 2-8    | Holder ID who will receive summaries         |
|                                           | 3                                                                                                       | Batch Number    | N    | 4    | 9-12   | Batch Number generated by Host               |
|                                           | 4                                                                                                       | Batch Type      | N    | 2    | 13-14  | 83=Receipts held summary for holder          |
|                                           | 5                                                                                                       | Batch Date      | N    | 8    | 15-22  | Date batch was created at host; MMDDYYYY     |
|                                           | 6                                                                                                       | Batch Time      | N    | 6    | 23-28  | Time batch was created at host; HHMMSS       |
|                                           | 7                                                                                                       | Filler          | A    | 72   | 29-100 | Reserved for EWR, Inc. use                   |
| D                                         | ETAIL LAYOUT FOR HS83                                                                                   |                 |      |      |        |                                              |
|                                           | Field                                                                                                   | Field Name      | Type | Size | Pos    | Description                                  |
|                                           | 1                                                                                                       | Record Type     | A    | 1    | 1      | D=Detail Record                              |
|                                           | 2                                                                                                       | Holder ID       | AN   | 7    | 2-8    | Holder ID of receipts issued                 |
|                                           | 3                                                                                                       | Warehouse Code  | N    | 6    | 9-14   | Warehouse Code of receipts issued            |
|                                           | 4                                                                                                       | Filler          | AN   | 4    | 15-18  | Reserved for EWR, Inc. use                   |
|                                           | 5                                                                                                       | Up to Date      | N    | 8    | 19-26  | Totals calculated as of date; MMDDYYYY       |
|                                           | 6                                                                                                       | Up to Time      | N    | 6    | 27-32  | Totals calculated as of time; HHMMSS         |
|                                           | 7                                                                                                       | *Issued-Regular | N    | 8    | 33-40  | Total number of electronic regular and       |
|                                           |                                                                                                         | & Certificated  |      |      |        | certificated warehouse receipts issued as of |
|                                           |                                                                                                         |                 |      |      |        | midnight (includes active and canceled       |
|                                           |                                                                                                         |                 |      |      |        | receipts)                                    |
|                                           | 8                                                                                                       | *Issued-Block   | N    | 8    | 41-48  | Number of electronic block receipts issued   |
|                                           | 9                                                                                                       | *Issued-Cancel  | N    | 8    | 49-56  | Number of receipts canceled                  |
|                                           | 10                                                                                                      | *Issued-Block   | N    | 8    | 57-64  | Number of electronic block receipts canceled |
|                                           |                                                                                                         | Cancel          |      |      |        |                                              |
|                                           | 11                                                                                                      | *Issued-        | N    | 8    | 65-72  | Number of certificated receipts issued.      |
|                                           |                                                                                                         | Certificated    |      |      |        |                                              |
|                                           | 12                                                                                                      | *Cancel-        | N    | 8    | 73-80  | Number of certificated receipts cancelled.   |
|                                           |                                                                                                         | Certificated    |      |      |        |                                              |
|                                           | 13                                                                                                      | Filler          | A    | 20   | 81-100 | Reserved for EWR, Inc. use                   |

### Table 100

| TRAILER LAYOUT FOR HS83   |              |      |      |        |                                                 |
|:--------------------------|:-------------|:-----|:-----|:-------|:------------------------------------------------|
| Field                     | Field Name   | Type | Size | Pos    | Description                                     |
| 1                         | Record Type  | A    | 1    | 1      | T=Trailer Record                                |
| 2                         | Holder ID    | AN   | 7    | 2-8    | The same as entered in the header record        |
| 3                         | Batch        | N    | 4    | 9-12   | The same as entered in the header record        |
|                           | Number       |      |      |        |                                                 |
| 4                         | Record Count | N    | 9    | 13-21  | Control total record count of detail records in |
|                           |              |      |      |        | the batch                                       |
| 5                         | Filler       | A    | 79   | 22-100 | Reserved for EWR, Inc. use                      |

### Table 101

| warehouse.  The batch is generated each night and placed in the banks Holder ID mailbox.  The collateral   |                       |                    |      |      |       |                                                |
|:-----------------------------------------------------------------------------------------------------------|:----------------------|:-------------------|:-----|:-----|:------|:-----------------------------------------------|
| summaries are provided only once each day and are calculated through the previous day’s totals.            |                       |                    |      |      |       |                                                |
| H                                                                                                          | EADER LAYOUT FOR HS89 |                    |      |      |       | Record Size = 90                               |
|                                                                                                            | Field                 | Field Name         | Type | Size | Pos   | Description                                    |
|                                                                                                            | 1                     | Record Type        | A    | 1    | 1     | H = Header Record                              |
|                                                                                                            | 2                     | Holder ID          | AN   | 7    | 2-8   | Holder ID who will receive summaries           |
|                                                                                                            | 3                     | Batch Number       | N    | 4    | 9-12  | Batch Number generated by Host                 |
|                                                                                                            | 4                     | Batch Type         | N    | 2    | 13-14 | 82 = Receipts held summary for                 |
|                                                                                                            |                       |                    |      |      |       | holder/subholder                               |
|                                                                                                            | 5                     | Batch Date         | N    | 8    | 15-22 | Date batch was created at host; MMDDYYYY       |
|                                                                                                            | 6                     | Batch Time         | N    | 6    | 23-28 | Time batch was created at host; HHMMSS         |
|                                                                                                            | 7                     | Filler             | A    | 62   | 29-90 | Reserved for EWR, Inc. use                     |
| D                                                                                                          | ETAIL LAYOUT FOR HS89 |                    |      |      |       |                                                |
|                                                                                                            | Field                 | Field Name         | Type | Size | Pos   | Description s                                  |
|                                                                                                            | 1                     | Record Type        | A    | 1    | 1     | D = Detail Record                              |
|                                                                                                            | 2                     | SubHolder ID       | AN   | 7    | 2-8   | Sub Holder ID of the receipts (Bank is holder) |
|                                                                                                            | 3                     | Merchant Name      | AN   | 25   | 9-33  | Name of merchant who is the subholder          |
|                                                                                                            | 4                     | Warehouse Code     | N    | 6    | 34-39 | Warehouse Code of receipts held as             |
|                                                                                                            |                       |                    |      |      |       | collateral                                     |
|                                                                                                            | 5                     | Non-Block Balance  | N    | 6    | 40-45 | Current count of receipts in the warehouse     |
|                                                                                                            | 6                     | Block Balance      | N    | 6    | 46-51 | Current count of block receipts in the         |
|                                                                                                            |                       |                    |      |      |       | warehouse                                      |
|                                                                                                            | 7                     | Block Bale Balance | N    | 6    | 52-57 | Current total of block bales in the            |
|                                                                                                            |                       |                    |      |      |       | warehouse                                      |
|                                                                                                            | 8                     | Pending Non Block  | N    | 6    | 58-63 | Current total of pending releases of non-      |
|                                                                                                            |                       |                    |      |      |       | block receipts                                 |
|                                                                                                            | 9                     | Pending Block      | N    | 6    | 64-69 | Current total of pending releases of block     |
|                                                                                                            |                       |                    |      |      |       | receipts                                       |
|                                                                                                            | 10                    | Pending Block      | N    | 6    | 70-75 | Current total of pending releases of block     |
|                                                                                                            |                       | Bales              |      |      |       | bales                                          |
|                                                                                                            | 11                    | Filler             | A    | 15   | 76-90 | Reserved for EWR, Inc. use                     |

### Table 102

|       | TRAILER LAYOUT FOR HS89   |      |      |       |                                               |
|:------|:--------------------------|:-----|:-----|:------|:----------------------------------------------|
| Field | Field Name                | Type | Size | Pos   | Description                                   |
| 1     | Record Type               | A    | 1    | 1     | T=Trailer Record                              |
| 2     | Holder ID                 | AN   | 7    | 2-8   | The same as entered in the header record      |
| 3     | Batch Number              | N    | 4    | 9-12  | The same as entered in the header record      |
| 4     | Record Count              | N    | 9    | 13-21 | Control total record of detail records in the |
|       |                           |      |      |       | batch                                         |
| 5     | Filler                    | A    | 69   | 22-90 | Reserved for EWR, Inc. use                    |
