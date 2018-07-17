# Insurtech
postlinkls = []
for l in range(1, 28):
	link = "https://www.postonline.co.uk/topics/insurtech?page=%s" %l
	postlinkls.append(link)
whole_art_num = 0
for page_num in range(0, len(postlinkls)+1):
    if page_num == 0:
        pass
    else:
        browser.get(postlinkls[page_num-1])
        #print('next',page_num+2)
        time.sleep(2)

    articlels = browser.find_elements_by_tag_name('h5')    
    article_num = len(articlels)
    
    for k in range(1, article_num+1):
        whole_art_num += 1
        #if page_num == 5 and k == 3:
        #    article = browser.find_element_by_xpath('//*[@id="news-articles"]/div[3]/div/div[1]/h3/a')
        #else:
        article = browser.find_element_by_xpath('//*[@id="listings"]/article[%s]/div[2]/h5/a'%k)        
        article.click()

#################################################
reinsuls = []
reinsurancelink = "https://www.reinsurancene.ws/tag/insurtech/"
for j in range(2, 21):
	link = "https://www.reinsurancene.ws/tag/insurtech/page/%s/" %j
	reinsuls.append(link)


whole_art_num = 0
for page_num in range(0, len(reinsuls)+1):
    if page_num == 0:
        pass
    else:
        browser.get(reinsuls[page_num-1])
        time.sleep(2)

    articlels = browser.find_elements_by_tag_name('h3')    
    article_num = len(articlels)
    
    for k in range(1, article_num+1):
        whole_art_num += 1
        #if page_num == 5 and k == 3:
        #    article = browser.find_element_by_xpath('//*[@id="news-articles"]/div[3]/div/div[1]/h3/a')
        #else:
        article = browser.find_element_by_xpath('//*[@id="articles-section"]/div[%s]/div[2]/h3/a'%k)        
        article.click()
        filename = "reinsu_article_"+str(whole_art_num)+'.txt'
        with open(filename, 'w', encoding='UTF-8') as txt_file:
            try:
                header = browser.find_element_by_tag_name('h1').text
                #author = browser.find_element_by_class_name('author').text
                #pub_date = browser.find_element_by_tag_name('time').text 
                pub_date = browser.find_element_by_xpath("//p[@class ='date']").text
                browser.find_element_by_xpath("//article[@class ='date']").text
                textbody = browser.find_element_by_tag_name('article').text
                print(whole_art_num, header, pub_date)

                txt_file.write("%s\n" % header)
                txt_file.write("\n")
                #txt_file.write("%s\n" % author)
                #txt_file.write("\n") 
                txt_file.write("%s\n" % pub_date)
                txt_file.write("\n") 
                txt_file.write("%s\n" % textbody)
                txt_file.write("\n\n")
                time.sleep(1)
            except Exception as e:
                print(page_num, article_num)
                print(whole_art_num)
                print(e)

            txt_file.close()
        browser.back()
        time.sleep(1)


http://aithority.com/tag/news/
http://aithority.com/tag/news/page/2/








