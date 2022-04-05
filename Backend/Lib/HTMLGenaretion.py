
style = """
<style>
body {
	margin:5px 0px 5px 5px;
	background-color: #EEEEEE;
}
.footer_text {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 10px;
	color: #666666;
	line-height: 15px;
}
.bar_bk {

	background-image: url(http://www.educationboardresults.gov.bd/images/bar_bk.jpg);
	background-repeat: repeat-x;
}
#site_title {
font-family:Verdana, Arial, Helvetica, sans-serif;
color:#FFFFEE; 
margin:3px 0px 0px 5px;
font-size:20px;
background-color: #007814;

}
#site_title_des {
font-family: Verdana, Arial, Helvetica, sans-serif; 
font-size:17px; 
color:#95e17d; 
margin:0px; 
margin-left:6px; 
display:block; 
margin:0px 0px 5px 5px;
background-color: #007814;
}
.left_round {
	background-image: url(../images/left_round.gif);
	background-repeat: no-repeat;
	background-position: left top;
}
.black11 {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 11px;
	color: #000000;
	text-decoration: none;
	font-weight: normal;
}
.red11 {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 11px;
	color: #F00;
	text-decoration: none;
	font-weight: normal;
}
.red12bold {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 11px;
	color: #F00;
	text-decoration: none;
	font-weight: bold;
}


.black12bold {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 12px;
	color: #000000;
	text-decoration: none;
	font-weight: bold;
}
.black12 {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 12px;
	color: #000000;
	text-decoration: none;
	font-weight: normal;
}

.black14bold {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 14px;
	color: #000000;
	text-decoration: none;
	font-weight: bold;
	clip: rect(auto,auto,auto,auto);
}
.black14 {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 14px;
	color: #000000;
	text-decoration: none;
	font-weight: normal;
	clip: rect(auto,auto,auto,auto);
}


.black16bold {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 16px;
	color: #000000;
	text-decoration: none;
	font-weight: bold;
}

.links {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 11px;
	color: #00F;
	text-decoration: none;
	font-weight: bold;
}
.links02 {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 11px;
	color: #FFF;
	text-decoration: none;
	font-weight: normal;
}

.links:hover {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 11px;
	color: #F00;
	text-decoration: none;
	font-weight: bold;
}
.links02:hover {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 11px;
	color: #0C9;
	text-decoration: none;
	font-weight: normal;
}
.vfield {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 22px;
	color: #000;
	text-decoration: none;
	background-color: #F4F0F2;
	border: 1px solid #999;
	font-weight: bold;
	width: 200px;
	padding-top: 4px;
	padding-right: 4px;
	padding-left: 4px;
	padding-bottom: 4px;
	border-radius: 4px;
}

.textfield01 {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 22px;
	color: #ACD0A1;
	text-decoration: none;
	background-color: #E4EDE4;
	border: 1px solid #C3C5C5;
	font-weight: bold;
	width: 180px;
	padding-top: 4px;
	padding-right: 4px;
	padding-left: 4px;
	padding-bottom: 4px;
	border-radius: 4px;
}

.textfield05 {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 12px;
	color: #000000;
	text-decoration: none;
	background-color: #F4F0F2;
	border: 1px solid #999;
	font-weight: normal;
	width: 205px;
	padding-top: 4px;
	padding-right: 4px;
	padding-left: 4px;
	padding-bottom: 4px;
	border-radius: 4px;
}
.textfield06 {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: 12px;
	color: #000000;
	text-decoration: none;
	background-color: #F4F0F2;
	border: 1px solid #999;
	font-weight: normal;
	width: 200px;
	padding-top: 4px;
	padding-right: 4px;
	padding-left: 4px;
	padding-bottom: 4px;
	border-radius: 4px;
}
</style>
"""


def GenarateHtml(dataObj):
    tmp = ""
    for row in dataObj['subject_grades']:
        tmp += f"""
        <tr>
               <td align="left" bgcolor="#DEE1E4" valign="middle">
                {row['subjectCode']}
               </td>
               <td align="left" bgcolor="#DEE1E4" valign="middle">
                {row['subjectName']}
               </td>
               <td align="left" bgcolor="#DEE1E4" valign="middle">
                {row['subjectGPA']}
               </td>
              </tr>
        """

    return f"""
<body>
{style}
 <table align="center" border="0" cellpadding="0" cellspacing="0" width="650">
  <tr>
   <td>
    <table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" width="650">
     <tr>
      <td align="left" background="http://www.educationboardresults.gov.bd/images/back_cor_left_top.gif" valign="top" width="12">
       <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
      </td>
      <td background="http://www.educationboardresults.gov.bd/images/back_top.gif" valign="top">
       <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
      </td>
      <td align="right" background="http://www.educationboardresults.gov.bd/images/back_cor_right_top.gif" valign="top" width="12">
       <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
      </td>
     </tr>
     <tr>
      <td align="left" background="http://www.educationboardresults.gov.bd/images/back_left.gif" valign="top">
      </td>
      <td valign="top">
       <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
         <td align="center" bgcolor="#EEEEEE" class="left_round" height="121" valign="middle" width="142">
          <img height="82" src="http://www.educationboardresults.gov.bd/images/bd_logo.png" width="82"/>
         </td>
         <td width="2">
          <img height="1" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="2"/>
         </td>
         <td bgcolor="#007814" valign="top">
          <table border="0" cellpadding="0" cellspacing="0" width="100%">
           <tr>
            <td style="background-color: #007814;" align="right">
             <table border="0" cellpadding="0" cellspacing="0" width="100%">
              <tr>
               <td style="background-color: #007814;" align="left" valign="bottom">
                <h1 id="site_title_des">
                 Ministry of Education
                </h1>
               </td>
               <td align="right" valign="top">
                <img border="0" height="41" hspace="0" src="http://www.educationboardresults.gov.bd/images/banner_flag.jpg" vspace="0" width="220"/>
               </td>
              </tr>
             </table>
            </td>
           </tr>
           <tr >
            <td align="left" bgcolor="#007814">
             <img height="1" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="1"/>
            </td>
           </tr>
           <tr style="background-color: #007814;">
            <td style="background-color: #007814;" align="left" height="55">
             <h1 style="background-color: #007814;" id="site_title">
              Intermediate and Secondary Education Boards Bangladesh
             </h1>
            </td>
           </tr>
           <tr>
            <td  align="right" bgcolor="#86C775" class="bar_bk" height="23">
             <a class="links02" href="http://www.educationboard.gov.bd">
              Official Website of Education Board
             </a>
            </td>
           </tr>
          </table>
         </td>
        </tr>
       </table>
       <img height="1" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="1"/>
      </td>
      <td align="right" background="http://www.educationboardresults.gov.bd/images/back_right.gif" valign="top">
      </td>
     </tr>
    </table>
   </td>
  </tr>
  <tr>
   <td>
    <table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" width="650">
     <tr>
      <td align="left" background="http://www.educationboardresults.gov.bd/images/back_left.gif" valign="top" width="12">
      </td>
      <td valign="top">
       <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
         <td align="center" class="black16bold" height="50" valign="middle">
          {dataObj['exam']} Result {dataObj['year']}
         </td>
        </tr>
        <tr>
         <td align="center" valign="middle">
          <table border="0" cellpadding="0" cellspacing="0" width="100%">
           <tr>
            <td align="center" valign="middle">
             <table border="0" cellpadding="3" cellspacing="1" class="black12" width="100%">
              <tr>
               <td align="left" bgcolor="#EEEEEE" valign="middle" width="12%">
                Roll No
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle" width="27%">
                {dataObj['roll']}
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle" width="22%">
                Name
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle" width="39%">
                {dataObj['name']}
               </td>
              </tr>
              <tr>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                Board
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                {dataObj['board']}
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                Father's Name
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                {dataObj['father_name']}
               </td>
              </tr>
              <tr>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                Group
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                {dataObj['group']}
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                Mother's Name
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                {dataObj['mother_name']}
               </td>
              </tr>
              <tr>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                Type
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                {dataObj['type']}
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                Date of Birth
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                {dataObj['dob']}
               </td>
              </tr>
              <tr>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                Result
               </td>
               <td align="left" bgcolor="#EEEEEE" class="black12bold" valign="middle">
                {dataObj['result']}
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                Institute
               </td>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                {dataObj['institute']}
               </td>
              </tr>
              <tr>
               <td align="left" bgcolor="#EEEEEE" valign="middle">
                GPA
               </td>
               <td align="left" bgcolor="#EEEEEE" class="black12bold" colspan="3" valign="middle">
                {dataObj['gpa']}
               </td>
              </tr>
             </table>
            </td>
           </tr>
           <tr>
            <td align="center" height="40" valign="middle">
             <span class="black16bold">
              Grade Sheet
             </span>
            </td>
           </tr>
           <tr>
            <td align="center" valign="middle">
             <table border="0" cellpadding="3" cellspacing="1" class="black12" width="100%">
              <tr class="black12bold">
               <td align="left" bgcolor="#AFB7BE" valign="middle" width="19%">
                Code
               </td>
               <td align="left" bgcolor="#AFB7BE" valign="middle" width="66%">
                Subject
               </td>
               <td align="left" bgcolor="#AFB7BE" valign="middle" width="15%">
                Grade
               </td>
              </tr>
              
              {tmp}
             </table>
            </td>
           </tr>
          </table>
         </td>
        </tr>
        <tr>
         <td>
          <table border="0" cellpadding="0" cellspacing="0" width="626">
           <tr bgcolor="#86c775">
            <td colspan="5">
             <img height="5" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="1"/>
            </td>
           </tr>
           <tr>
            <td colspan="5">
             <img height="1" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="1"/>
            </td>
           </tr>
           <tr>
            <td align="left" bgcolor="#F2F2F2" class="footer_text" valign="bottom" width="5">
             <img height="5" src="http://www.educationboardresults.gov.bd/images/footer_corner_left.gif" width="5"/>
            </td>
            <td align="left" bgcolor="#F2F2F2" class="footer_text" height="70" valign="middle" width="356">
             �2005-2020  Ministry of Education, All rights reserved.
            </td>
            <td align="right" bgcolor="#F2F2F2" class="footer_text" height="70" valign="middle" width="150">
             Powered by
             <img height="5" src="http://www.educationboardresults.gov.bd/images/footer_corner_right.gif" width="5"/>
            </td>
            <td align="center" bgcolor="#F2F2F2" height="70" valign="middle" width="110">
             <img height="44" src="http://www.educationboardresults.gov.bd/images/tbl_logo.png" width="83"/>
            </td>
            <td align="left" bgcolor="#F2F2F2" class="footer_text" valign="bottom" width="5">
             <img height="5" src="http://www.educationboardresults.gov.bd/images/footer_corner_right.gif" width="5"/>
            </td>
           </tr>
          </table>
         </td>
        </tr>
       </table>
      </td>
      <td align="right" background="http://www.educationboardresults.gov.bd/images/back_right.gif" valign="top" width="12">
      </td>
     </tr>
     <tr>
      <td align="left" background="http://www.educationboardresults.gov.bd/images/back_cor_left_bot.gif" valign="top">
       <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
      </td>
      <td background="http://www.educationboardresults.gov.bd/images/back_bot.gif" valign="top">
       <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
      </td>
      <td align="right" background="http://www.educationboardresults.gov.bd/images/back_cor_right_bot.gif" valign="top">
       <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
      </td>
     </tr>
    </table>
   </td>
  </tr>
  <tr>
   <td>
   </td>
  </tr>
 </table>
</body>
    """
