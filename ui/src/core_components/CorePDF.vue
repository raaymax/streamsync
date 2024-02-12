<template>
  <div id="pageContainer">
    <div id="viewer" class="pdfViewer"></div>
  </div>
</template>

<script>
import pdfjsLib from "pdfjs-dist/build/pdf";
import { PDFViewer } from "pdfjs-dist/web/pdf_viewer";
import "pdfjs-dist/web/pdf_viewer.css";

pdfjsLib.GlobalWorkerOptions.workerSrc =
  "https://cdn.jsdelivr.net/npm/pdfjs-dist@2.0.943/build/pdf.worker.min.js";

export default {
  name: "PdfViewer",
  props: { docPath: String },
  mounted() {
    this.getPdf();
  },
  methods: {
    async getPdf() {
      let container = document.getElementById("pageContainer");
      let pdfViewer = new PDFViewer({
        container: container,
      });
      let pdf = await pdfjsLib.getDocument(this.docPath);
      pdfViewer.setDocument(pdf);
    },
  },
};
</script>

<style>
#pageContainer {
  margin: auto;
  width: 80%;
}

div.page {
  display: inline-block;
}
</style>


<template>
	<div class="CorePDF" :style="rootStyle" v-on:click="handleClick" ref="rootEl">
    <VuePdfEmbed class="pdf" annotation-layer text-layer :source="fields.source.value" :page="page"  @loaded="handleLoad" @rendered="handleDocumentRender"/>
		<div class="mask" />
	</div>
</template>

<script lang='ts'>
import { FieldCategory, FieldType } from "../streamsyncTypes";
import { cssClasses, secondaryTextColor } from "../renderer/sharedStyleFields";
import { getClick } from "../renderer/syntheticEvents";
import VuePdfEmbed from 'vue-pdf-embed'

// essential styles
import 'vue-pdf-embed/dist/style/index.css'

// optional styles
import 'vue-pdf-embed/dist/style/annotationLayer.css'
import 'vue-pdf-embed/dist/style/textLayer.css'

const description =
	"A component to embed a PDF document.";

const docs = `

`;

export default {
	streamsync: {
		name: "PDF",
		description,
		docs,
		category: "Content",
		fields: {
			source: {
				name: "Pdf source",
				type: FieldType.Text,
				desc: "either URL, Base64, binary, or document proxy",
			},
			cssClasses,
		},
	},
};
</script>

<script setup lang="ts">
import { Ref, computed, inject, ref } from "vue";
import injectionKeys from "../injectionKeys";

const rootEl:Ref<HTMLElement> = ref(null); 
const ss = inject(injectionKeys.core);
const fields = inject(injectionKeys.evaluatedFields);

function handleClick(ev: MouseEvent) {
	const ssEv = getClick(ev);
	rootEl.value.dispatchEvent(ssEv);
}
</script>

<style scoped>
@import "../renderer/sharedStyles.css";
.CorePDF{
  position: relative;
  width: 100%;
  height: 80vh;
}
.CorePDF .pdf {
  width: 100%;
  height: 100%;
  display: block;
  margin: auto;
  border-radius: 12px;
  border: 1px solid var(--separatorColor);
}
.CorePDF .mask {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0);
  border-radius: 12px;
}
.CorePDF.selected .mask {
  display: none;
}
</style>


<template>
  <div id="pageContainer">
    <div id="viewer" class="pdfViewer"></div>
  </div>
</template>

<script>
import pdfjsLib from "pdfjs-dist/build/pdf";
import { PDFViewer } from "pdfjs-dist/web/pdf_viewer";
import "pdfjs-dist/web/pdf_viewer.css";

pdfjsLib.GlobalWorkerOptions.workerSrc =
  "https://cdn.jsdelivr.net/npm/pdfjs-dist@2.0.943/build/pdf.worker.min.js";

export default {
  name: "PdfViewer",
  props: { docPath: String },
  mounted() {
    this.getPdf();
  },
  methods: {
    async getPdf() {
      let container = document.getElementById("pageContainer");
      let pdfViewer = new PDFViewer({
        container: container,
      });
      let pdf = await pdfjsLib.getDocument(this.docPath);
      pdfViewer.setDocument(pdf);
    },
  },
};
</script>

<style>
#pageContainer {
  margin: auto;
  width: 80%;
}

div.page {
  display: inline-block;
}
</style>
