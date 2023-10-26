from sentence_transformers import SentenceTransformer, util


class sts_module:

    def model_func(self,model, titles, thresholds, util):

        corpus_sentences = titles
        corpus_embeddings = model.encode(corpus_sentences, batch_size=128, show_progress_bar=True,
                                         convert_to_tensor=True)

        clusters = util.community_detection(corpus_embeddings, min_community_size=1, threshold=thresholds)
        final_titles = []

        for i, cluster in enumerate(clusters):
            token = 0
            result_titles = []
            for sentence_id in cluster:
                result_titles.append(corpus_sentences[sentence_id])
            if token == 0:
                final_titles.append(result_titles)

        return final_titles

    def sts_func(self,content_list):
        # Sbert수행
        model = SentenceTransformer('jhgan/ko-sbert-sts')
        titles=[]
        result = []
        for t,l in content_list:
            titles.append(t)
        # ------------------------------------ 아래부분 반복 수행 3회이상----------------------------------------------------
        threshold =0.66

        titles = self.model_func(model,titles,threshold,util)
        for t in titles:
            for content in content_list:
                if t[0] == content[0]:
                    result.append(content)

        return list(set(result))