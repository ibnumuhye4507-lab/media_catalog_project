<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
        <head>
            <title>ኢስላማዊ ሚዲያ ካታሎግ</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f0f4f0; padding: 40px; }
                .container { max-width: 1000px; margin: auto; background: white; padding: 30px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); }
                h2 { color: #1b5e20; text-align: center; border-bottom: 4px solid #2e7d32; padding-bottom: 15px; }
                
                table { width: 100%; border-collapse: collapse; margin-top: 30px; }
                th { background-color: #2e7d32; color: white; padding: 18px; text-align: left; }
                td { padding: 18px; border-bottom: 1px solid #eee; }
                
                .btn-view { color: white; padding: 10px 20px; text-decoration: none; border-radius: 8px; font-size: 14px; font-weight: bold; display: inline-block; }
                .btn-book { background-color: #3498db; }
                .btn-movie { background-color: #e67e22; }
                
                /* የዝርዝር መረጃ ካርድ ስታይል */
                .detail-section { margin-top: 50px; border-top: 2px solid #2e7d32; padding-top: 20px; }
                .detail-card { background: #f9f9f9; border-left: 8px solid #2e7d32; padding: 20px; margin-bottom: 30px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
                .back-link { font-size: 12px; color: #2e7d32; text-decoration: none; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>የኢስላማዊ ሚዲያ ካታሎግ</h2>
                
                <table>
                    <tr>
                        <th>ዓይነት</th>
                        <th>ርዕስ</th>
                        <th>ደራሲ/ዳይሬክተር</th>
                        <th>ተግባር</th>
                    </tr>
                    <xsl:for-each select="catalog/*">
                    <tr>
                        <td>
                             <xsl:choose>
                                <xsl:when test="name()='book'">መጽሐፍ</xsl:when>
                                <xsl:otherwise>ቪዲዮ</xsl:otherwise>
                            </xsl:choose>
                        </td>
                        <td style="font-weight:bold;"><xsl:value-of select="title"/></td>
                        <td>
                            <xsl:choose>
                                <xsl:when test="name()='book'"><xsl:value-of select="author"/></xsl:when>
                                <xsl:otherwise><xsl:value-of select="director"/></xsl:otherwise>
                            </xsl:choose>
                        </td>
                        <td>
                            <a class="btn-view">
                                <xsl:attribute name="class">
                                    <xsl:choose>
                                        <xsl:when test="name()='book'">btn-view btn-book</xsl:when>
                                        <xsl:otherwise>btn-view btn-movie</xsl:otherwise>
                                    </xsl:choose>
                                </xsl:attribute>
                                <xsl:attribute name="href">#item-<xsl:value-of select="generate-id()"/></xsl:attribute>
                                <xsl:choose>
                                    <xsl:when test="name()='book'">መ/ፍ አንብብ</xsl:when>
                                    <xsl:otherwise>ቪድወእይ</xsl:otherwise>
                                </xsl:choose>
                            </a>
                        </td>
                    </tr>
                    </xsl:for-each>
                </table>

                <div class="detail-section">
                    <h2 style="text-align: left;">ዝርዝር መረጃዎች</h2>
                    <xsl:for-each select="catalog/*">
                        <div class="detail-card">
                            <xsl:attribute name="id">item-<xsl:value-of select="generate-id()"/></xsl:attribute>
                            <h3>ርዕስ፦ <xsl:value-of select="title"/></h3>
                            <p><strong>ዓይነት፦ </strong> <xsl:value-of select="name()"/></p>
                            <p><strong>የወጣበት ዓመት፦ </strong> <xsl:value-of select="year"/> ዓ.ም</p>
                            
                            <xsl:choose>
                                <xsl:when test="name()='book'">
                                    <p><strong>ደራሲ፦ </strong> <xsl:value-of select="author"/></p>
                                    <p><em>ይህ መጽሐፍ በካታሎጋችን ውስጥ በዝርዝር ተመዝግቧል።</em></p>
                                </xsl:when>
                                <xsl:otherwise>
                                    <p><strong>አዘጋጅ (Director)፦ </strong> <xsl:value-of select="director"/></p>
                                    <p><em> ይህ ቪዲዮ በቅርቡ የሚለቀቅ ጠቃሚ ትምህርት ነው።</em></p>
                                </xsl:otherwise>
                            </xsl:choose>
                            <a href="#" class="back-link">ወደ ላይ ተመለስ ↑</a>
                        </div>
                    </xsl:for-each>
                </div>
            </div>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>