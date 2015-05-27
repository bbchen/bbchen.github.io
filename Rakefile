task :default => :server

desc "Build site with WinterSmith"
task :build do
    system "wintersmith build --config deploy.json --clean"
end

desc 'Preview site'
task :server do
    system "wintersmith preview"
end

desc 'Build and deploy'
task :deploy => [:build] do
    sh 'rsync -rtzh --progress --delete ./build/ -e ssh binchen@login.itd.umich.edu:~/Public/html/'
    sh 'rsync -rtzh --progress --delete ./build/ -e ssh binchen@www.earth.lsa.umich.edu:~/Sites/'
end

desc 'Begin a new post'
task :post do   
    ROOT_DIR = File.dirname(__FILE__)

    title = ARGV[1]
    where = ARGV[2 ]

    unless title
        puts %{Usage: rake post "The Post Title"}
        exit(-1)
    end

    datetime = Time.now.strftime('%Y-%m-%d')  # 30 minutes from now.
    slug = title.strip.downcase.gsub(/ /, '-')

    # E.g. 2006-07-16_11-41-batch-open-urls-from-clipboard.markdown
    path = "#{ROOT_DIR}/#{where}contents/life/posts/#{datetime}-#{slug}.md"

    header = <<-END
title: #{title}
date: #{datetime} 
template: life.jade

END

File.open(path, 'w') {|f| f << header }
system("mvim", path)
end
